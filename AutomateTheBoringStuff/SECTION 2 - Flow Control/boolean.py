# boolean.py

print(5 > 4)
print(not 5 > 4)

# Boolean reserved keywords

# not
True
False

# Truth table

# And
True  and True  # True
True  and False # False
False and True  # False
False and False # False

# Or
True  or True  # True
True  or False # True
False or True  # True
False or False # False

# XOR (Exclusive or)
True  != True  # False
True  != False # True
False != True  # True
False != False # False

# Logical Operators

# Equal to
# ==

# Not equal to
#!=

# Less than
#<

# Greater than
#>

# Less than or equal to
#<=

# Greater than or equal to
#>=

# Truthy & Falsey values
# Whenever an empty string is returned, that is considered-
# a falsey all other states are considered a truthy, spaces
# and other characters.

name = input("What is your name?\n")

# Whenever the condition on if is not compared against anything-
# it is comparing to True by default for strings. Whenever it-
# comes to integers the 0 is falsey and anything else is truthy

if name:
    print("Thank you for entering a name.")
else:
    print("You did not enter a name.")

print(bool(0)) # falsey
print(bool(1)) # truthy
print(bool(-1)) # truthy