from flask import Flask, render_template
import os
import pymongo

app = Flask(__name__)

# Creating the connection to Mongo
app.config["MONGO_DBNAME"] = "online_cookbook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


# Create the connection
conn = pymongo.MongoClient(os.getenv("MONGO_URI"))


@app.route("/")
def hello():
    return "hello"



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
