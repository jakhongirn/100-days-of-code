import os
from art import logo
import random

def clear():
    os.system('cls') #Clears the previous output



def deal_card():
  card_decks = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(card_decks)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare_scores(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  


def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}\nTotal score: {user_score}.\n")
    print(f"Computer's first card: {computer_cards[0]}\n")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      get_another_card = input("Do you want to get another card? Type 'y' or 'n': ")
      if get_another_card == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
      else:
        is_game_over =True

  while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}\nFinal score: {user_score}\n")
  print(f"Computer's final hand: {computer_cards}\nFinal score:{computer_score}\n")

  print(compare_scores(user_score, computer_score))

while input("Do you want to play Blackjack? Type 'y' or 'n':\n") == 'y':
  clear()
  play_game()


      



