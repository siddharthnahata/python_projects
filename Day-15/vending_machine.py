MENU = {
    "espresso": {
        "cost": 1.5,
        "ingredients": {
            "coffee": 18,   # grams
            "water": 50     # milliliters
        }
    },
    "latte": {
        "cost": 2.5,
        "ingredients": {
            "coffee": 24,   # grams
            "water": 200,
            "milk": 150
        }
    },
    "cappuccino": {
        "cost": 1.5,
        "ingredients": {
            "coffee": 24,   # grams
            "water": 250,   # milliliters
            "milk": 180     # milliliters
        }
    }
}


resources = {
    "coffee": 100,
    "water": 500,
    "milk": 550
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        return True
    
def process_coins():
    print("Please insert coins.")
    try:
        total = int(input("How many quarters? ")) * 0.25
        total += int(input("How many dimes? ")) * 0.10
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many pennies? ")) * 0.01
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0
    return total


is_on = True
profit = 0.0

while is_on:
    choice = input("What Would you like to have? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
        print("Turning off the machine.")
        continue
    if choice == "report":
        print(f"Profit: ${profit:.2f}")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    else:
        drink = MENU.get(choice)
        if drink is None:
            print("Sorry, that item is not available.")
            continue    
        if is_resource_sufficient(drink["ingredients"]):
            amount_received = process_coins()
            if amount_received >= drink["cost"]:
                change = round(amount_received - drink["cost"], 2)
                print(f"Here is ${change:.2f} in change.")
                profit += drink["cost"]
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                print(f"Here is your {choice}. Enjoy!")            
            else:
                print("Sorry, that's not enough money. Money refunded.")
        