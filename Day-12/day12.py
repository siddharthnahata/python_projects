import random

def guess_num():
    print("Welcome to the Guessing Number game!!")
    print("I am thinking a number between 1 - 100")
    
    computer_number = random.randint(1, 100)
    
    lives = 0
    difficulty = input("choose the difficulty. Hard/Easy? ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    print(f"You have {lives} attempts to make the correct guess. ") 
    
    guess = 0
    
    while guess != computer_number or lives > 0:
        guess = int(input("Nake the Guess. "))
        if guess == computer_number:
            print("Yay! You guessed the correct number. ")
        elif guess !=  computer_number:
            if guess > computer_number:     
                print("Too high")
            elif guess < computer_number:
                print("Too Low")
            lives -= 1
        if lives > 0:
            print(f"You have {lives} attemps left.")
        else:
            print("You ran out of lives")
            return
    return
    
guess_num()