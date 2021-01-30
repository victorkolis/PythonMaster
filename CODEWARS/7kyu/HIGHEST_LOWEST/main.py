#!/usr/bin/env python3

# Return the minimum and maximum values in a string

def high_and_low(numbers):
	return f'{str(max([int(x) for x in numbers.split()]))} {str(min([int(x) for x in numbers.split()]))}'
	

print(high_and_low("-1 2 3 4 5"))
