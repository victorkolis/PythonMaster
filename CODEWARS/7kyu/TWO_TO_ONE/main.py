#!/usr/bin/env python3

def longest(a1, a2):
	a1 = sorted(list(set(a1)))
	a2 = sorted(list(set(a2)))
	a3 = sorted(list(set(a1 + a2)))
	
	return ''.join(a3)

print(longest("aretheyhere", "yestheyarehere"))

# "aehrsty"