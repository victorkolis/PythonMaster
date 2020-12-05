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

    # Process coins
    print('Please insert coins.')
    quarters = int(input('QUARTERS: ')) * 0.25
    dimes = int(input('DIMES: ')) * 0.10
    nickles = int(input('NICKLES: ')) * 0.05
    pennies = int(input('PENNIES: ')) * 0.01
