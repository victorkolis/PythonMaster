#!/usr/bin/env python3

def get_count(str):
	
	vowels = 0
	
	for letter in str:
		if letter in ['a', 'e', 'i', 'o', 'u']:
			vowels += 1
			
	return vowels
	


print(get_count('victor vinicius reis de matos'))
