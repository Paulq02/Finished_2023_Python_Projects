#from turtle import Turtle, Screen

#paul=Turtle()
#print(paul)
#paul.shape("turtle")
#paul.color("red","green")
#paul.fd(100)

#paul_screen=Screen()
#print(paul_screen.canvheight)
#paul_screen.exitonclick()

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Charmander","Squirtle"])
table.add_column("Type",["Electric","Fire","Water"])
table.align="l"
print(table)

