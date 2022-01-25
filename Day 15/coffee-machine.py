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

#TODO:





def is_resources_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():

    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f'Here is ${change} in change.')
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drinkName, orderIngredients):
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName}. Enjoy☕️")

isOn = True

while isOn:
    userResponse = input("What would you like? (espresso/latte/cappuccino): ")


    if userResponse.lower() == "off":
        isOn = False
    elif userResponse.lower() == "report":
        for key in resources:
            print(f"{key.capitalize()}: {resources[key]}")
    elif userResponse in MENU:
        drink = MENU[userResponse]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(userResponse, drink["ingredients"])
    else:
        print("Sorry. I didn't get your choice. Try again.")
