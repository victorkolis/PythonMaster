#!/usr/bin/env python3

def solution(matrix):
	return True if '>x' in [''.join(x).replace(' ', '') for x in matrix] else False
	
	
print(solution(
	[
		[' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' '],
		[' ', ' ', '>', ' ', 'x'],
		[' ', ' ', '', ' ', ' ']
	]
))
