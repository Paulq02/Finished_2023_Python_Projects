from calculator_art_2 import logo

import os

def clear():
    #clears the screen after every calculation
    
    os.system('clear')

def add(num1,num2):
    
    #returns the value of 2 numbers being added
    return num1+num2

def subtract(num1,num2):
    
    #returns the value of 2 numbers being subtracted
    return num1-num2

def multiply(num1,num2):
    
    #returns the value of 2 numbers being multiplied
    return num1*num2

def divide(num1,num2):
    #returns the value of 2 numbers being divided
    return num1/num2


#The values in this dictionary are the functions we created earlier, we don't add the parentheses because we aren't adding any inout yet


operations={
    
   "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
#By wrapping this program in a function, rather than a while loop it gives the user more options, if they want to start a fresh calculation they can just re-call this function"""
    print(logo)

    first_number=float(input("What's the first number?: "))



    calculation_done=False
    
    #Here is a for loop to iterate through the dictionary and print out each key
    
    while calculation_done==False:
        for pick in operations:
            
            print(pick)


    
        
        #Here we created a while loop as the 2nd option if the user wants to continue a calculation using a previous answer. If they select this option the program restarts here.
        
        make_pick=input("Pick an operation from the options above: ")
        
        
        #After having the dictionary keys printed for the user to see, they then can make a choice of the operation theyd like to use
        

        function_called=operations[make_pick]
        
        #This line of code accesses the operations dictionary by using your input to access one of the functions, the function selected is assigned to a variable called 'function_called'
        

        second_number=float(input("What's the second number?: "))


        answer=function_called(first_number,second_number)
        #After selelcting an operation, from the dictionary the variable 'functioned_called' now acts as a function itself holding the exact same functionality as the ones we created earlier

        print(f"{first_number} {make_pick} {second_number} = {answer}")
        
        #Here a f string print out of the full calculation

        restart=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if restart=="y":
            """Gives the user an option to restart a calculation using the previous calculations answer, by assigning the value of your answer to the 'first_number' that is asked at the beginning of the program
              and restarting the program at the beginning of the while loop  """
            first_number=answer
            clear()
        else:
            #If the user wants a fresh calculation the while loop stops and the 'calculator' function is called, starting a brand new program/calculation
            calculation_done=True
            clear()
            calculator()


calculator()






