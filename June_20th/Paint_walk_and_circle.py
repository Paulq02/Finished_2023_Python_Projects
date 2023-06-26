from turtle import Screen
from turtle import Turtle
import random

from random import choice
from random import randint
timmy=Turtle()

from turtle import colormode
timmy.speed(0)
colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors

#def shape(num_sides):
#    for _ in range(num_sides):
#        angle=360/num_sides
#        timmy.forward(100)
#        timmy.right(angle)

#for number_of_sides in range(3,11):
#    shape(number_of_sides)
#    timmy.color(random.choice(colors))

#timmy.width(10)
#directions=[0, 90, 180, 270]
#for _ in range(300):
#    timmy.color(random_color())
#    timmy.forward(30)
#    timmy.setheading(random.choice(directions))

def draw_circle(size_gap):
    for _ in range(int(360/size_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_position=timmy.heading()
        timmy.setheading(current_position + size_gap)

draw_circle(30)































screen=Screen()
screen.exitonclick()



