# building_mine_own_functions.py

def hi():
    print("Hi there!")
    print("How's you doing mahn?")
    print("How's tricks?")
    print("")


for i in range(3):
    hi()


# returning a value


def plus_one(number):
    return number + 1


print(plus_one(27))

# Every single function has a return value, if not defined it automatically returns the 'None' value
# you are not obligated to define the return
