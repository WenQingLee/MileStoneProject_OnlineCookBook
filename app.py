from flask import Flask, render_template
import os
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Create the connection to MongoDB
conn = pymongo.MongoClient(os.getenv("MONGO_URI"))

# Define the Database used for easy reference and future updates
RECIPE_DATABASE = 'online_cookbook'

@app.route("/")
def index():
    
    recipes = conn[RECIPE_DATABASE]["recipes"].find({})
    
    type_meat = conn[RECIPE_DATABASE]["recipes"].find({"type":"meat"})
    
    type_vegetable = conn[RECIPE_DATABASE]["recipes"].find({"type":"vegetable"})
    
    type_dessert = conn[RECIPE_DATABASE]["recipes"].find({"type":"dessert"})
    
    return render_template("index.html", recipes=recipes, type_meat=type_meat, type_vegetable=type_vegetable, type_dessert=type_dessert)

@app.route("/recipe-list")
def recipe_list():
    
    type_meat = conn[RECIPE_DATABASE]["recipes"].find({"type":"meat"})
    
    type_vegetable = conn[RECIPE_DATABASE]["recipes"].find({"type":"vegetable"})
    
    type_dessert = conn[RECIPE_DATABASE]["recipes"].find({"type":"dessert"})
    
    return render_template("recipes-list.html", type_meat=type_meat, type_vegetable=type_vegetable, type_dessert=type_dessert)

@app.route("/recipe-details/<recipe_id>")
def recipe_details(recipe_id):
    
    recipe_detail = conn[RECIPE_DATABASE]["recipes"].find_one({
        "_id":ObjectId(recipe_id)
    })
    
    # Use the objectid to find the "ingredients" to find the prep_steps in the referenced document
    ingredients_list = conn[RECIPE_DATABASE]["ingredients"].find_one({
        "_id":ObjectId(recipe_detail["ingredients"])
    })
    
    # Declare the variables to be used in the while loop to contain the ingredients n an array
    i=1
    show_ingredients = []
    
    # While loop to append the ingredients into a new array called show_ingredients
    while i < len(ingredients_list):
        show_ingredients.append(ingredients_list[str(i)])
        i = i+1

    # Use the objectid for the "prep_steps" to find the prep_steps in the referenced document 
    prep_steps_list = conn[RECIPE_DATABASE]["prep_steps"].find_one({
        "_id":ObjectId(recipe_detail["prep_steps"])
    })
    
    # Declare the variables to be used in the while loop to contain the prep_steps in an array
    j=1
    show_prep_steps = []
    
    # While loop to append the steps into a new array called show_prep_steps
    while j < len(prep_steps_list):
        show_prep_steps.append(prep_steps_list[str(j)])
        j = j+1
    
    return render_template("recipe-detail.html", recipe_detail=recipe_detail, show_ingredients=show_ingredients, show_prep_steps=show_prep_steps)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
