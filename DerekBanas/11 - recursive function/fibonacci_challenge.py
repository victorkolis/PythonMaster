def fibonacci(f_range):
    if f_range == 0:
        return 0

    elif f_range == 1:
        return 1

    else:
        result = fibonacci(f_range - 1) + fibonacci(f_range - 2)
        return result
    pass


for _ in range(10):
    print(fibonacci(_))
