import items

while True:
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'off':
        break
    elif order == 'report':
        resources = list(items.resources.items())

        for resource in resources:
            resource_name, resource_quantity = resource
            if resource_name == 'coffee':
                print(f'{resource_name.title()}: {resource_quantity}g ')
            else:
                print(f'{resource_name.title()}: {resource_quantity}ml ')
    elif order == 'espresso':
        if items.resources['water'] < items.resources['water']:
