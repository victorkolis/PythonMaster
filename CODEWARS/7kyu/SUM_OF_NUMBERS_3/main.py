#!/usr/bin/env python3

# Sum all the numbers in a range between two given numbers, save those who are; 
# similar. Those should return themselves.

def get_sum(x, y):
	greater = max(x, y)
	lesser  = min(x, y)
	account = 0
	if x == y:
		return x
	else:
		for number in range(lesser, greater + 1):
			account += number
			
	return account

print(get_sum(-1, 2))
