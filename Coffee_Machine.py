
#Here we have a constant named MENU that is a dictionary, it contains the measurments of the cofee,water and milk for every drink in the virtual machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# Here is another dictionary containing the amount of water,milk and coffee the virtual coffee machine holds at a time
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#We added the key "money" to the resources dictionary to keep track of how much money we're collecting
resources['money']=0


def latte_drink(water,milk,coffee):
    """
    checks the resources dictionary if there is enough product to make the drink selected.
    Latte needs 50ml of water,150ml of milk and 24grams of coffee.
    If there isn't enough resources user is prompted with a message, and a return value of 0 is output for a full refund to be issued


    """
    if water<50:
        print("Sorry there isn't enough water")
        return 0
    elif milk<150:
        print("Sorry there isn't enough milk")
        return 0
    elif coffee<24:
        print("Sorry there isn't enough coffee")
        return 0
    

def espresso_drink(water,coffee):
    """
    checks the resources dictionary if there is enough product to make the drink selected.
    Espresso needs 50ml of water, 18grams of coffee.
    If there isn't enough resources user is prompted with a message, and a return value of 0 is output for a full refund to be issued
    """
    if water<50:
        print("Sorry there isn't enough water")
        return 0
    elif coffee<18:
        print("Sorry there isn't enough coffee")
        return 0


def cappuccino_drink(water,milk,coffee):
    """
    checks the resources dictionary if there is enough product to make the drink selected.
    Cappuccino needs 250ml of water,100ml of milk and 24grams of coffee.
    If there isn't enough resources user is prompted with a message, and a return value of 0 is output for a full refund to be issued 
    """
    if water<250:
        print("Sorry there isn't enough water")
        return 0
    elif milk<100:
        print("Sorry there isn't enough milk")
        return 0
    elif coffee<24:
        print("Sorry there isn't enough coffee")
        return 0

def calculate(quarters_input,dimes_input,nickels_input,pennies_input):
    """
    Takes the virtual "coin" input (float) and multiplies each number by the "real life" value of each coin.
    example 5 quarters as ($0.25) would be $0.25*5=$1.25
    Then adds all values together and outputs all the money inserted
    """
    money_inserted=quarters_input*0.25+dimes_input*0.10+nickels_input*0.05+pennies_input*0.01
    return float(money_inserted)





