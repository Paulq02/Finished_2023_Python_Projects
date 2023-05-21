from coffee_machine_data import MENU

from coffee_machine_data import resources

def check_resources(water,milk,coffee):
    if water<MENU[order]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return 0
    if milk<MENU[order]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
        return 0
    if coffee<MENU[order]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        return 0
    
        




machine_on=True

while machine_on==True:
    order=input("What would you like? (espresso/latte/cappuccino): ")

#for drink in MENU:
#    if drink==order:
#        print(MENU[order]["ingredients"]["water"])


    if order=="off":
        machine_on=False
    if order=="report":
        print("Water:",resources.get("water"),"ml")
        print("Milk:",resources.get("milk"),"ml")
        print("Coffee:",resources.get("coffee"),"ml")
    if order=="espresso":
        message=check_resources(water=resources["water"],milk=resources["milk"],coffee=resources["coffee"])
        if not message== 0:
            print(f"Enjoy your {order}")
        
    if order=="latte":
        message=check_resources(water=resources["water"],milk=resources["milk"],coffee=resources["coffee"])
        if not message== 0:
            print(f"Enjoy your {order}")
    if order=="cappuccino":
        message=check_resources(water=resources["water"],milk=resources["milk"],coffee=resources["coffee"])
        if not message== 0:
            print(f"Enjoy your {order}")


        





    
    