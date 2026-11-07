from requirements import MENU, resources, logo
print(logo)

# Global Constants
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01
machine_money = 0

def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${machine_money}")

machine_running = True
while machine_running:
    # prompt
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

    # turn off coffee machine when prompt is off
    if user_choice == "off":
        machine_running = False
        continue

    # print report if prompt is report
    elif user_choice == "report":
        print_report()
    else:
        if user_choice not in MENU:
            print("Incorrect Choice")
            continue
        else:
            # check sufficient resources
            insufficient_ingredients = False
            for resource in resources:

                stock = resources[resource]
                coffee_requirements = MENU[user_choice]["ingredients"][resource]

                if stock < coffee_requirements:
                    print(f"Sorry, there is not enough {resource}")
                    insufficient_ingredients = True

            # When ingredients are not enough, prompt for user choice
            if insufficient_ingredients:
                continue

            # process coins
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            coins_inserted = (quarters * QUARTER) + (dimes * DIME) + (nickels * NICKEL) + (pennies * PENNY)

            # check transaction successful?
            coffee_cost = MENU[user_choice]["cost"]
            if coins_inserted < coffee_cost:
                print("Sorry that's not enough money. Money refunded.")
                continue
            elif coins_inserted == coffee_cost:
                machine_money += coffee_cost
            else:
                machine_money += coffee_cost
                change = float(coins_inserted - coffee_cost)
                print(f"Here is ${change:.2f} in change.")

            # make coffee
            for resource in resources:

                coffee_requirements = MENU[user_choice]["ingredients"][resource]
                resources[resource] -= coffee_requirements

            print(f"Here is your {user_choice} ☕. Enjoy!")