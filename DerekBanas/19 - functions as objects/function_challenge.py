# Create a function that receives a list and a function
# The function passed will return True or False if a list value is odd
# Then the surrounding function will return a list of odd numbers


def odd_finder(number):
    if number % 2 != 0:
        return True
    else:
        return False


def func_and_list_receiver(numbers: list, func):
    odds = []
    for number in numbers:
        if func(number):
            odds += [number]

    return odds


print(func_and_list_receiver([x for x in range(20)], odd_finder))
