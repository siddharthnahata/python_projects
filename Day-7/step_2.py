import random
word_list = ["dog", "cammel", "mango"]

#Task_1 
word = random.choice(word_list)
print(word)


placeholder = "-" * len(word)

print(placeholder)

#Task_2
entered_input = input("\nPlease enter a letter.\n")

display = ""
for letter in word:
    if entered_input == letter:
        display += entered_input 
    else: 
        display += "-"

print(display)