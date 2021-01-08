def calc_type(a, b, res):
    if a * b == res:
        return 'multiplication'
    elif a / b == res:
        return 'division'
    elif a + b == res:
        return 'addition'
    elif a - b == res:
        return 'subtraction'


print(calc_type(7, 3, 21))

