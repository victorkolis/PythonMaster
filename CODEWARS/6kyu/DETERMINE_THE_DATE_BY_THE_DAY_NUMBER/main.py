#!/usr/bin/env python3

def get_day(days, is_leap): 
	calendar = {
		"January": 31,
		"February": 28 + (1 if is_leap else 0),
		"March": 31,
		"April": 30,
		"May": 31,
		"June": 30,
		"July": 31,
		"August": 31,
		"September": 30,
		"October": 31,
		"November": 30,
		"December": 31
		}
	
	# Testing for months
	for month in calendar:
		if days <= calendar[month]:
			return f'{month}, {days}'
		
		# Reducing the days
		days -= calendar[month]


	
print(get_day(258, False))
