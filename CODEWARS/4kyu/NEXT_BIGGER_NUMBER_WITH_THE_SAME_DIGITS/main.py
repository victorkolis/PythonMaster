#!/usr/bin/env python3

def next_bigger(n: int) -> int:
	
	# Two digit cases
	if n < 99:
		n = str(n)
		m = int(n[1] + n[0])
		if m > int(n):
			return m
		else:
			return -1
	
	# Three digit case
	m = str(n)
	if len(m) == 3:
		m = m[0] + m[2] + m[1]
		m = int(m)
		if m > n:
			return m
		else:
			m = m[2] + m[0] + m[1]
			if m > n:
				return m
			else:
				return -1
	
	# Four and above cases
	for index, element in enumerate():
		
	

print(next_bigger(1234))
