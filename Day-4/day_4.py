import random

rock = "Rock"
paper = "Paper"
scissor = "Scissor"

user_input = int(input("Please chose your move. Rock(0), Paper(1), Scissor(2).\n"))

computer_choice = random.randint(0, 2)
print(computer_choice)
if computer_choice == user_input:
    print("TIE!")
elif (user_input - computer_choice) % 3 == 1:
    print("You Win!")
else:
    print("You Lose!")
    