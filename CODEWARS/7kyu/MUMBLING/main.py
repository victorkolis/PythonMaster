#!/usr/bin/env python3

# accum("abcd") -> "A-Bb-Ccc-Dddd"

def accum(s):
	mumble = ''
	for index, element in enumerate(s):
		index += 1
		mumble += element * index
		if index < len(s):
			mumble += '-'
	
	return mumble.title()

print(accum("abcd"))
