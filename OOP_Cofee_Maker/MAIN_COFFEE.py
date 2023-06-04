from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#We created 3 objects from the Classes written in the documentation provided
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


#Our boolean condition to keep the program running 
machine_on=True


while machine_on:
    #In the documentation the get_items() Method  Returns all available options from the menu
    
    #So we assigned a variable called "options" to store/hold the return value of what is available on the menu
     
    options=menu.get_items()

    #After assigning the "options" variable to store the menu items we use this return value/variable inside an f string to display to the user as well as ask for input 

    #The user is prompted for input for what drink they'd like to order form the options displayed

    order=input(f"What would you like to order? {options}?: ")
    
    #If you want to turn the coffee machine off simply enter "off" and the while loop ends
    if order=="off":
        machine_on=False
    #To get a report on the available resources type "report" and a print out will be displayed of the milk,water,coffee levels along with how much money has been collected
    elif order=="report":
        #remember these 2 report methods already have print statements built in so theres no need to use print function 
        coffee_maker.report()
        money_machine.report()
    else:
        #In the documentation the Menu class has a method called find_drink which takes input and searches within the menu for what the user input
        
        #It also returns a menu item object if the drink youve entered exists within the menu, if it doesnt it returns none
        
        #We assigned a variable to store the return value called "orderd_drink" 

        orderd_drink=menu.find_drink(order)

        #If the drink you've entered as input exists on the menu we then check to see if there are enough resources to make the drink

        #The is_resource_sufficient method takes input in the form of the menu item that exists that we ordered via input

        #If there is enough resources we then move onto payment, The make_payment method takes input in the form of what exists on the menu (continued below)
        #from what we've input along with the cost attribute in relation to the price of that drink

        #The make_payment method then prompts the user for input in the form of a float to represent coins

        #If we have enough resources to make the drink and we also cover the cost of the drink then the make_coffee method is called making the drink and completing the transaction


        if coffee_maker.is_resource_sufficient(orderd_drink) and money_machine.make_payment(orderd_drink.cost)==True:
            coffee_maker.make_coffee(orderd_drink)



        

        


        




                


           
        
        
        









    



            
        
        





