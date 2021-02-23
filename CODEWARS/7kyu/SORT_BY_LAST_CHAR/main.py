#!/usr/bin/env python3

# Given a string, return a last-letter sorted array of words

def last(s):
	s = [x for x in s.split()]
	return sorted(s, key=lambda x: x[-1])


print(last('what time are we climbing up the volcano'))
