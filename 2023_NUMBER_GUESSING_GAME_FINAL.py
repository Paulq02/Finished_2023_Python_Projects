import random

import os



from number_art_may13 import logo
"""
random number is generated from the random module ans assigned to a variable called answer"""
answer=random.randint(1,100)
"""
set a constant of 10 tries for easy mode and 5 tries for hard"""
HARD_LEVEL=5
EASY_LEVEL=10

def clear():
    """clears screen for better user experience"""
    os.system('clear')

def difficulty():
    """prompts the user for input asking what level they want,
    returns 10 for easy mode and 5 for hard mode"""
    question=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if question=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(guess_input,answer_input,turns_input):
    """
    checks if your guess is equal to the randomly generated answer,
    keeps track of how many attempts you have left by subtracting 1,
    also clears screen after every guess
    if you are incorrect"""
    if guess_input>answer_input:
        clear()
        print(("too high \nguess again 🤬🤬🤬".upper()))
        return turns_input -1
    elif guess_input<answer_input:
        clear()
        print(("too low \nguess again 🤬🤬🤬"))
        return turns_input -1
    elif guess_input==answer_input:
        clear()
        print((f"You got it! 😃😃😃 The answer was {answer_input} YOU WIN!!! 🎉🎉🎉🎉").upper())


def play_game():
    print(logo)


    print(("Welcome to the number guessing game!").upper())


    print("I'm thinking of a number bewteen 1 and 100. Lets see if you can guess it 😃😃 ")

    #print(f"the answer is {answer} ")

    turns=difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaning to guess the answer")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess_input=guess,answer_input=answer,turns_input=turns)

        if turns==0:
            print("You've run out of guesses 🤬🤬🤬")
            return
        

    
    
play_game()
