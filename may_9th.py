from calculator_art_2 import logo

import os

def clear():
    os.system('clear')

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(logo)

    first_number=float(input("What's the first number?: "))

    for pick in operations:
        print(pick)


    calculation_done=False

    while calculation_done==False:
        make_pick=input("Pick an operation: ")

        function_called=operations[make_pick]

        second_number=float(input("What's the second number?: "))


        answer=function_called(first_number,second_number)

        print(f"{first_number} {make_pick} {second_number} = {answer}")


        restart=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if restart=="y":
            first_number=answer
            clear()
        else:
            calculation_done=True
            clear()
            calculator()


calculator()






