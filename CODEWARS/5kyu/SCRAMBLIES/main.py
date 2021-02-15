#!/usr/bin/env python3

# Check whether it is possible to create s2 with letters in s1

def scramble(s1, s2):
	add2 = 0
	add1 = 0
	
	for letter in s2:
		if s2.count(letter) > s1.count(letter):
			return False

	return True
	
	
print(scramble('katas', 'steak'))
