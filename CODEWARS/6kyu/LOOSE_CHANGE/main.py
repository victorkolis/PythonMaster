def loose_change(cents):
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    cents = int(cents)
    for number in range(cents, 0, -25):
        if cents < 25:
            break
        else:
            change_dict['Quarters'] += 1
            cents -= 25

    for number in range(cents, 0, -10):
        if cents < 10:
            break
        else:
            change_dict['Dimes'] += 1
            cents -= 10

    for number in range(cents, 0, -5):
        if cents < 5:
            break
        else:
            change_dict['Nickels'] += 1
            cents -= 5

    for number in range(cents, -1, -1):
        if cents < 1:
            break
        else:
            change_dict['Pennies'] += 1
            cents -= 1

    return change_dict


print(loose_change(445))
