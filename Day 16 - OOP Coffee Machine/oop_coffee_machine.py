from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects for each class
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    # prompt
    user_choice = input(f"What would you like? {coffee_menu.get_items()}:: ").lower()

    # turn off coffee machine when prompt is off
    if user_choice == "off":
        machine_is_on = False
    # 1. print report
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = coffee_menu.find_drink(user_choice)
        # 2. check resources sufficient and 3. process coins 4. check transaction successful
        if order is not None and coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            # 5. make coffee
            coffee_maker.make_coffee(order)