#!/usr/bin/env python3

# Count how many duplicates of a given letter is found in an array/list

def duplicate_count(text):
	text = sorted([x.lower() for x in text])  # sorted to speed the search
	singled_letters = sorted(list(set(text)))
	counter = 0
	for letter in singled_letters:
		if text.count(letter) > 1:
			counter += 1
			
	return counter
	
print(duplicate_count("Abccdeaa"))