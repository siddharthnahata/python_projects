from day import data
import random

highest_score = 0
score = 0
def compare(a, b, x):
  a_follow = a["followers"]
  b_follow = b["followers"]

  if x == "a":
    if a_follow > b_follow:
      global score
      score += 1
      return
    else:
      return False
  else:
    if b_follow > a_follow:
      score += 1
      return
    else:
      return False
big_game = True

while big_game:
  score = 0
  game = True
  while game:
    print(f"Your current score is score {score}")
    random_a = random.choice(data)
    while game:

      random_b = random.choice(data)
      while random_b == random_a:
        random_b = random.choice(data)

      print(f"Compare A: {random_a["name"]}, a {random_a["description"]} from {random_a["location"]} ")
      print("\n" * 2)
      print(f"Compare B: {random_b["name"]}, a {random_b["description"]} from {random_b["location"]} ")
      guess = input("Make your guess. A/B? ").lower()
      print("\n" * 20)

      if compare(random_a, random_b, guess) is False:
        game = False
        if highest_score < score:
          highest_score = score
          print(f"You are incorrect your score is {score}, Your new highest score is {highest_score}")
        else:

          print(f"You are incorrect your score is {score}, Your highest was score is {highest_score}")
      random_a = random_b

  more = input("Do you want to play more. Y/N? ")
  if more == "y":
    continue
  else:
    big_game = False
