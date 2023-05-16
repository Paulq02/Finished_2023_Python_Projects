import random
from higher_lower_data import data
from higher_lower_art import logo
from higher_lower_art import vs
import os


def clear():
    os.system('clear')




def person_1(input_a):
    
    person_a_name=person_a["name"]
    person_a_description=person_a["description"]
    person_a_country=person_a["country"]
    print(f"Compare A: {person_a_name}, a {person_a_description}, from {person_a_country}")


def person_2(input_b):
    
    person_b_name=person_b["name"]
    person_b_description=person_b["description"]
    person_b_country=person_b["country"]
    print(f"Compare B: {person_b_name}, a {person_b_description}, from {person_b_country}")



def compare(person_a_followers_input,person_b_followers_input):
    if person_a_followers_input>person_b_followers_input:
        return "a"
    elif person_b_followers_input>person_a_followers_input:
        return "b"



person_a=random.choice(data)
person_b=random.choice(data)
if person_a==person_b:
        person_b=random.choice(data)
if person_a==person_b:
        person_b=random.choice(data)
if person_a==person_b:
        person_b=random.choice(data)
if person_a==person_b:
        person_b=random.choice(data)



correct_guesses=0


game_over=False
while game_over==False:
    print(logo)

    
    
    person_a_followers=person_a["follower_count"]
    person_1(person_a)
    print(person_a_followers)
    
    

    print(vs)
    
    
    person_b_followers=person_b["follower_count"]
    person_2(person_b)

    print(person_b_followers)
    

    question=input("Who has more followers? Type 'A' or 'B': ").lower()

    winner=compare(person_a_followers_input=person_a_followers,person_b_followers_input=person_b_followers)

    if question==winner:
        clear()
        correct_guesses+=1
        print(f"You're right!! Curent score: {correct_guesses}")

        person_a=person_b
        if person_a==person_b:
            person_b=random.choice(data)
        if person_a==person_b:
            person_b=random.choice(data)
        if person_a==person_b:
            person_b=random.choice(data)
        if person_a==person_b:
            person_b=random.choice(data)
        
        
        
    else:
        game_over=True
        print(f"Sorry that was wrong, Final score: {correct_guesses}")



    

