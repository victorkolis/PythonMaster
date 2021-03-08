#!/usr/bin/env python3

# Convert the cockroach speed from (km/h -> cm/s) floor/round it down
# Formula: Multiply kilometers per hour * 27.778 get -> centimeters per second


import math


def cockroach_speed(s: int or float) -> int:
	return math.floor(s * 27.778)
	

print(cockroach_speed(1.08))


