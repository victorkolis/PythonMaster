# simple_calculator.py

import art
import subprocess
import math

def logo():
    subprocess.call("clear")
    print(art.logo) 

logo()

def final_logo(string):
    subprocess.call("clear")
    print("""
 _____________________
|  ___________________|
| |"""+ string + """
| |___________________| 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| | 
| | . | 0 | = | | / | | 
| |___|___|___| |___| |
|_____________________|
""")

def add(n1, n2):
    return decimal_checker(round(n1 + n2, 2))
    
def subtract(n1, n2):
    return decimal_checker(round(n1 - n2, 2))

def multiply(n1, n2):
    return decimal_checker(round(n1 * n2, 2))

def divide(n1, n2):
    return decimal_checker(round(n1 / n2, 2))

operations = {'+':add, '-':subtract, 'x':multiply, '/':divide}

def decimal_checker(number):
    number = str(number)
    if ".0" in number:
        return math.trunc(float(number))
    else:
        return number

_continue = True

num1 = float(input('\n\n::::: '))
operation_symbol = input('::::: ')
num2 = float(input('::::: '))

function = operations[operation_symbol]

logo()


if ".0" in str(num1) and ".0" in str(num2):
    final_logo(str(function(num1, num2)))
    print(f"{int(num1)}{operation_symbol}{int(num2)}")
elif ".0" in str(num1):
    final_logo(str(function(num1, num2)))
    print(f"{int(num1)} {operation_symbol} {num2} = " + str(function(num1, num2)))
elif ".0" in str(num2):
    final_logo(str(function(num1, num2)))
    print(f"{num1} {operation_symbol} {int(num2)} = " + str(function(num1, num2)))
else:
    final_logo(str(function(num1, num2)))
    print(f"{num1} {operation_symbol} {num2} = " + str(function(num1,num2)))
