#!/usr/bin/env python3

def draw_stairs(x: int) -> str:
	n = ''
	for _ in range(x):
		n += ' ' * _ + 'I'
		if _ < x - 1:
			n += '\n'
	return n


print(draw_stairs(8))
