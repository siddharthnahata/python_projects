import random
word_list = ["dog", "cammel", "mango"]

#Task_1 
word = random.choice(word_list)
print(word)


placeholder = "-" * len(word)

print(placeholder)

#Task_2
game_over = False


display_list = []

lives_count = 5

while lives_count == 0:
    while not game_over:
        entered_input = input("\nPlease enter a letter.\n")
        display = ""
        
        for letter in word:
            if entered_input == letter:
                display += entered_input
                display_list.append(letter)
            elif letter in display_list:
                display += letter
            else: 
                display += "-"
                lives_count -= 1
        
        print(display)
        
        if "-" not in display:
            game_over = True
            