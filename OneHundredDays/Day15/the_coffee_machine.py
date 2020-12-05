import items

while True:
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'off':
        break
    elif order == 'report':
        resources = list(items.resources.items())

        for resource in resources:
            resource_name, resource_quantity = resource
            if
            print(f'{resource_name}: {resource_quantity} ')
