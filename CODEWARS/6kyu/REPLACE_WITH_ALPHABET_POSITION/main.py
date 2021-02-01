#!/usr/bin/env python3

# a -> 1, b -> 2 and etc.

import string

def alphabet_position(text):
	text = text.lower()
	new_text = ''
	alphabet = ' '.join(string.ascii_lowercase).split()
	
	for word in text:
		if word.isalpha():
			new_text += f'{alphabet.index(word) + 1} '
	
	return new_text.strip()
	

print(alphabet_position('the'))
