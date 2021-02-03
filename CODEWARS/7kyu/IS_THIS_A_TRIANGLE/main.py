#!/usr/bin/env python3

# Given three measures check whether it is possible to create a triangle with them.

# Triangle Inequality Theorem

def is_triangle(a, b, c):
	
	return a + b > c and a + c > b and b + c > a
	

print(is_triangle(1, 2, 5))
