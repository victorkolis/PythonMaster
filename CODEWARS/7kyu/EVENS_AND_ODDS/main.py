#!/usr/bin/env python3

# Convert odds to hexadecimal and evens to binary

def evens_and_odds(n):
	return '{0:b}'.format(n) if n % 2 == 0 else '{0:x}'.format(n)


print(evens_and_odds(47))
