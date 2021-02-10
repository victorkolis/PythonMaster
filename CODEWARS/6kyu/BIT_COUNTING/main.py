#!/usr/bin/env python3

# Convert a given number into binary and then count the '1' that show up and retun it
# integer: 10 -> binary: 1010 -> 2


def count_bits(n):
	return '{0:b}'.format(n).count('1')


print(count_bits(10))
