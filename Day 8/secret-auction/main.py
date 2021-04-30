import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

def clear():
    os.system('cls') #Clears the previous output

print(logo)

print("Welcome to the blind auction program!\nBefore starting make sure you know how it works.")

bids_list = {}

while True:
  name = input("What is your name: ")
  bid = int(input("What is your bid: $"))
  bids_list[name] = bid
  do_continue = input("Is there anybody else to bid? Type 'yes' or 'no': ")
  if do_continue == 'no':
    break
  elif do_continue == "yes":
    clear()
    

max_bid = 0
for i in bids_list:
  
  if bids_list[i] > max_bid:
    max_bid = bids_list[i]
    max_bidder = i

print(f"The winner is {max_bidder} with a bid of ${max_bid} ")








