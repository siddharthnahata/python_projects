import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def cal_score(deal):
    if sum(deal) == 21 and len(deal) == 2: 
        return 0
    
    if 11 in deal and sum(deal) > 21:
        deal.remove(11)
        deal.append(1)
        
    return sum(deal)

                
print("Lets Play BlackJack!!")
wanna_play_more = True
while wanna_play_more:
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    
    game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_over:
        user_score = cal_score(user_cards)
        computer_score = cal_score(computer_cards)
        if user_score == 0:
            user_score = "Black Jack"
            print(f"Your Crads are {user_cards}, Your Have a {user_score}")
            game_over = True
            break
        print(f"Your Crads are {user_cards}, Your score is {user_score}")
        print(f"Dealer Open Card is {computer_cards[1]}")
        
        
        
        if computer_cards == 0 or user_score > 21 or user_score == 21:
            game_over = True
        else:
            one_more = input("Do you want one more card. Y/N? ").lower()
            if one_more == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
                
    while computer_score < 17 and computer_score != 0:
        if user_score == 0:
            break
        computer_cards.append(deal_card())
        computer_score = cal_score(computer_cards)
        
    
    if computer_score == 0:
        computer_score = "Black Jack"    
        
    print(f"Dealer Cards are {computer_cards} and Dealer has: {computer_score}")
    
    
    if user_score == computer_score:
        if user_score > 21 :
            print("You Bust!!\nYou Lost.")
        else:
            print("You Have a Push!!")
    elif user_score == "Black Jack":
        print("Black Jack!!\nYou Won!!")
    elif computer_score == "Black Jack":
        print("Black Jack for the dealer\nYou Lost.")
    if user_score > 21:
        print("You Bust!!\nYou Lost.")
    elif computer_score > 21:    
        print("Dealer Bust!!\nYou Won!!")
    elif user_score > computer_score:
        print("You Won!!")
    elif user_score < computer_score:
        print("You Lost.")
    
   
    wanna_play = input("Do You want to play more Black jack. Y/N? " ).lower()
    if wanna_play == "n":
        wanna_play_more = False
    else:
        print("\n"*100)
    