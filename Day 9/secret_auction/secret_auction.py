import os
from art import logo

clear = lambda: os.system('cls')


print(logo)
print("Welcome to the blind auction...")

bidders = {}
def blind_auction():
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  def add_bider(bider_name, bider_bid):
    bidders[name] = price
    
  add_bider(name, price)
  answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if answer == "yes":
    clear()
    blind_auction()
  else:
    highest_bid = 0
    winner = ""
    for bidder in bidders:
      bid_amount = bidders[bidder]
      if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


blind_auction()