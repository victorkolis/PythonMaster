# simple_calculator.py

import art
import subprocess
import math

def logo():
    subprocess.call("clear")
    print(art.logo) 

logo()

def add(n1, n2):
    return decimal_checker(round(n1 + n2, 2))
    
def subtract(n1, n2):
    return decimal_checker(round(n1 - n2, 2))

def multiply(n1, n2):
    return decimal_checker(round(n1 * n2, 2))

def divide(n1, n2):
    return decimal_checker(round(n1 / n2, 2))

operations = {'+':add, '-':subtract, 'x':multiply, '/':divide}

print("available operations: ")
for operation in operations:
    print(f"{operation}", end=' ')

def decimal_checker(number):
    number = str(number)
    if ".0" in number:
        return math.trunc(float(number))
    else:
        return number

num1 = float(input('\n\n::::: '))
operation_symbol = input('::::: ')
num2 = float(input('::::: '))

function = operations[operation_symbol]

logo()

if ".0" in str(num1) and ".0" in str(num2):
    print(f"{int(num1)} {operation_symbol} {int(num2)} = " + str(function(num1, num2)))
elif ".0" in str(num1):
    print(f"{int(num1)} {operation_symbol} {num2} = " + str(function(num1, num2)))
elif ".0" in str(num2):
    print(f"{num1} {operation_symbol} {int(num2)} = " + str(function(num1, num2)))
else:
    print(f"{num1} {operation_symbol} {num2} = " + str(function(num1,num2)))
