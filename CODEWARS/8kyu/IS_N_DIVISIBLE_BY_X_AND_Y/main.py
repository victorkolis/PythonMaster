#!/usr/bin/env python3

def is_divisible(n,x,y):
	return True if n % x == 0 and n % y == 0 else False


print(is_divisible(10, 3, 7))
