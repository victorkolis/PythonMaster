# multiple_assignment.py


def variable_flipper1(a, b):
    a, b = b, a
    return a, b

def variable_flipper2(a, b):
    return b, a

print('Assign values to these variables below. So that I can swap them.')
num1 = int(input('num1: '))
num2 = int(input('num2: '))


num1, num2 = variable_flipper2(num1, num2)

print(f'Now num1 is {num1} and num2 is {num2}')
