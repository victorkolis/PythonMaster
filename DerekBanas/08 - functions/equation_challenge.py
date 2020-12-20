# This software objective is to solve the + equations given to it such as: x + 5 = 10

def solve_equation(problem):
    values = problem.replace('x', '').replace(' ', '').replace('+', ' ').replace('=', '')
    values = values.split()
    print(values)
    num1 = 0
    num2 = 0
    for value in values:
        value = int(value)
        if num1 != num2:
            num1 = value
        else:
            num2 = value

    x = num1 - num2
    print(f'x is equal to {x}.')


equation = input('Enter the equation.\ne.g: 5 + x = 7\n')
solve_equation(equation)
