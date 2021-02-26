#!/usr/bin/env python3

# Return me the amount of fibonacci I need

def fibonacci(x):
	if x <= 0:
		return []
	
	else:
		fibo = [0, 1]
		for _ in range(x):
			fibo.append(fibo[-2] + fibo[-1])
		
		return fibo[:x]


if __name__ == '__main__':
	print(fibonacci(2))
