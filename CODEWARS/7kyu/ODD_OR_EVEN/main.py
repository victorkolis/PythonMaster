#!/usr/bin/env python3

def odd_or_even(arr):
	return 'Even' if sum(arr) % 2 == 0 else 'Odd'


print(odd_or_even([1, 2, 5, 7]))
