# multiple_assignment.py

def variable_flipper(a, b):
    
    a, b = b, a
    return a, b

print('Assign values to these variables below. So that I can swap them.')
num1 = int(input('num1: '))
num2 = int(input('num2: '))


num1, num2 = variable_flipper(num1, num2)

print(f'Now num1 is {num1} and num2 is {num2}')
