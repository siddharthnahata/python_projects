import random
word_list = ["dog", "cammel", "mango"]

#Task_1 
word = random.choice(word_list)
print(word)

#Task_2
entered_input = input("Please enter a letter.\n")

for letter in word:
    if entered_input == letter:
        print("Right")
    else: 
        print("Wrong")
