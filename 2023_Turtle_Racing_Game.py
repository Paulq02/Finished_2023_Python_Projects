from turtle import Turtle
from turtle import exitonclick
from turtle import Screen
import turtle_class


from random import choice
import random
#Here we made a list of colors that will be assigned to the 6 objects we create from the for loop below
colors=["red", "orange", "yellow", "green", "blue", "purple"]

#The same goes for a y corridinate position, each turtle will be assigned a diffent position to line up on the y axis
position=[-60, -40, -20, 0, 20, 40]

#after each turtle is created, they will each be appended to this empty list which will be continuously interated through with a for loop, which will be controlled by a while loop
turtles=[]

#gives us a screen to interact with
screen=Screen()

#shrank screen size
screen.setup(width=500,height=400)

#textinput is a a method that allows a prompt to be displayed for the user to enter a string, it acts as the users guess of which turtle you think will win
user_guess = screen.textinput(title="make a bet",prompt="Who will win? Choose a color: ").lower()


#here we have a for loop that assigns a color and a postion to each seperate turtle instance and each instance is appended to an empty list
for turtle_attribute in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_attribute])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=position[turtle_attribute])
    turtles.append(new_turtle)
    
#if the prompt asking you who will win is filled in then the game condition is set to true , which starts the while loop
if user_guess:
    race_on=True

#while loop starts and the for loop begins, each turtle is assigned a step disatance ranging from 0 to 10

#whoever crosses the 230 x axis is the winner and the while loop stops

#if your input (user_guess) which is a color is the same as the turtle color that won you are prompted you are correct
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on=False
            winner = turtle.fillcolor()
            if user_guess == winner:
                print("Correct!!")
            else:
                print(f"Winner was the {winner} turtle, You guessed wrong")
                     
        #having the random number here ensures for each turtle a new random number is assigned for the step forward
        #before you had it on top of the page
        step=random.randint(0,10)
        turtle.forward(step)
            


































screen.exitonclick()

