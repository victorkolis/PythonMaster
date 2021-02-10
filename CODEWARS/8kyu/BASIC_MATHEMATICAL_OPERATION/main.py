#!/usr/bin/env python3

def basic_op(op, v1, v2):
	return v1 + v2 if op == '+' else v1 - v2 if op == '-' else v1 * v2 if op == '*' else v1 / v2
	

print(basic_op('-', 3, 2))
