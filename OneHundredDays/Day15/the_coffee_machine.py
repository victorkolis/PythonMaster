import items

while True:
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'off':
        break
    elif order == 'report':
        print(items.MENU)
