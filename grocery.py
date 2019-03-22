# Created 29 June 2017
grocery = []

keepAdding = True

while keepAdding:
    groceryItem = input("Enter item to add to grocery list: ")
    grocery.append(groceryItem)

    #Check if the user wants to keep adding
    addMoreItems = input("Do you want to add more items Y/N ? ")

    if addMoreItems.upper() == "Y".upper():
        keepAdding = True
    else:
        keepAdding = False

print ("This is my grocery list:")
for item in grocery:
    print(item)

print ("Your grocery list has", len(grocery), "item(s)")

removeItems = input("Do you want to remove any items Y/N ? ")
if removeItems.upper() == "Y".upper():
    keepRemoving = True
else:
    keepRemoving = False

while keepRemoving:
    falseItem = True
    while falseItem:
        removedItem = input("Enter item to remove from grocery list: ")
        if removedItem in grocery:
            grocery.remove(removedItem)
            falseItem = False
        else:
            print ("Not in list!")
            if len(grocery) > 0:
                falseItem = True
            else:
                falseItem = False

    removeMoreItems = input("Do you want to remove more items Y/N ? ")

    if removeMoreItems.upper() == "Y".upper():
        if len(grocery) > 0:
            keepRemoving = True
        else:
            print("No items to remove!")
            keepRemoving = False
    else:
        keepRemoving = False

print ("This is my grocery list:")
for item in grocery:
    print(item)

print ("Your grocery list has", len(grocery), "item(s)")

anythingElse = input("Would you like to add or remove any more items Y/N ? ")

if anythingElse.upper() == "Y".upper():
    addOrRemove = input("Add or remove?: ")
    if addOrRemove.upper() == "ADD".upper():
        keepAdding = True
    elif addOrRemove.upper() == "REMOVE".upper():
        keepRemoving = True
else:
    printAgain = input("Would you like to see your list again Y/N ? ")
    if printAgain.upper() == "Y".upper():
        print ("This is my grocery list:")
        for item in grocery:
            print(item)

        print ("Your grocery list has", len(grocery), "item(s)")
