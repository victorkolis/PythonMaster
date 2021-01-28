#!/usr/bin/env python3

def sum_two_smallest_numbers(numbers):
	numbers.sort()
	return numbers[0] + numbers[1]

print(sum_two_smallest_numbers([-10, 5, 6 , 55, 1]))


# or 

def sum_two_smallest_numbers(a):
	return sorted(a)[0] + sorted(a)[1]