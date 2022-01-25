from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

isOn = True
while isOn:

    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("Have a nice day!")
        isOn = False
    elif choice == "report":
        coffee_maker.report()
    elif choice == "profit":
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)






