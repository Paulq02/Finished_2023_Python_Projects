import random
from April_29th_Hangman_list import word_list
from April_29th_Hangman_art import logo
from April_29th_Hangman_art import stages
import os
from NEW_hangman_list import ufc_fighters

def clear():
    os.system('clear')

print(logo)
print()
print()

print("Guess the name of this UFC Fighter")

print()
print()
print()
print()







chosen_word=random.choice(ufc_fighters)

game_over=False

lives=6

length_chosen_word=len(chosen_word)
answer=[]
for _ in chosen_word:
    if _.isalnum():
        answer+="_"
    else:
        answer+=" "
print(" ".join(answer))
print()
print()
print()
print(chosen_word)








   

while game_over==False:
    guess=input("Guess a letter: ").upper()

    if guess in answer:
        clear()
        print(f"You've already guessed {guess}")

    for index_position in range(length_chosen_word):
        letter=chosen_word[index_position]
        
        if guess==letter:
            clear()
            print(f"Awesome! \'{guess}\' is in the word, Keep going! ")
            answer[index_position]=letter

    if guess not in chosen_word:
        clear()

        lives-=1
        print(f"Sorry {guess} is not in the word, you lose a life. You have {lives} lives left")

    print(" ".join(answer))


    
    if "_" not in answer:
        game_over=True
        print("😀 😀 😀 😀 AWESOME!!!! YOU WIN!!! 😀 😀 😀 😀 😀 ")

    if lives==0:
        game_over=True
        print(f"🤬🤬🤬🤬🤬 Sorry you ran out of lives you lose, the word was: {chosen_word}")
    

    print(stages[lives])