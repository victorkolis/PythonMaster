#!/usr/bin/env python3

def century(year: int) -> int:
	return (year - 1) // 100 + 1


print(century(400))
