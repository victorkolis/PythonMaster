# functions_with_output.py

# return - keyword

import math

def multiply(a, b):
    c = a * b
    c = str(c)
    if ".0" in c:
        return math.trunc(a * b)
    else:
        return round(float(c), 2)

a = float(input("enter a value: "))
b = float(input("enter another value: "))

result = multiply(a, b)

print(result)
