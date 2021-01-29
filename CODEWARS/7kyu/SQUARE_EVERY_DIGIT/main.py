#!/usr/bin/env python3

def square_digits(num):
	return int(''.join([str(int(number) * int(number)) for number in str(num)]))

print(square_digits(9119))
