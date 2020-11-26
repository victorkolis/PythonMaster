# abs_function.py

# This is just a representatio of what the abs function might look like
def absolute(argument):
    if argument < 0:
        argument = -argument
        return argument
    elif argument == True:
        return 1
    elif argument == False:
        return 0
    

# My module
print(absolute(-1))


# The abs function returns the absolute value of a given number ignoring the negative symbol for example
# Standard
print(abs(-1))


print(absolute(not False))
print(abs(False))
