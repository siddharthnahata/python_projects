choice_1 = input("Where do you want to goo. Right/Left? ").lower()


if choice_1 == "left":
    print("You have succussfully completed level 1. \nNow here in huge river.")
    choice_2 = input("Would you like to swim or wait for boat. Swim/wait? ").lower()
    if choice_2 == "wait":
        print("Boat is arrived. \nYou coverd the river succussfully! \nWe can see three gate. ")
        choice_3 = input("Which gate will you go to. Red/Blue/Yellow? ").lower()
        if choice_3 == "red":
            print("Burned by fire. \nGame Over.")
        elif choice_3 == "blue":
            print("Eaten by beasts. \nGame Over")
        elif choice_3 == "yellow":
            print("You Win!")
        else:
            print("Incorrect Input please try again. ")
    elif choice_2 == "swim":
        print("Attacked by trout. \nGame Over")
    else:
        print("Incorrect Input please try again. ")
elif choice_1 == "right":
    print("You fell into the hole.\nGame Over!")
else:
    print("Incorrect Input please try again. ")