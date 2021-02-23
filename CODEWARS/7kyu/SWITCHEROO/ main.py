#!/usr/bin/env python3

# replace a's for b's and vice versa

def switcheroo(string):
	new_string = ''
	for letter in string:
		if letter == 'a':
			new_string += 'b'
		elif letter == 'b':
			new_string += 'a'
			
		else:
			new_string += letter
	return new_string


print(switcheroo('abcdefababbbbaaa'))
