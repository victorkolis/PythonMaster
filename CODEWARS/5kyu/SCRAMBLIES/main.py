#!/usr/bin/env python3

# Check whether it is possible to create s2 with letters in s1

def scramble(s1, s2):
	s2 = sorted(s2)
	s1 = sorted(s1)
	
	for letter in s2:
		try:
			s1.remove(letter)
		except ValueError:
			return False
	
	return True


print(scramble('cedewaraaossoqqyt', 'codewars'))
