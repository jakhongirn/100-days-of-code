import random
from art import logo

def guess_the_number():
  key_number = random.randint(1, 100)
  print(key_number)
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  attempts = 0
  if level == 'hard':
    attempts = 5
  elif level == 'easy':
    attempts = 10
  else:
    print("You haven't chose the difficulty. Try again.")
    return
  
  while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess == key_number:
      print(f"You got it. The answer was {key_number}.")
      return
    elif guess > key_number:
      print("Too high.")
      attempts -= 1
    else:
      print("Too low.")
      attempts -= 1
  print("Yo've run out of guesses. You lose.")

print(logo)
print("Welcome to the Number Guessing game.\nI'm thinking a number between 1 and 100.")


guess_the_number()