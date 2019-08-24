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
        
    # Setting the flash message    
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
    
    # To obtain the numbering for ingredients
    i=0
    ingredient_numbering=[]
    while i<len(recipe_detail["ingredients"]):
        i+=1
        ingredient_numbering.append(i)
        
    # To obtain the numbering for preparation steps
    j=0
    prep_steps_numbering=[]
    while j<len(recipe_detail["prep_steps"]):
        j+=1
        prep_steps_numbering.append(j)
    
    return render_template("update-recipe.html", recipe_detail=recipe_detail, meat_selected=meat_selected, vegetable_selected=vegetable_selected, dessert_selected=dessert_selected, show_ingredients=zip( ingredient_numbering, recipe_detail["ingredients"] ), show_prep_steps=zip( prep_steps_numbering, recipe_detail["prep_steps"] ) )

# Route to process the form to update an existing recipe
@app.route("/update-recipe/<recipe_id>", methods=["POST"])
def process_update_recipe(recipe_id):
    
    # Get the form inputs
    name_input = request.form.get("recipe-name")
    nutrition_facts_input = request.form.get("nutrition-facts")
    cooking_time_input = request.form.get("cooking-time")
    type_input = request.form.get("type")
    ingredients_input=request.form.getlist("ingredientInput")
    prep_input=request.form.getlist("prepInput")
    
    # Using Mongo to update
    conn[RECIPE_DATABASE]["recipes"].update({
        "_id":ObjectId(recipe_id)
    }, {
        "$set": {
            "name":name_input,
            "nutrition_facts":nutrition_facts_input,
            "cooking_time":cooking_time_input,
            "type":type_input,
            "ingredients":ingredients_input,
            "prep_steps":prep_input
        }
    })
    
    # Set the flash message
    flash("You have updated recipe: " + name_input)
    
    return redirect(url_for("recipe_details", recipe_id=recipe_id))
    
# Route to confirm recipe deletion
@app.route("/confirm-delete-recipe/<recipe_id>")
def confirm_delete_recipe(recipe_id):
    
    recipe_detail = conn[RECIPE_DATABASE]["recipes"].find_one({
        "_id":ObjectId(recipe_id)
    })
    
    return render_template("confirm-delete-recipe.html", recipe_name=recipe_detail["name"], recipe_id=recipe_detail["_id"])

# Route to delete the recipe
@app.route("/delete-recipe/<recipe_id>")
def delete_recipe(recipe_id):
    
    recipe_detail = conn[RECIPE_DATABASE]["recipes"].find_one({
        "_id":ObjectId(recipe_id)
    })
    
    conn[RECIPE_DATABASE]["recipes"].delete_one({
        '_id':ObjectId(recipe_id)
    })
    
    flash("The recipe: {} has been deleted".format(recipe_detail["name"]))
    
    return redirect(url_for("recipe_list"))


if __name__ == '__main__':
    app.secret_key = os.environ.get('secret_app_key')
    app.config['SESSION_TYPE'] = os.environ.get('session_key')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
