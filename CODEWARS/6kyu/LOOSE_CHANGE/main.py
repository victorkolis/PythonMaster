def loose_change(cents):
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    cents = int(cents)
    for number in range(cents, 0, -25):
        if number != cents:
            change_dict['Quarters'] += 1
            cents -= 25

    for number in range(cents, 0, -10):
        if number != cents:
            change_dict['Dimes'] += 1
            cents -= 10

    for number in range(cents, 0, -5):
        if number != cents:
            change_dict['Nickels'] += 1
            cents -= 5

    for number in range(cents, -1, -1):
        if number != cents:
            change_dict['Pennies'] += 1
            cents -= 1

    return change_dict


print(loose_change(125))
