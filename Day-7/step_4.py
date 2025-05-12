import random
word_list = ["dog", "cammel", "mango"]

#Task_1 
word = random.choice(word_list)


placeholder = "-" * len(word)

print(placeholder)

#Task_2
game_over = False


display_list = []

lives_count = 6

while not game_over:
    entered_input = input("\nPlease enter a letter.\n")
    display = ""
    
    
    if len(entered_input) >= 2:
        print("Please enter single word at a time. You Lost a life")
    
    if entered_input in display_list:
        print(f"You already have letter '{entered_input}'" )
    
    for letter in word:
        if entered_input == letter:
            display += entered_input
            display_list.append(letter) 
        elif letter in display_list:
            display += letter
        else: 
            display += "-"
            
   
    print(display)
    
    if entered_input not in word:
        lives_count -= 1
        print("You lose 1 live.")
        if lives_count == 0:
            game_over = True
            print("Game Over!!\nYou Lose!!")
    print("Remaining lives: ",lives_count)
    if "-" not in display:
        game_over = True
        print("Game Over!!\nYou Won!!")
        
        
        
        
        
        