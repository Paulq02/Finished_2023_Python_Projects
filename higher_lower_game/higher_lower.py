import random
from higher_lower_data import data
from higher_lower_art import logo
from higher_lower_art import vs
import os


def clear():
    """
    clears the screen after every guess for better user experience
    """
    os.system('clear')




def person_1(input_a):
    """
    Takes the randomly generated choice (person_a) as input and accesses the values (name,description,country)
    prints those values 
    
    """
    
    person_a_name=person_a["name"]
    person_a_description=person_a["description"]
    person_a_country=person_a["country"]
    print(f"Compare A: {person_a_name}, a {person_a_description}, from {person_a_country}")


def person_2(input_b):
    """
    Takes the randomly generated choice (person_b) as input and accesses the values (name,description,country)
    prints those values 
    
    """
    
    person_b_name=person_b["name"]
    person_b_description=person_b["description"]
    person_b_country=person_b["country"]
    print(f"Compare B: {person_b_name}, a {person_b_description}, from {person_b_country}")



def compare(person_a_followers_input,person_b_followers_input):
    """
    Takes each of the randomly generated picks follower count and compares who has the larger follower count,
     returns 'a' if randomly generated choice was 'person_a'
    returns 'b' if randomly generated choice was 'person_b'
    """
    if person_a_followers_input>person_b_followers_input:
        return "a"
    elif person_b_followers_input>person_a_followers_input:
        return "b"


#Two randomly generated choices
person_a=random.choice(data)
person_b=random.choice(data)

#I've made a 'filter' to make sure choices aren't the same, checks multiples time 
if person_a==person_b:
        person_b=random.choice(data)
if person_a==person_b:
        person_b=random.choice(data)
if person_a==person_b:
        person_b=random.choice(data)
if person_a==person_b:
        person_b=random.choice(data)


#guesses tracker
correct_guesses=0

#The follower count 'values' of the 2 randomly generated choices
person_a_followers=person_a["follower_count"]
person_b_followers=person_b["follower_count"]


game_over=False
while game_over==False:
    #prints logo
    print(logo)

    
    
    #Function 'person_1' is called, with the randomly generated choice 'person_a' inserted as input
    person_1(person_a)
    
    #below code is for testing purposes
    #print(person_a_followers)
    
    
    #2nd logo is printed to seperate the choices
    print(vs)
    
    
    #Function 'person_2' is called, with the randomly generated choice 'person_b' inserted as input
    person_2(person_b)
    
    #below code is for testing purposes
    #print(person_b_followers)
    
    #User is asked for 'a' or 'b' input to make guess
    question=input("Who has more followers? Type 'A' or 'B': ").lower()

    
    #The output of the compare function (who has more followers) is assigned to the variable 'winner', output will either be 'a' or 'b'
    winner=compare(person_a_followers_input=person_a_followers,person_b_followers_input=person_b_followers)

    
    #Users guess ('a' or 'b') is compared to the winner- if you guess correctly the screen clears ,1 point is added to your score, and you're updated with your current score
    if question==winner:
        clear()
        correct_guesses+=1
        print(f"You're right!! Curent score: {correct_guesses}")




        #After a correct guess person_a now becomes person_b and a new person_b is randomly generated to compare
        person_a=person_b
        
        
        
        #This is another 'filter' to check if the new randomly generated 'person_b' choice is the same as 'person_a'- if it is the same, generate another random 'person_b' choice -repeat
        if person_a==person_b:
            person_b=random.choice(data)
        if person_a==person_b:
            person_b=random.choice(data)
        if person_a==person_b:
            person_b=random.choice(data)
        if person_a==person_b:
            person_b=random.choice(data)
        
        
    #If you guess incorrectly, the game ends and you are shown your score 
    else:
        game_over=True
        print(f"Sorry that was wrong, Final score: {correct_guesses}")



    

