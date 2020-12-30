def factorial(value):
    if value <= 1:
        return 1
    else:
        result = value + factorial(value - 1)
        return result


print(factorial(10))
