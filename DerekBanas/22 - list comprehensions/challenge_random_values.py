#!/usr/bin/env python3

from random import *

# Generate 50 random numbers that are multiples of 9

counter = 1
while True:
	number = randint(1, 1000)
	if number % 9 == 0:
		print(f'{counter} {number}')
		counter += 1
	if counter > 50:
		break


# Using list comprehension
print([x for x in [randrange(1, 1000) for _ in range(1000)] if x % 9 == 0])
