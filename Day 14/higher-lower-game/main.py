import random
from game_data import data
from arts import logo, vs
import os 

def clear():
  os.system('cls')

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]

  return f"{name}, a {description}, from {country}"
  

def get_random_account(A):
  while True:
    B = random.choice(data)
    if A!=B:
      break 
  return B

def higher_one(A, B):
  if A["follower_count"] > B["follower_count"]:
    return "a"
  else:
    return "b"


def game():
  print(logo)
  A = random.choice(data)
  
  gameOver = False
 
  score = 0

  while not gameOver:
    
    B = get_random_account(A)
    
    more_follower = higher_one(A, B)

    print(f"Compare A: {format_data(A)}")

    print(vs)

    print(f"Against B: {format_data(B)}")

    guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

    if guess == more_follower:
      clear()
      print(logo)
      print("Good! You're right.")
      A = B
      score += 1
      print(f"Your current score is {score}")
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Your final score: {score}") 
      break


game()