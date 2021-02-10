#!/usr/bin/env python3

# add up all the multiples of 3 and 5

def solution(n):
	n_set = set()
	for multiple in range(1, n):
		if not multiple % 3 or not multiple % 5:
			n_set.add(multiple)
	
	return sum(n_set)
	
print(solution(10))
