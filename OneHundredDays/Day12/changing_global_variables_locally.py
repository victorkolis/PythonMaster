# changing_global_variables_locally.py

# not a very good practice
global_variable = 0

def function():
    for iterator in range(9):
        global global_variable
        global_variable += 2

function()

print(global_variable)

# a very good practice

def function():
    new_value = 0
    for iterator in range(9):
        new_value += 1
    return new_value

global_variable = function()

print(global_variable)
