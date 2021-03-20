
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


def report():
    for item in resources:
        print(f"{item}: {resources[item]}")
    start()


def process_money(cost):
    print("Insert Coins")
    quarters = int(input('Enter quarters'))
    dimes = int(input('Enter dimes'))
    nickels = int(input('Enter nickels'))
    pennies = int(input('Enter pennies'))
    total = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
    balance = total-cost
    if balance>0:
        print(f"Here is your ${balance}")
        return 0
    elif balance == 0:
        return 0
    else:
        print("Insufficient money")
        return 1


def prepare_coffee(coffee):
    bal = process_money(MENU[coffee]['cost'])
    if bal==0:
        for item in MENU[coffee]["ingredients"]:
            resources[item] -= MENU[coffee]["ingredients"][item]
        print(f"enjoy your {coffee}")
        start()
    else:
        start()


def coffee_selected(coffee):
    for item in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][item]>resources[item]:
            print(f"sorry! not enough {item}")
            start()
    prepare_coffee(coffee)


def start():
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice=="report":
        report()
    elif choice=="espresso" or "latte" or "cappuccino":
        coffee_selected(choice)


start()
