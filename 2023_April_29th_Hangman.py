#Imported the random module to randomly choose a name from the UFC names list
import random
#imported the logo for when you start the game as well as the ASCII art to know how close you are to being hung
from April_29th_Hangman_art import logo
from April_29th_Hangman_art import stages
import os
from NEW_hangman_list import ufc_fighters

def clear():
    """
    clears the screen for a better user experience
    """
    os.system('clear')
#Logo is printed as well as a couple empty print statements to space things out
print(logo)
print()
print()


print("Guess the name of this UFC Fighter")

print()
print()
print()
print()






#The random module randomly selects a name from the ufc fighters list and is assigned to a variable called chosen_word
chosen_word=random.choice(ufc_fighters)

#Set condition to stop while loop
game_over=False

#We have 6 guesses/lives to guess the name
lives=6

#We use a for loop to print the underscores for as many letters in the chosen word, so we used the len function to get an accurate number of characters
length_chosen_word=len(chosen_word)

#We are using a list as our container
answer=[]

#Here we use a for loop to iterate through each character of the randomly chosen word
for _ in chosen_word:
    
    #This if statement checks if any character is a letter or number to instead add an underscore instead of the letter or number to the empty list "answer" 
    if _.isalnum():
        answer+="_"
    
    #If a character or letter in the chosen word isn't a letter or number it must be whitespace, so this else statement adds a space to "answer"
    else:
        answer+=" "

#After all letters have been replaced by underscores we used the .join() function to print the list as a string to the user
print(" ".join(answer))
print()
print()
print()
#This print statement is for testing your code if you need it
print(chosen_word)








   
#Here we start the while loop 
while game_over==False:
    
    #The user is asked for input to guess a letter, it's converted to uppercase 
    guess=input("Guess a letter: ").upper()

    #This checks if you already guessed a letter, you are prompted that you've already guessed the letter
    if guess in answer:
        clear()
        print(f"You've already guessed {guess}")

    #This for loop geta a hold of the index postion of each character in the answer list
    #By using the range function along with the legnth of the chosen word we can accurately achieve this since
    #Since index postions start with 0 along with the range function
    for index_position in range(length_chosen_word):
        
        #After grabbing hold of each character and it's index postion,we assign the variable "letter" to each characters index postion per iteration
        #Example: if the word was "cat" chosen_word[0] would be "c", then chosen_word[1] would be "a" and so on
        letter=chosen_word[index_position]
        
        #This checks to see if the letter you guessed if equal to a letter in the chosen word
        #If it is you get prompted you are correct and the index postion of the letter within the answer list if filled in with the letter you correctly guessed
        if guess==letter:
            clear()
            print(f"Awesome! \'{guess}\' is in the word, Keep going! ")
            answer[index_position]=letter
    
    #If the letter you guessed is incorrect the variable "lives" is deducted by 1 and you are prompted that your guess was incorrect
    #You then are updated on how many lives you have left
    if guess not in chosen_word:
        clear()

        lives-=1
        print(f"Sorry {guess} is not in the word, you lose a life. You have {lives} lives left")

    print(" ".join(answer))

    
    
    #If there are no more underscores in the "answer" list and you haven't used up your lives, You have successfully guessed all the letters
    #After successfully guessing all the letters the while loop ends and you're prompted that you win
    if "_" not in answer:
        game_over=True
        print("😀 😀 😀 😀 AWESOME!!!! YOU WIN!!! 😀 😀 😀 😀 😀 ")

    #If you have no more lives left, the while loop stops and you are prompted that you have lost
    if lives==0:
        game_over=True
        print(f"🤬🤬🤬🤬🤬 Sorry you ran out of lives you lose, the word was: {chosen_word}")
    
    #This prints our the ASCII art of your stick figure in relation to how many lives you have left and how close you are to being hung
    print(stages[lives])