from flask import Flask, render_template, request, flash, redirect, url_for
import os
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Create the connection to MongoDB
conn = pymongo.MongoClient(os.getenv("MONGO_URI"))

# Define the Database used for easy reference and future updates
RECIPE_DATABASE = 'online_cookbook'

# Route to homepage
@app.route("/")
def index():
    
    recipes = conn[RECIPE_DATABASE]["recipes"].find({})
    
    type_meat = conn[RECIPE_DATABASE]["recipes"].find({"type":"meat"})
    
    type_vegetable = conn[RECIPE_DATABASE]["recipes"].find({"type":"vegetable"})
    
    type_dessert = conn[RECIPE_DATABASE]["recipes"].find({"type":"dessert"})
    
    return render_template("index.html", recipes=recipes, type_meat=type_meat, type_vegetable=type_vegetable, type_dessert=type_dessert)

# Route to recipes list
@app.route("/recipe-list")
def recipe_list():
    
    type_meat = conn[RECIPE_DATABASE]["recipes"].find({"type":"meat"})
    
    type_vegetable = conn[RECIPE_DATABASE]["recipes"].find({"type":"vegetable"})
    
    type_dessert = conn[RECIPE_DATABASE]["recipes"].find({"type":"dessert"})
    
    return render_template("recipes-list.html", type_meat=type_meat, type_vegetable=type_vegetable, type_dessert=type_dessert)

# Route to recipe details
@app.route("/recipe-details/<recipe_id>")
def recipe_details(recipe_id):
    
    recipe_detail = conn[RECIPE_DATABASE]["recipes"].find_one({
        "_id":ObjectId(recipe_id)
    })
    
    return render_template("recipe-detail.html", recipe_detail=recipe_detail, show_ingredients=recipe_detail["ingredients"], show_prep_steps=recipe_detail["prep_steps"])

# Route to form to submit a new recipe
@app.route("/submit-recipe")
def submit_recipe():
    return render_template("submit-recipe.html")
    
# Route to process the form to submit a new recipe
@app.route("/submit-recipe", methods=["POST"])
def process_submit_recipe():
    
    # Getting the inputs from the form submitted
    name_input = request.form.get("recipe-name")
    nutrition_facts_input = request.form.get("nutrition-facts")
    cooking_time_input = request.form.get("cooking-time")
    type_input = request.form.get("type")
    
    ingredients_input=request.form.getlist("ingredientInput")
    prep_input=request.form.getlist("prepInput")
    
    # Insert the recipe into a new document
    conn[RECIPE_DATABASE]["recipes"].insert({
            "name":name_input,
            "nutrition_facts":nutrition_facts_input,
            "cooking_time":cooking_time_input,
            "type":type_input,
            "ingredients":ingredients_input,
            "prep_steps":prep_input
        })
        
    flash("You have created the new recipe: " + name_input)
    
    return redirect(url_for("recipe_list"))

# Route to process the form to update a recipe
@app.route("/update-recipe/<recipe_id>")
def update_recipe(recipe_id):
    
    recipe_detail = conn[RECIPE_DATABASE]["recipes"].find_one({
        "_id":ObjectId(recipe_id)
    })
    
    # Declaring variables for recipe types 
    meat_selected=""
    vegetable_selected="" 
    dessert_selected=""
    
    # if else statement to pass the selected type into the update form
    if recipe_detail["type"] == "meat":
        meat_selected = "selected"
    elif recipe_detail["type"] == "vegetable":
        vegetable_selected = "selected"
    else: 
        dessert_selected = "selected"
    
    print(recipe_detail["ingredients"])
    
    i=0
    ingredient_numbering=[]
    while i<len(recipe_detail["ingredients"]):
        i+=1
        ingredient_numbering.append(i)
        print (ingredient_numbering)
        
    
    return render_template("update-recipe.html", recipe_detail=recipe_detail, meat_selected=meat_selected, vegetable_selected=vegetable_selected, dessert_selected=dessert_selected, show_ingredients=zip( ingredient_numbering, recipe_detail["ingredients"] ) )


if __name__ == '__main__':
    app.secret_key = os.environ.get('secret_app_key')
    app.config['SESSION_TYPE'] = os.environ.get('session_key')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
