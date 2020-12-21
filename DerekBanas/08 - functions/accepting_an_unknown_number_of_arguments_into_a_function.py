def sum_all(*args):
    total = 0
    for number in args:
        total += number
    return total


print('Let\'s add them all!')
print(f'The total is : {sum_all(1, 2, 3, 4)}')
