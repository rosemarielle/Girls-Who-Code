gameOn = True

while gameOn:
    name = input("What's your name?: ")
    print("You start off at your cabin, only to find that you're not alone.")
    print("You hear a noise and see killer clowns inside your house.")
    print("You try to run, but one comes up from behind, grabs you, and ties you to a chair.")
    print("The clowns decide to go outside, and you use that time to escape.")
    answer3 = True
    while answer3 == True:
        print("Where do you want to go?")
        print("Type 'left' to go left or 'right' to go right.")
        user_input = input()
        if user_input.lower() == "left".lower():
            print("You decide to go left and find a forest.")
            print("Hide or look for people?")
            answer3 = False
            user_input = input()
            if user_input.lower() == "hide".lower():
                print("Where do you want to hide?")
                print("Bush, tree, or lake?")
                user_input = input()
                if user_input.lower() == "bush".lower():
                    print("Game Over")
                    print("You were unable to keep quiet and got caught by the killer clowns.")
                elif user_input.lower() == "tree".lower():
                    print("You fall off and die!")
                    print("Game Over")
                elif user_input.lower() == "lake".lower():
                    print("The lake was too cold and you died from hypothermia.")
                    print("Game Over")
                else:
                    print("Invalid option!")
            elif user_input.lower() == "look for people".lower():
                print("You find people who hunt killer clowns")
                print("Stay with them or keep running?")
                user_input = input()
                if user_input.lower() == "stay with them".lower():
                    print("You kill the clowns together and live.")
                    print("Congratulations %s. You live. But beware, they might come back." %name)
                elif user_input.lower() == "keep running".lower():
                    print("The clowns find you alone and kill you.")
                    print("Game Over")
                else:
                    print("Invalid option!")
            else:
                print("Invalid option!")
        elif user_input.lower() == "right".lower():
            answer3 = False
            answer1 = True
            while answer1 == True:
                print("You choose to go right and run into more clowns")
                print("Run or give up?")
                user_input = input()
                if user_input.lower() == "run".lower():
                    print("You escape but get dehydrated and pass out.")
                    print("You wake up in a hospital, away from the killer clowns.")
                    print("Congratulations %s. You live. But beware, they might come back." %name)
                    answer1 = False
                elif user_input.lower() == "give up".lower():
                    print("The clowns stab you to death.")
                    print("Game Over")
                    answer1 = False
                else:
                    print("Invalid option!")
        else:
            print("Invalid option!")
    answer2 = True
    while answer2 == True:
        answer = input("Do you want to play again? Yes or no: ")
        if answer.lower() == "yes".lower():
            gameOn = True
            answer2 = False
        elif answer.lower() == "no".lower():
            gameOn = False
            answer2 = False
        else:
            print("Invalid Option!")
