#!/usr/bin/env python3

def get_day(day, is_leap):
	months = {
		'Jan' or 'Mar': 31,
		'May' or 'Jul': 31,
		'Aug' or 'Oct': 31,
		'December': 31,
		
		'Apr' or 'Jun': 30,
		'Set' or 'Nov': 30,
		
		'Feb': 28,
	}
	
	if is_leap:
		pass
	else:
		
		
	
	
	
print(get_day(41, False))


"""
Jan 31
Feb 28
Mar 31
Apr 30
May 31
Jun 30
Jul 31
Aug 31
Sep 30
Oct 31
Nov 30
Dec 31
"""
