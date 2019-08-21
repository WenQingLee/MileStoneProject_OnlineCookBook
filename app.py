from flask import Flask, render_template
import os
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Create the connection to MongoDB
conn = pymongo.MongoClient(os.getenv("MONGO_URI"))


@app.route("/")
def index():
    
    recipes = conn["online_cookbook"]["recipes"].find({})
    
    type_meat = conn["online_cookbook"]["recipes"].find({"type":"meat"})
    
    type_vegetable = conn["online_cookbook"]["recipes"].find({"type":"vegetable"})
    
    type_dessert = conn["online_cookbook"]["recipes"].find({"type":"dessert"})
    
    return render_template("index.html", recipes=recipes, type_meat=type_meat, type_vegetable=type_vegetable, type_dessert=type_dessert)

@app.route("/recipe-list")
def recipe_list():
    
    type_meat = conn["online_cookbook"]["recipes"].find({"type":"meat"})
    
    type_vegetable = conn["online_cookbook"]["recipes"].find({"type":"vegetable"})
    
    type_dessert = conn["online_cookbook"]["recipes"].find({"type":"dessert"})
    
    return render_template("recipes-list.html", type_meat=type_meat, type_vegetable=type_vegetable, type_dessert=type_dessert)

@app.route("/recipe-details/<recipe_id>")
def recipe_details(recipe_id):
    
    recipe_detail = conn["online_cookbook"]["recipes"].find_one({
        "_id":ObjectId(recipe_id)
    })
    
    # Obtain the objectid for the "ingredients" referenced document
    ingredients_ref = recipe_detail["ingredients"]
    
    # Use the objectid to find the ingredients list
    ingredients_list = conn["online_cookbook"]["ingredients"].find_one({
        "_id":ObjectId(ingredients_ref)
    })
    
    # Declare the variables to be used in the while loop to obtain the ingredients
    i=1
    show_ingredients = []
    
    # While loop to append the ingredients into a new array called show_ingredients
    while i < len(ingredients_list):
        show_ingredients.append(ingredients_list[str(i)])
        i = i+1

    # Obtain the objectid for the "prep_steps" referenced document
    prep_steps_ref = recipe_detail["prep_steps"]
    
    # Use the objectid to find the prep_steps
    prep_steps_list = conn["online_cookbook"]["prep_steps"].find_one({
        "_id":ObjectId(prep_steps_ref)
    })
    
    # Declare the variables to be used in the while loop to obtain the prep_steps
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
