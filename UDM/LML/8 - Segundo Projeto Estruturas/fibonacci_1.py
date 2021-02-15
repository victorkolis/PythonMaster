#!/usr/bin/env python3

# 0, 1, 1, 2, 3, 5, 8...


def fib():
	penult = 0
	last = 1
	print(f'{penult}, {last}', end=', ')
	
	while True:
		next_fib = penult + last
		print(next_fib, end=', ')
		penult, last = last, next_fib


if __name__ == '__main__':
	fib()

