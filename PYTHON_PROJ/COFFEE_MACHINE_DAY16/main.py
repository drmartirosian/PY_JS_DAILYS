from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()     
money_machine = MoneyMachine()
menu = Menu()
is_on = True

# 1. print report - CHECK
# 2. Check resources sufficient - CHECK
# 3. process coins - CHECK
# 4. check transaction successful - CHECK
# 5. make coffee - CHECK


while is_on == True:
    #Print options
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    #switch machine off
    if choice == 'off':
        is_on = False
    #Report resources and money status of machine
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        #checks if drink optin you selected above exists, drink = order
        drink = menu.find_drink(choice)
        print(drink)
        #if enough resources and payment enough...
        if coffee_maker.is_resource_sufficient(drink) == True and money_machine.make_payment(drink.cost) == True:
                #make the coffee (order = drink)
                coffee_maker.make_coffee(drink)