#Since we need the program to continue to run we set our condition to true
machine_on=True
#Since we need the program to continue to run we set our condition to true
while machine_on==True:
    #Asks the user what drink they would like to order
    order=input("What would you like? (espresso/latte/cappuccino): ")


    #Allows the user to turn the virtual machine off, turns the "True" condition to "False" if user enters "off"
    if order=="off":
        machine_on=False
    #If you would like to know how much resources (water,milk,coffee) are left in the virtual coffee machine, typing "report" before ordering a drink will list whats left
    if order=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk:  {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    
    #if user orders a latte 
    if order=="latte":
        #Once the user orders a latte the "latte" function is called, it checks to see if there is enough resources to make the drink
        
        #The latte function outputs a value of 0 if there isn't enough resources. The code below will run IF 0 is NOT output (meaning there IS enough resources)
        message=latte_drink(water=resources["water"],milk=resources["milk"],coffee=resources["coffee"])
        if not message== 0:
            #user is prompted to enter coins
            print("Please insert coins.")
            #all input in this block is converted to a float to represent coins
            quarters=float(input("how many quarters?: "))
            dimes=float(input("how many dimes?: "))
            nickles=float(input("how many nickels?: "))
            pennies=float(input("how many pennies?: "))
            #After input the calculate function adds everything up and is output to a variable called total
            total=calculate(quarters_input=quarters,dimes_input=dimes,nickels_input=nickles,pennies_input=pennies)
            #If the user entered exact change the drink is made and the resources are deducted from the dictionary
            #After deduction the user is prompted with a message to enjoy their drink to complete the transaction
            if total==2.50:
                resources['water']-=200
                resources["milk"]-=150
                resources["coffee"]-=24
                resources["money"]+=total
                print(f"Enjoy your {order}")
            elif total>2.50:
                #If the user entered more than what the drink costs the drink is made and the user is refunded the remaining change 

                refund=total-2.50
                resources['water']-=200
                resources["milk"]-=150
                resources["coffee"]-=24
                resources["money"]+=total
                print(f"Here is your ${round(refund,2)} in change.")
                print(f"Enjoy your {order}")
            elif total<2.50:
                #If the user enters less than what the drink costs, the user is alerted and then issued a full refund of what they entered
                print(f"Sorry thats not enought money, You've been refunded ${round(total,2)} ")



    if order=="espresso":
        #Once the user orders a espresso the "espresso" function is called, it checks to see if there is enough resources to make the drink
        
        #The espresso function outputs a value of 0 if there isn't enough resources. The code below will run IF 0 is NOT output (meaning there IS enough resources)
        message=espresso_drink(water=resources["water"],coffee=resources["coffee"])
        if not message== 0:
            #user is prompted to enter coins
            print("Please insert coins.")
            #all input in this block is converted to a float to represent coins
            quarters=float(input("how many quarters?: "))
            dimes=float(input("how many dimes?: "))
            nickles=float(input("how many nickels?: "))
            pennies=float(input("how many pennies?: "))
            #After input the calculate function adds everything up and is output to a variable called total
            total=calculate(quarters_input=quarters,dimes_input=dimes,nickels_input=nickles,pennies_input=pennies)
            #If the user entered exact change the drink is made and the resources are deducted from the dictionary
            #After deduction the user is prompted with a message to enjoy their drink to complete the transaction
            if total==1.50:
                resources['water']-=50
                resources["coffee"]-=18
                resources["money"]+=total
                print(f"Enjoy your {order}")
            elif total>1.50:
            #If the user entered more than what the drink costs the drink is made and the user is refunded the remaining change 
                refund=total-1.50
                resources['water']-=200
                resources["milk"]-=150
                resources["coffee"]-=24
                resources["money"]+=total
                print(f"Here is your ${round(refund,2)} in change.")
                print(f"Enjoy your {order}")
            elif total<1.50:
             #If the user enters less than what the drink costs, the user is alerted and then issued a full refund of what they entered
                print(f"Sorry that's not enough money, You've been refunded ${round(total,2)} ")


    if order=="cappuccino":
        #Once the user orders a cappuccino the "cappuccino" function is called, it checks to see if there is enough resources to make the drink
        
        #The cappuccino function outputs a value of 0 if there isn't enough resources. The code below will run IF 0 is NOT output (meaning there IS enough resources)
        message=cappuccino_drink(water=resources["water"],milk=resources["milk"],coffee=resources["coffee"])
        if not message== 0:
            #user is prompted to enter coins
            print("Please insert coins.")
            #all input in this block is converted to a float to represent coins
            quarters=float(input("how many quarters?: "))
            dimes=float(input("how many dimes?: "))
            nickles=float(input("how many nickels?: "))
            pennies=float(input("how many pennies?: "))
            #After input the calculate function adds everything up and is output to a variable called total
            total=calculate(quarters_input=quarters,dimes_input=dimes,nickels_input=nickles,pennies_input=pennies)
            #If the user entered exact change the drink is made and the resources are deducted from the dictionary
            #After deduction the user is prompted with a message to enjoy their drink to complete the transaction
            if total==3.00:
                resources['water']-=250
                resources["milk"]-=100
                resources["coffee"]-=24
                resources["money"]+=3.0
                print(f"Enjoy your {order}")
            elif total>3.00:
                #If the user entered more than what the drink costs the drink is made and the user is refunded the remaining change
                refund=total-3.00
                resources['water']-=200
                resources["milk"]-=150
                resources["coffee"]-=24
                resources["money"]+=total
                print(f"Here is your ${round(refund,2)} in change.")
                print(f"Enjoy your {order}")
            elif total<3.00:
                #If the user enters less than what the drink costs, the user is alerted and then issued a full refund of what they entered
                print(f"Sorry that's not enough money, You've been refunded ${round(total,2)}")


        





    
    