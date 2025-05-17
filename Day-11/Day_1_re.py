import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)

print("Let's Play BlackJack!!")
wanna_play_more = True

while wanna_play_more:
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    game_over = False

    while not game_over:
        user_score = cal_score(user_cards)
        computer_score = cal_score(computer_cards)

        print(f"Your Cards are {user_cards}, your score is {user_score if user_score != 0 else 'Blackjack!'}")
        print(f"Dealer's open card is {computer_cards[1]}")
        
        if user_score == 0 or user_score > 21:
            game_over = True
        else:
            more = input("Do you want another card? (Y/N): ").lower()
            if more == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = cal_score(computer_cards)

    print(f"\nDealer's cards: {computer_cards}, Dealer's score: {computer_score if computer_score != 0 else 'Blackjack!'}")

    # Determine the result
    if user_score == computer_score:
        print("Push! It's a tie.")
    elif user_score == 0:
        print("Blackjack! You win!")
    elif computer_score == 0:
        print("Dealer has Blackjack. You lose.")
    elif user_score > 21:
        print("You busted. You lose.")
    elif computer_score > 21:
        print("Dealer busted. You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose.")

    again = input("\nDo you want to play another round? (Y/N): ").lower()
    if again != "y":
        wanna_play_more = False
    else:
        print("\n" * 100)
