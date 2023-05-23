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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources['money']=0


def latte_drink(water,milk,coffee):
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
    if water<50:
        print("Sorry there isn't enough water")
        return 0
    elif coffee<18:
        print("Sorry there isn't enough coffee")
        return 0


def cappuccino_drink(water,milk,coffee):
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
    money_inserted=quarters_input*0.25+dimes_input*0.10+nickels_input*0.05+pennies_input*0.01
    return float(money_inserted)






machine_on=True

while machine_on==True:
    order=input("What would you like? (espresso/latte/cappuccino): ")



    if order=="off":
        machine_on=False
    if order=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk:  {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    
    
    if order=="latte":
        message=latte_drink(water=resources["water"],milk=resources["milk"],coffee=resources["coffee"])
        if not message== 0:
            quarters=float(input("how many quarters?: "))
            dimes=float(input("how many dimes?: "))
            nickles=float(input("how many nickels?: "))
            pennies=float(input("how many pennies?: "))
            total=calculate(quarters_input=quarters,dimes_input=dimes,nickels_input=nickles,pennies_input=pennies)
            if total>=2.50:
                resources['water']-=200
                resources["milk"]-=150
                resources["coffee"]-=24
                resources["money"]+=total
                
                print(f"Enjoy your {order}")
        
    if order=="espresso":
        message=espresso_drink(water=resources["water"],coffee=resources["coffee"])
        if not message== 0:
            quarters=float(input("how many quarters?: "))
            dimes=float(input("how many dimes?: "))
            nickles=float(input("how many nickels?: "))
            pennies=float(input("how many pennies?: "))
            total=calculate(quarters_input=quarters,dimes_input=dimes,nickels_input=nickles,pennies_input=pennies)
            if total>=1.50:
                resources['water']-=50
                resources["coffee"]-=18
                resources["money"]+=total
            
                print(f"Enjoy your {order}")
    if order=="cappuccino":
        message=cappuccino_drink(water=resources["water"],milk=resources["milk"],coffee=resources["coffee"])
        if not message== 0:
            quarters=float(input("how many quarters?: "))
            dimes=float(input("how many dimes?: "))
            nickles=float(input("how many nickels?: "))
            pennies=float(input("how many pennies?: "))
            total=calculate(quarters_input=quarters,dimes_input=dimes,nickels_input=nickles,pennies_input=pennies)
            if total>=3.00:
                resources['water']-=250
                resources["milk"]-=100
                resources["coffee"]-=24
                resources["money"]+=3.0
                print(f"Enjoy your {order}")


        





    
    