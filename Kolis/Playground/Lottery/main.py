#!/usr/bin/env python3

from random import *


def lottery() -> list:
	numbers = []
	for _ in range(6):
		new_number = randrange(1, 60)
		if new_number not in numbers:
			numbers += [new_number]
	return sorted(numbers)


print(lottery())
