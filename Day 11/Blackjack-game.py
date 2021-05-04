import os
from art import logo
import random

def clear():
    os.system('cls') #Clears the previous output

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


 
#!!Should update the convert the 11 into 1 when user score over than 21

def playgame():
  user_cards = [random.choice(cards), random.choice(cards)]
  comp_cards = [random.choice(cards), random.choice(cards)]
  while True:
    sum_uscore =sum(user_cards)
    
    print(f"Your cards: {user_cards}, current score: {sum_uscore}")
    print(f"Computer's first card: {comp_cards[0]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
      user_cards.append(random.choice(cards))
      sum_uscore = sum(user_cards)
      if sum_uscore > 21:
        break
    else:
      break
  while True:
    sum_compscore= sum(comp_cards)
    if sum_compscore < 17:
      comp_cards.append(random.choice(cards))
    else: 
      break
  print(f"Your final hand: {user_cards}, your final score: {sum_uscore}")
  print(f"Computer's final hand: {comp_cards}, final hand: {sum_compscore}")
  if sum_uscore > 21:
    print("You went over! You lose 😭")
  elif sum_uscore == 21 and len(user_cards) == 2 and sum_compscore == 21 and len(comp_cards) == 2:
      return "Draw 🙃"
  elif sum_uscore == 21 and len(user_cards) == 2: 
    return "You win with a Blackjack! 😎"
  elif sum_compscore == 21 and len(comp_cards) == 2:
    return "Computer has a Blackjack! You lose 😱"

  elif sum_uscore <=21 and sum_compscore > 21:
    print("Computer went over. You Win 😁")
  elif sum_uscore <=21 and sum_uscore > sum_compscore:
    print("You win 😃")
  elif sum_uscore <=21 and sum_uscore == sum_compscore:
    print("Draw 🙃")
  else :
    print("You lose 😤")
  
  
  



while True:
  blackjack_game = input("Do you want to play Blackjack game? Type 'y' or 'n': ")
  if blackjack_game == 'y':
    clear()
    print(logo)
    playgame()
  else: 
    break


