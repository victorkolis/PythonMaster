# try_and_except.py


def div(argument):
    try:
        return 42 / argument
    except ZeroDivisionError:
        return "** Division error"
    except TypeError:
        return "** Please enter a number"


print(div('a'))
print(div(5))
print(div(10))
print(div(0))
print(div(7))
