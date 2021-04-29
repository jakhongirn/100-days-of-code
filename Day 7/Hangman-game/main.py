import random
from hangman_arts import *
from hangman_words import *

# let me give some info about the game. It's like guessword game you should guess the word by letters and when you guess wrong letter you lose a life. When you guess all the letters you win otherwise you'll hang on gallows;))

print(logo)
print("\nWelcome to the Hangman! \nBefore you start the game make sure you know how to play it. (https://www.considerable.com/entertainment/games/hangman/)")
print("You have overall 6 lives.\nLesh goo!\n")

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)


display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display +='_'


lives = 6

end_of_game = False

while not end_of_game: 
  guess = input("Guess the letter: ").lower()

  if guess in display:
    print("You've already guessed this letter.")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
    
    
 

  if guess not in chosen_word:
    lives-=1
    print(f"You've  guessed {guess}, that's not in the word. You lose a life.")
    print(stages[lives])
    if lives ==0:
      print(f"You lose! \n{game_over}")
      break

  print(f"{' '.join(display)}\n")

  if '_' not in display:
    end_of_game=True
    print(you_win)
