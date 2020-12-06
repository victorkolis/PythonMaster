import items

while True:
    order = input('What would you like? (espresso/latte/cappuccino): ')
    # Turns the coffee machine off
    if order == 'off':
        break
    # Check the coffee machine resources
    elif order == 'report':
        resources = list(items.resources.items())
        for resource in resources:
            resource_name, resource_quantity = resource
            if resource_name == 'coffee':
                print(f'{resource_name.title()}: {resource_quantity}g ')
            elif resource_name == 'money':
                print(f'{resource_name.title()}: ${resource_quantity} ')
            else:
                print(f'{resource_name.title()}: {resource_quantity}ml ')
    elif order == 'espresso':
        if items.resources['water'] < items.MENU.get("espresso").get("ingredients").get("water"):
            print(f"Sorry, there is not enough Water.")
        elif items.resources['coffee'] < items.MENU.get("espresso").get("ingredients").get("coffee"):
            print(f"Sorry, there is not enough Coffee.")

    elif order == 'latte' or order == 'cappuccino':
        if items.resources['water'] < items.MENU.get(order).get("ingredients").get("water"):
            print(f"Sorry, there is not enough Water.")
        elif items.resources['coffee'] < items.MENU.get(order).get("ingredients").get("coffee"):
            print(f"Sorry, there is not enough Coffee.")
        elif items.resources['milk'] < items.MENU.get(order).get("ingredients").get("milk"):
            print(f"Sorry, there is not enough Milk.")

    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        # Process coins
        print('Please insert coins.')
        quarters = float(input('QUARTERS: ')) * 0.25
        dimes = float(input('DIMES: ')) * 0.10
        nickles = float(input('NICKLES: ')) * 0.05
        pennies = float(input('PENNIES: ')) * 0.01
        coins_total = round(quarters + dimes + nickles + pennies, 2)

        # Check the amount of money summed up
        if coins_total > items.MENU[order]['cost']:
            print(f"Here is ${coins_total - items.MENU[order]['cost']} in change")
            print(f"Here is your {order} ☕️ enjoy!!")

            # Subtract the resources in order to emulate a real coffee machine using its internal resources.
            for resource in items.MENU.get('espresso').values():
                item = resource
                
        else:
            print("Sorry, that's not enough money. Money refunded.")
