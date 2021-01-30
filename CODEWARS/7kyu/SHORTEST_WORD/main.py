#!/usr/bin/env python3

# Find the shortest word in a given string

def find_short(s: str) -> str:
	current_word = s.split()[0]
	for word in s.split():
		if len(word) < len(current_word):
			current_word = word
	
	return len(current_word)

print(find_short("bitcoin take over the world maybe who knows perhaps"))