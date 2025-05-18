from day import data
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_location = account["location"]
    return f"{account_name}, a {account_description}, from {account_location}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(f"Welcome to the High Low game. Let's Begin!!")
game_status = True
highest_score = 0

while game_status:
    current_game_status = True
    score = 0
    account_a = random.choice(data)
    while current_game_status:
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        print(f"Compare A: {format_data(account_a)}")
        print("\n" * 5)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers. A/B? ").lower()

        a_follower_count = account_a["followers"]
        b_follower_count = account_b["followers"]

        if highest_score < score:
            highest_score = score
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        if is_correct:
            score += 1
            account_a = account_b
            print("\n"*35)
            print(f"You guessed it correct. Your current score is {score}.")
        else:
            print(f"You guessed it incorrect you score is {score}, Your highest score is {highest_score}")
            current_game_status = False
            score = 0
            play_more = input("Do you want to play more. Y/N? ").lower()
            if play_more == "n":
                game_status = False
            else:
                print("\n"*35)

