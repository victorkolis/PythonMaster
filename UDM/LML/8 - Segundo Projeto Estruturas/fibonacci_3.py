#!/usr/bin/env python3

# 0, 1, 1, 2, 3, 5, 8...


def fib(limit):
	penult = 0
	last = 1
	print(0, end=', ')
	
	while True:
		
		print(last, end=', ')
		penult, last = last, penult + last
		if last > limit:
			print()
			break


if __name__ == '__main__':
	fib(10000000000)
