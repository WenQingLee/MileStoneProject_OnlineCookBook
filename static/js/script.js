// To initialise the navbar
$(document).ready(function(){
    $('.sidenav').sidenav();
  });

// To initisalise the carousel elements
 $(document).ready(function(){
    $('.carousel').carousel();
  });

// To initialise the select element in submit-recipe.html
$(document).ready(function() {
  $('select').formSelect();
});

// To add an input field for ingredients when the add button is clicked
$("#add-ingredient").on("click", function() {
  let i = $("#ingredients-input div").length + 1;
  $("#ingredients-input").append('<div class="input-field col s12"> Ingredient ' + i + '<input placeholder="Ingredient" name="ingredientInput" type="text" class="validate" required></div>');
});

// To remove an input field for ingredients when the remove button is clicked
$("#remove-ingredient").on("click", function() {
  $("#ingredients-input > div").last().remove();
});

// To add an input field for preparations when the add button is clicked
$("#add-prep").on("click", function() {
  let j = $("#preparations-input div").length + 1;
  $("#preparations-input").append('<div class="input-field col s12"> Step ' + j + '<input placeholder="Preparation Step" name="prepInput" type="text" class="validate" required></div>');
});

// To remove an input field for preparationss when the remove button is clicked
$("#remove-prep").on("click", function() {
  $("#preparations-input > div").last().remove();
});