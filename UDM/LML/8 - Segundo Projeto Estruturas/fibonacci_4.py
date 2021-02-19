#!/usr/bin/env python3

def fibonacci(limit):
	result = [0, 1]
	while True:
		result += [result[-2] + result[-1]]
		if result[-1] > limit:
			break
	return result


if __name__ == '__main__':
	for fib in fibonacci(10000):
		print(fib)
