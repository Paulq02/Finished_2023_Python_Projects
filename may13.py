import random

import os



from number_art_may13 import logo

answer=random.randint(1,100)

HARD_LEVEL=5
EASY_LEVEL=10

def clear():
    os.system('clear')

def difficulty():
    question=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if question=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(guess_input,answer_input,turns_input):
    if guess_input>answer_input:
        clear()
        print("too high \nguess again")
        return turns_input -1
    elif guess_input<answer_input:
        clear()
        print("too low \nguess again")
        return turns_input -1
    elif guess_input==answer_input:
        clear()
        print(f"You got it! The answer was {answer_input}")


def play_game():
    print(logo)


    print("Welcome to the number guessing game!")


    print("I'm thinking of a number bewteen 1 and 100. Lets see if you can guess it ")

    print(f"the answer is {answer} ")

    turns=difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaning to guess the answer")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess_input=guess,answer_input=answer,turns_input=turns)

        if turns==0:
            print("You've run out of guesses")
            return
        

    
    
play_game()
