#!/usr/bin/env python3


def sequence(a):
	return [int(y) for y in sorted([str(x) for x in range(1, a + 1)])]

print(sequence(20))

