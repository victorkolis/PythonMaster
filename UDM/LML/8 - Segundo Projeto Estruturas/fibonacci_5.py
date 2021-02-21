#!/usr/local/bin/python3


# Use sum in this exercise in order to achieve the same

# 0, 1, 1, 2, 3, 5, 8, 13, 21 
def fibonacci(limit):
    result = [0, 1]
    while True:
        if result[len(result) - 1] > limit:
            break
        else:
            result += [sum(result[-2:])] 
    
    return result


if __name__ == '__main__':
    for fib in fibonacci(100000):
        print(fib)

