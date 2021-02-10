#!/usr/bin/env python3

# 347 -> 3 + 4 + 7 -> 14 -> 1 + 4 -> 5

def digital_root(n: int) -> int:
	sum_of_digits = 0
	
	# The final number cannot contain 2 digits
	while n >= 10:
		for element in str(n):
			sum_of_digits += int(element)
		n = sum_of_digits
		
		# sum_of_digits must be reset, otherwise, the number is going to add  up to infinity
		sum_of_digits = 0
	return n
	
print(digital_root(347))
