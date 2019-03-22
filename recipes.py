# Created 24 July 2017

# Recipe catalog that keeps track of all my recipes

recipeCatalogList =["Scrambled Eggs", "Mug Cake"]

# Ingredients dictionary that stores the list of ingredients for this recipe

ingredientsDict = {
    "Scrambled Eggs" : [
        "eggs: 3",
        "olive oil: 2 TS",
        "grated cheese: 1 TBS",
        "salt: to taste",
        "pepper: to taste",
        "dried thyme: 1 TS"
    ],
    "Mug Cake" : [
        "flour: 1/4 cup",
        "white sugar: 1/4 cup",
        "cocoa powder : 2 TBS",
        "baking soda: 1/8 TS",
        "salt: 1/8 TS",
        "milk: 3 TBS"
        "canola oil: 2 TBS",
        "water: 1 TBS",
        "vanila extract: 1/4 TS"
    ]
}

# The dictionary that stores prep steps
prepStepsDict = {
    "Scrambled Eggs" : [
        "1. crack the eggs in a bowl and whisk",
        "2. in a pan that's heated pour the egg mixture",
        "3. once eggs are somewhat cooked, sprinkle salt, pepper, thyme, and cheese"
    ],
    "Mug Cake" : [
        "1. mix flour, sugar. cocoa powder, baking soda, and salt in mug",
        "2. stir in milk, canola oil, water, and vanilla extract",
        "3. microwave for 1 min 45 sec or until cake is done"
    ]
}

# This function will find and print a recipe
def findRecipe (recipeName) :
    recipeFound = 0

    # Printing all the ingredients in a recipe
    for recipe, ingredients in ingredientsDict.items():
        if recipe.lower() == recipeName.lower():
            recipeFound += 1
            print ("\nThis recipe is for:", recipeName)
            print("\nIngredients:")
            for item in ingredients:
                print(item)

    # Printing all the steps in a recipe
    for recipe, steps in prepStepsDict.items():
        if recipe.lower() == recipeName.lower():
            recipeFound += 1
            print("\nPreparation Steps:")
            for item in steps:
                print(item)
    return recipeFound

# This function will add a recipe
def addRecipe():
    newRecipe = input("Enter the name of the recipe you want to add: ")
    recipeCatalogList.append(newRecipe)
    ingredientsList = []
    newIngredients = input("Enter the name of the ingredients you want to add: ")
    ingredientsList.append(newIngredients)
    ingredientsDict.update({newRecipe: ingredientsList})
    stepsList = []
    newSteps = input("Enter the directions for the recipe: ")
    stepsList.append(newSteps)
    prepStepsDict.update({newRecipe: stepsList})
    return addRecipe

choiceLoop = True

while choiceLoop:
    addOrDisplay = input("Do you want to display a recipe or add? Type 'add' or 'display': ")
    if addOrDisplay == "add":
        addRecipe()
        choiceLoop = False
    elif addOrDisplay == "display":
        # Print the list of recipes available
        for recipe in recipeCatalogList:
            print (recipe)


        # Get input for the recipe that user wants to print
        selectRecipe = input("Please provide a recipe name from above: ")

        # Call function to find and print the recipe
        result = findRecipe(selectRecipe)

        # Evaluate result and print message accordingly
        if result == 0:
            print("Oops recipe not found!")
        elif result < 2:
            print("Sorry, this recipe does not look to be complete.")
        else:
            print("Recipe found and printed successfully!")
        choiceLoop = False
    else:
        print("Not an option!")

displayRecipe = input ("Do you want to see your recipes? Type 'yes' or 'no': ")
if displayRecipe == "yes":
    displayTrue = True
else:
    displayTrue = False

while displayTrue:
    # Print the list of recipes available
    for recipe in recipeCatalogList:
        print (recipe)

    # Get input for the recipe that user wants to print
    selectRecipe = input("Please provide a recipe name from above: ")

    # Call function to find and print the recipe
    result = findRecipe(selectRecipe)

    # Evaluate result and print message accordingly
    if result == 0:
        print("Oops recipe not found!")
    elif result < 2:
        print("Sorry, this recipe does not look to be complete.")
    else:
        print("Recipe found and printed successfully!")
    displayTrue = False
