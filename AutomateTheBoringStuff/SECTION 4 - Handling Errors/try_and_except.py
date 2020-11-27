# try_and_except.py


def div(argument):
    try:
        return 42 / argument
    except:
        return "** Division error"

print(div(2))
print(div(5))
print(div(10))
print(div(0))
print(div(7))
