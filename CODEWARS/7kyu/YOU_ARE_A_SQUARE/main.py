#!/usr/bin/env python3


# Find out whether a given number is a square or not

def is_square(n):
	return True if '.0' in str(n ** .5) and len(str(n ** .5)) == 3 else False
	

print(is_square(0))
