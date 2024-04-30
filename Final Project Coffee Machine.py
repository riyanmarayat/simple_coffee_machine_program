MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 50,
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

type_of_coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

profit = 0

list_user_input = ["espresso", "latte", "cappuccino", "off", "report"]


def user_input():
    """Fungsi untuk user dapat memasukkan input yang diingkannya"""
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user not in list_user_input:
        print(f"Sorry your input '{user}' is wrong, please input the right word!")
        user_input()
    else:
        return user


def turn_off():
    """Mematikan coffee machine jika input yang dimasukan 'off'"""
    print("\033[2J\033[H", end="", flush=True)  # clear console
    return False


def print_report():
    """Fungsi untuk mengeluarkan report berupa nilai resources yang tersisa jika user menginput 'report'"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")


def is_resources_sufficient(drink):
    """Fungsi untuk mengecek apakah resources yang tersedia cukup untuk membuat pesanan konsumen"""
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough milk")
        return False
    else:
        return True


def process_coins(_quarters, _dimes, _nickles, _pennies):
    """Fungsi untuk memproses total uang yang dimasukan oleh konsumen"""
    total_money = (int(_quarters) * type_of_coins["quarters"] + int(_dimes) * type_of_coins["dimes"] + int(_nickles)
                   * type_of_coins["nickles"] + int(_pennies) * type_of_coins["pennies"])
    return total_money


def is_transaction_success(_money, drink):
    if _money < MENU[drink]["cost"]:
        print(f"Sorry that's not enough money to buy a {drink}. You must pay ${MENU[drink]["cost"]}. Money "
              f"${_money} refunded.")
        return False
    elif _money > MENU[drink]["cost"]:
        print(f"Here is ${_money - MENU[drink]["cost"]:.2f} dollars in change.")
        return True
    else:
        return True


# TODO 7. Make Coffee
#   a. If the transaction is successful and there are enough resources to make the drink the user selected, then the
#      ingredients to make the drink should be deducted from the coffee machine resources.
#      E.g. report before purchasing latte:
#      Water: 300ml
#      Milk: 200ml
#      Coffee: 100g
#      Money: $0
#      _
#      Report after purchasing latte:
#      Water: 100ml
#      Milk: 50ml
#      Coffee: 76g
#      Money: $2.5
#      _ DONE Done
#   b. Once all resources have been deducted, tell the user "Here is your latte. Enjoy!". If latte was their choice of
#      drink.
def make_coffee(drink):
    global resources
    global profit
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    profit += MENU[drink]["cost"]


is_coffee_machine_run = True
while is_coffee_machine_run:
    user_prompt = user_input()
    if user_prompt == "off":
        is_coffee_machine_run = turn_off()
        break
    elif user_prompt == "report":
        print_report()
        continue
    elif user_prompt in MENU:
        if not is_resources_sufficient(user_prompt):
            continue
        print("Please insert your coins.")
        user_quarters = input("How many quarters?: ")
        user_dimes = input("How many dimes?: ")
        user_nickles = input("How many nickles?: ")
        user_pennies = input("How many pennies?: ")
        user_money = process_coins(user_quarters, user_dimes, user_nickles, user_pennies)
        if not is_transaction_success(user_money, user_prompt):
            continue
        make_coffee(user_prompt)
        print(f"Here is your {user_prompt}. Enjoy!")
