from turtle import Turtle
from turtle import exitonclick
from turtle import Screen
import turtle_class


from random import choice
import random



#Created screen to interact with
screen=Screen()

#Created my first turtle object
timmy = Turtle()


#Changed the shape of the object to a turtle
timmy.shape("turtle")

#Changed the screen to a smaller one
screen.setup(width=500,height=400)

#Prompt the user to make a bet on which color turtle will win
user_guess = screen.textinput(title="make a bet",prompt="Who will win? Choose a color: ")

#Move turtle to a specific area of the screen 
timmy.penup()
timmy.goto(x=-240,y=0)





















screen.exitonclick()

