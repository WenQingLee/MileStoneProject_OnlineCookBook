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



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
