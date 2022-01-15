from Hangman_arts import stages
from Hangman_words import word_list
import random

def hangman(chosen_word):

    display = []
    for i in chosen_word:
        display += "_"

    tries = 6

    endofgame = False

    while not endofgame:
        guessed_letter = input("Guess the letter:").lower()

        for i in range(len(chosen_word)):
            if guessed_letter == chosen_word[i]:
                display[i] = chosen_word[i]
                print("Right") 


        if guessed_letter not in chosen_word:
            tries -= 1
            print(stages[tries])
            print(f"Wrong. You have {tries} tries left.")
            if tries == 0:
                print("You Lose!")
                break
        
        print(" ".join((display)))

        if "_" not in display:
            print("You have found all letters. You won!!!")
            endofgame = True

random_word = random.choice(word_list)

hangman(random_word)
    
    

