# Cookit-Mons

Data Centric Development Milestone Project  

## Index

1. [Project Purpose](#project-purpose)
2. [UX](#ux)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## <a name="project-purpose">Project Purpose</a>


The premise of Cookit-Mons is:
1. For chefs and home cooks to find and share recipes
2. Raise awareness of MAC knives


## <a name="ux">UX</a>

The goal in the design is to present data in a systematic approach that encourages first time learning

The user stories considered are:
* I want to be able to contribute a new recipe for everyone to view
* I want to be able to read my recipe and other people's recipes
* I want to be able to update/improve any existing recipes
* I want to be able to delete the recipes if they are incomplete or not usable
* I want to be able to raise awareness of MAC knives

A tree structure information architecture is used for the website as it reduces complexity and only reveals information as the user navigate and transverse up and down the tree.

The color orange is predominately used in this website as it is an appetizing and trendy color. The color blue is used for the logo and Cookit-Mons is an amalgamation of the words (1) cook, (2) it and (3) mon (a reference to the jamaican phrase "Ya Mon").

To reduce cognitive oveerload, the user will also not be required to go beyond 3 clicks to get to their destination.

The ER diagram, scope and wireframe can be found under the scope and skeleton folder.

## <a name="features">Features</a> 

### Existing Features

1. Home/Index Page
    * Mobile responsive Navigation bar that allows easy navigation to either (1) Submit a recipe or (2) Search the existing recipes
    * Carousel introducting the user to the MAC knives (Clicking it will open a new window to the knife's details)
2. Submit a recipe page
    * Mobile responsive Navigation bar that allows easy navigation to either (1) Submit a recipe or (2) Search the existing recipes
    * Mobile responsive Breadcrumb navigation trail
    * Input fields for the recipes
    * Add and remove buttons for ingredients and preparation steps for the user to use accordingly
    * Input fields are to be filled up before the recipe may be submitted. For the inputs of ingredients and preparation steps, it is dependent on the number of input fields the user added.
    * Submit button for the user to add new recipes
    * Once the recipe is submitted, the user will be redirected to the recipe list page with a flashed message that the recipe has been added.
3. Recipe-list Page
    * Mobile responsive Navigation bar that allows easy navigation to either (1) Submit a recipe or (2) Search the existing recipes
    * Mobile responsive Breadcrumb navigation trail
    * The recipes are categorised according to the types and sorted alphabetically: (1) Meat Recipes, (2) Vegetable Recipes, (3) Desserts
    * Mobile responsive cards that reveal the recipes when clicked
    * Carousel introducing the user to the MAC knives (Clicking it will open a new window to the knife's details)
    * The user may click on the individual recipes for the details of the recipe
4. Recipe-detail Page
    * Mobile responsive Navigation bar that allows easy navigation to either (1) Submit a recipe or (2) Search the existing recipes
    * Mobile responsive Breadcrumb navigation trail
    * Dashboard with the recipe details such as Name, Nutrition, Cooking Time, Type of recipe, Ingredients and Preparation Steps
    * Buttons to either update or delete the recipe
5. Update-recipe Page
    * Mobile responsive Navigation bar that allows easy navigation to either (1) Submit a recipe or (2) Search the existing recipes
    * Mobile responsive Breadcrumb navigation trail
    * Input fields for the recipes (With the previous recipes inputs for easy reference)
    * Input fields are to be filled up before the recipe may be updated. For the inputs of ingredients and preparation steps, it is dependent on the number of input fields the user added.
    * Update button for the user to add new recipes
    * Once the recipe is updated, the user will be redirected to the recipe details page with a flashed message that the recipe has been updated.
6. Confirm-delete-recipe Page
    * Mobile responsive Navigation bar that allows easy navigation to either (1) Submit a recipe or (2) Search the existing recipes
    * Mobile responsive Breadcrumb navigation trail
    * If the user clicks no, they will be redirected back to the recipe details page
    * If the user clicks yes, they will be redirected back to the recipe lists page with a flashed message that informs them that the recipe has been deleted.

### Features left to implement
1. To allow the user to upload files
2. User authentication (Register/Login/Logout)
3. To promote the MAC knife tools that are specific to each recipe type by using referenced documents (e.g. cleavers for meat recipes and paring knives for vegetable recipes)


## <a name="technologies-used">Technologies Used</a>
1. HTML (https://www.w3schools.com/html/html_intro.asp)
2. CSS (https://www.w3schools.com/css/)
3. Materialize (https://materializecss.com/): The frontend was built using Materialize framework
4. Javascript (https://www.javascript.com/)
5. JQuery (https://jquery.com/): The project uses JQuery to simplify DOM manipulation.
6. Python (https://www.python.org/)
7. PyMongo (https://api.mongodb.com/python/current/)
8. Flask with Jinja2 (https://github.com/pallets/flask)
9. MongoDB (https://www.mongodb.com/): MongoDB was used as a database

## <a name="testing">Testing</a>

### Manual Testing

1. Home/Index Page
    * Navigation bar is mobile responsive and links to the correct pages.
    * Carousel is working that introduces the user to the MAC knives. Clicking on the link will open a new window to the knife's details
2. Submit a recipe page
    * Navigation bar is mobile responsive and links to the correct pages
    * Breadcrumb navigation trail is mobile responsive and links to the correct pages
    * Input fields for the recipes are required to be filled up before submission (String for Recipe Name, Ingredients and Preparation Steps. Numbers for Nutrition Facts and Cooking Time)
    * Dropdown list is working
    * Add and remove buttons for ingredients and preparation steps creates and removes an input field respectively.
    * Input fields are to be filled up before the recipe may be submitted. For the inputs of ingredients and preparation steps, it is dependent on the number of input fields the user added.
    * Submit button for the user to add new recipes is working
    * Once the recipe is submitted, the user is redirected to the recipe list page with a flashed message that the recipe has been added.
3. Recipe-list Page
    * Navigation bar is mobile responsive and links to the correct pages
    * Breadcrumb navigation trail is mobile responsive and links to the correct pages
    * The recipes are categorised according to the types and sorted alphabetically: (1) Meat Recipes, (2) Vegetable Recipes, (3) Desserts
    * Mobile responsive cards reveal the list of recipes when clicked
    * Carousel introducing the user to the MAC knives (Clicking it opens a new window to the knife's details)
    * The user may click on the individual recipes for the details of the recipe
4. Recipe-detail Page
    * Navigation bar is mobile responsive and links to the correct pages
    * Breadcrumb navigation trail is mobile responsive and links to the correct pages
    * Dashboard with the recipe details such as Name, Nutrition, Cooking Time, Type of recipe, Ingredients and Preparation Steps
    * Buttons to either update or delete the recipe
5. Update-recipe Page
    * Navigation bar is mobile responsive and links to the correct pages
    * Breadcrumb navigation trail is mobile responsive and links to the correct pages
    * Input fields are filled with the previous recipes inputs
    * Add and remove buttons for ingredients and preparation steps creates and removes an input field respectively.
    * Input fields are to be filled up before the recipe may be submitted. For the inputs of ingredients and preparation steps, it is dependent on the number of input fields the user added.
    * Update button for the user to update recipes
    * Once the recipe is updated, the user will be redirected to the recipe details page with a flashed message that the recipe has been updated and the details reflecting it.
6. Confirm-delete-recipe Page
    * Navigation bar is mobile responsive and links to the correct pages
    * Breadcrumb navigation trail is mobile responsive and links to the pages
    * If the user clicks no, they will be redirected back to the recipe details page
    * If the user clicks yes, they will be redirected back to the recipe lists page with a flashed message that informs them that the recipe has been deleted.
    * The recipe is deleted and recipe list has been updated

## <a name="deployment">Deployment</a>

The website has been deployed at https://wq-cookit.herokuapp.com/


### Heroku Deployment (Debug value changed to false for deployment)

1. Sign up for a Heroku Account (https://www.heroku.com/)
2. Install Heroku using bash:
    * nvm i v8 npm 
    * install -g heroku 
3. Log into Heroku in bash
    * heroku login -i
4. Create a new app called wq-cookit
    * heroku create wq-cookit
5. Check that the new remote has been added
    * git remote -v
6. Install gunicorn
    * pip3 install gunicorn
7. Create a file named "Procfile", add the following line and save it
    * web gunicorn app:app 
8. Create the requirements file using bash
    * pip3 freeze --local > requirements.txt
9. Commit and push the project to heroku
    * git add .
    * git commit -m "<commit message>"
    * git push heroku master
10. Install --classic heroku
    *sudo snap install --classic heroku
11. Set the environment variables by using heroku config:set <WHATEVER=VALUE>
    * Set MONGO_URI config by typing this in the CLI: 
        heroku config:set MONGO_URI=(input here)
12. To check the current existing config variables
    * heroku config

### To re-generate requirements.txt after installing more packages
1. pip3 freeze --local > requirements.txt
2. git add .
3. git commit -m ​"Updated requirements.txt" 
4. git push heroku master 


### Running the application locally
1. Create a new workspace in C9 with a workspace name and description
2. Clone the github repository at https://github.com/WenQingLee/MilestoneProject_OnlineCookbook
3. Install requirements
    * pip3 install -r requirements.txt
4. The secret key and session key has to be created in the environment 
5. In app.py set debug to True.
6. To run the application locally, type python3 app.py

## <a name="credits">Credits</a>
### Content
The recipes were copied from the following sites: https://www.allrecipes.com/, https://www.delish.com/, https://www.blueapron.com/pages/sample-recipes

The logo was obtained from freelogodesign: https://www.freelogodesign.org/

The source of knives were taken from the MAC knives webpage: https://www.macknife.com/ 

### Media
The photos used in this site were obtained from Pexels and the following sites: https://www.allrecipes.com/, https://www.delish.com/, https://www.blueapron.com/pages/sample-recipes

### Acknowledgements
I received inspiration for this project from the following sites:
* Website Layout: https://www.blueapron.com/pages/sample-recipes
* Colors: https://jenndavid.com/colors-that-influence-food-sales/
