#!/usr/local/bin/python3

def fibonacci(quantity):
    result = [0, 1]
    while True:
        result += [sum(result[-2:])]
        if len(result) == quantity:
            break

    return result


counter = 1
if __name__ == '__main__':
    for fib in fibonacci(20):
        print(f'{counter}:\t {fib}')
        counter += 1
