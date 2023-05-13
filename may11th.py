from number_guess_art import logo
import random

EASY_LEVEL=10
HARD_LEVEL=5


def difficulty(level_selected):
    if level_selected=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(guess_input,answer_input,turns_input):
    if guess_input<answer_input:
        print("too low")
        return turns_input -1 
    elif guess_input>answer_input:
        print("too high")
        return turns_input - 1
    elif guess_input==answer_input:
        return "Correct!!😀😀"
    









print(logo)

answer=random.randint(1,100)

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100, let's see if you can guess it 😀😀")

print(f"Psst the correct answer is {answer}")

level=input("Choose a difficulty. Type 'easy' or 'hard': ")

turns=difficulty(level)



game_over=False

while not game_over:
    
    print(f"You have {turns} attempts to guess the answer")

    guess=int(input("Make a guess: "))
    
    
    turns=check_answer(guess_input=guess,answer_input=answer,turns_input=turns)

    
    
    
    if guess==answer:
        game_over=True
       
    if turns==0:
        game_over=True
        print("🤬🤬 You've run out of lives, you lose 🤬🤬")







