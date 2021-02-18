#!/usr/bin/env python3

def vowel_2_index(string):
	new_string = ''
	for index, letter in enumerate(list(string)):
		if letter in 'aAeEiIoOuU':
			new_string += str(index + 1)
		else:
			new_string += letter
	
	return new_string
	
	
print(vowel_2_index('sentence here'))
