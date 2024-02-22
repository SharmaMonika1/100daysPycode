# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Global Variables are denoted by capital letters
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

resources = {"water": 300,
             "milk": 200,
             "coffee": 100,
             }


def resource_enough(choice, source):
    is_enough = True
    for item in choice:
        if source[item] < choice[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


def calculate_money(choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    print(f"You gave ${amount}.")
    if amount < choice["cost"]:
        return 0
    else:
        return amount


def make_coffee(choice, amount):
    for item in choice["ingredients"]:
        resources[item] -= choice["ingredients"][item]
    change = round(amount - choice["cost"], 2)
    print(f"Here is {change} in change.")
    print("Here is your latte ☕️.Enjoy!")
    return choice["cost"]


machine_on = True
money = 0
while machine_on:
    user_choice = input("What would you like?(espresso/latte/cappuccino):")
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money}")
    elif user_choice in ("espresso", "latte", "cappuccino"):
        drink = MENU[user_choice]
        check_value = resource_enough(drink["ingredients"], resources)
        if check_value:
            user_amount = calculate_money(MENU[user_choice])
            if user_amount == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += make_coffee(MENU[user_choice], user_amount)
    else:
        print("Wrong Input.")
