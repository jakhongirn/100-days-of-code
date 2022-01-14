import random

user_choice = int(input("What do you chosse? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n "))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]

computer_choice = random.randint(0, 2)


print(f"Your choice: {rps[user_choice]}")
print(f"Computer's choice: {rps[computer_choice]}")

if user_choice == computer_choice:
    print("Draw.")

elif user_choice == 0:
    if computer_choice == 1:
        print("You lose! Oh no!")
    else:
        print("Yay! You win!")

elif user_choice == 1:
    if computer_choice == 2:
        print("You lose! Oh no!")
    else:
        print("Yay! You win!")

elif user_choice == 2:
    if computer_choice == 0:
        print("You lose! Oh no!")
    else:
        print("Yay! You win!")

else:
    print("Hmm. Yo've typed invalid number. You lose.")