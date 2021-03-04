#!/usr/bin/env python3

def perfect_roots(x: int) -> int:
	for number in x:
		x = x ** .5
		if type(x) == float:
			return False
	
	return True
	

print(perfect_roots(256))
