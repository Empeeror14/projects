
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1500,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2000,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3000,
    }
}
profit =0

resources = {
    "water": 300,
    "milk"  :160,
    "coffee": 76,
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item ] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """return total aamont of cash slotted in"""
    print("Please slot in your cash.")
    total = int(input("How many 100 naira notes?: ")) *100
    total+= int(input("How many 200 naira notes?: "))*200
    total += int(input("How many 500 naira notes?: "))*500
    total += int(input("How many 1000 naira notes?: "))*1000
    return total

def is_transaction_succesful(money_recieved,drink_cost):
    """Return true when the money is accepted, or false if money is insufficient"""
    if money_recieved>=drink_cost:
        profit += drink_cost
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change £{change}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False



is_on= True
while is_on:
    choice  =input("​What would you like? (espresso/latte/cappuccino):")
    if choice =="off".lower():
        is_on= False
    elif choice == "report".lower():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['water']}g")
        print(f"money: ${resources['money']}")
    else:
        drink = MENU[choice]
        # print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()


