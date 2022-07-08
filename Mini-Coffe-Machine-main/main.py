MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}

def prompt_user():
    print("Welcome to the coffee machine!")
    print("What would you like? (espresso/latte/cappuccino)")
    user_input = input()
    if user_input == "espresso":
        return "espresso"
    elif user_input == "latte":
        return "latte"
    elif user_input == "cappuccino":
        return "cappuccino"
    elif user_input == "off":
        return False
    elif user_input == "report":
        report()
        return False
    else:
        print("Invalid input")
        prompt_user()

def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))

def check_resources_sufficient(drink):
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            print("Sorry, not enough " + ingredient + ".")
            return False
    return True

def coins(res_stat):
    if res_stats == True:
        print("Insert Coins.")
        print("How many quarters: ")
        quarters = int(input())
        print("How many dimes: ")
        dimes = int(input())
        print("How many nickles: ")
        nickles = int(input())
        print("How many pennies: ")
        pennies = int(input())
        total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
        return round(total, 2)

def txn_successful(total, drink):
    if total < drink["cost"]:
        print("Sorry, not enough money. Money refunded.")
        return False
    else:
        resources["money"] += drink["cost"]
        change = total - drink["cost"]
        return round(change,2)

def coffee_machine(drink):
    if check_resources_sufficient(drink):
        resources["water"] -= drink["ingredients"]["water"]
        resources["milk"] -= drink["ingredients"]["milk"]
        resources["coffee"] -= drink["ingredients"]["coffee"]
    else:
        print("Sorry, not enough resources.")


state = True
while state:
    drink = prompt_user()
    if drink == False:
        state = False
    else:
        res_stats = check_resources_sufficient(MENU[drink])
        total = coins(res_stats)
        change = txn_successful(total, MENU[drink])
        print(f"Here is your {str(drink)}. Enjoy!")
        if change:
            coffee_machine(MENU[drink])
            print("Change: $" + str(change))
            print("Your change is $" + str(change))

