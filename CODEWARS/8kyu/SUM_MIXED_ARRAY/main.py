#!/usr/bin/env python3

# [1, '2', '2'] -> 5, sum the array

def sum_mix(arr: list) -> int:
	for index, element in enumerate(arr):
			if type(element) == str:
				arr[index] = int(element)
				
	
	return sum(arr)
	

print(sum_mix([9, 3, '7', '3']))
