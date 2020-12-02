# debugging.py

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

'''
The iterator 'i' was not being incremented, therefore, this loop could not
function properly since the 'if i == 20' would never be satisfied. If the condition
is never satisfied since there is no 'else'condition nor the increment the comparison
breaks the program short. The range only produces numbers up to but not iuncluding the
delimitation or last number.
'''

# SOLUTION #01
def my_function():
    for i in range(1, 21):
        if i == 20:
          print("You got it")
my_function()

# SOLUTION #02
def my_function():
    for i in range(1, 20):
        i += 1
        if i == 20:
          print("You got it")
my_function()
