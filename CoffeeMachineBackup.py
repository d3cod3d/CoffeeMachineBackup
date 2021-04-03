import sys


def main_menu():

    global customer_choice
    global break_out_flag
    customer_choice = input("""\nWhat would you like?\n
       1. Espresso
       2. Latte
       3. Cappuccino

       Press button of your choice: """)
    check_override(str(customer_choice))


def main_menu2():
    global customer_choice
    global break_out_flag
    customer_choice = int(customer_choice)
    print(customer_choice)
    if customer_choice < 1 or customer_choice > 3:
        print("Do not attempt to hack the coffee machine!")
        break_out_flag = True
    return 0


def check_water(choice):
    if choice == 1 and resources["water"] > 50:
        return True
    elif choice == 2 and resources["water"] > 200:
        return True
    elif choice == 3 and resources["water"] > 250:
        return True
    else:
        return False


def check_milk(choice):
    if choice == 1:
        return True
    elif choice == 2 and resources["milk"] > 150:
        return True
    elif choice == 3 and resources["milk"] > 100:
        return True
    else:
        return False


def check_coffee(choice):
    if choice == 1 and resources["coffee"] > 18:
        return True
    elif choice == 2 and resources["coffee"] > 24:
        return True
    elif choice == 3 and resources["coffee"] > 24:
        return True
    else:
        return False


def enough_resources(choice):
    global break_out_flag
    if not check_water(choice):
        print("Sorry! not enough water.\nPlease make another selection")
        break_out_flag = True
        return False
    elif not check_milk(choice):
        print("Sorry! not enough milk.\nPlease make another selection")
        break_out_flag = True
        return False
    elif not check_coffee(choice):
        print("Sorry! not enough coffee.\nPlease make another selection")
        break_out_flag = True
    else:
        return True


def check_override(choice):
    global break_out_flag
    if choice == "off":
        sys.exit("shutting down")
    elif choice == "report":
        for key, value in resources.items():
            print(key, ' : ', value)
            break_out_flag = True
    if choice != str("1") and choice != str("2") and choice != str("3"):
        print("Invalid input")
        break_out_flag = True

    return 0


def cost(choice):
    if choice == 1:
        cost_of_drink = (MENU["espresso"]["cost"])
        return cost_of_drink
    if choice == 2:
        cost_of_drink = (MENU["latte"]["cost"])
        return cost_of_drink
    if choice == 3:
        cost_of_drink = (MENU["cappuccino"]["cost"])
        return cost_of_drink


def process_coins(choice):
    global break_out_flag
    print(f"{ITEMS[choice - 1]}'s cost $ {'{:.2f}'.format(cost(choice))} ")
    print("Please insert coins ")
    cost_of_drink = float("{:.2f}".format(cost(choice)))
    quarters = int(input("How many Quarters?"))
    dimes = int(input("How many Dimes"))
    nickles = int(input("How many nickles"))
    pennies = int(input("How many Pennies"))
    total_change_inserted = float(quarters * .25) + float(dimes * .10) + float(nickles * .05) + float(pennies * .01)
    if total_change_inserted < cost_of_drink:
        print("You did not insert enough money for your purchase, money refunded")
        break_out_flag = True

    elif total_change_inserted >= cost_of_drink:
        refund = total_change_inserted - cost_of_drink
        print(f"Thank You!\nyour change is ${'{:.2f}'.format(refund)}")
    return 0


def make_coffee(choice):
    print("making coffee\n.\n.\n.")
    if choice == 1:
        resources["water"] -= 50
        resources["coffee"] -= 18
        resources["money"] += 1.5
    elif choice == 2:
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        resources["money"] += 2.5
    elif choice == 3:
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        resources["money"] += 3.0
    print(f"Here is your {ITEMS[choice-1]}. Enjoy!")


ITEMS = ["Espresso", "Latte", "Cappuccino"]
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
    "money": 0,
}

machine_on = True

while machine_on:
    break_out_flag = False
    while not break_out_flag:
        customer_choice = 0
        main_menu()
        if break_out_flag:
            break
        main_menu2()
        if break_out_flag:
            break
        enough_resources(customer_choice)
        if break_out_flag:
            break
        process_coins(customer_choice)
        if break_out_flag:
            break
        make_coffee(customer_choice)
