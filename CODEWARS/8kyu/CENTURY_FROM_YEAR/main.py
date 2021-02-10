#!/usr/bin/env python3

def century(year: int) -> int:
	year = str(year)
	
	return int(year[0:2]) + int(year[len(year) - 1]) if int(year) > 999 else int(year[0]) + int(year[len(year) - 1])


print(century(1709))
