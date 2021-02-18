#!/usr/bin/env python3

# Like a credit card masking -> ###1234

def maskify(cc):
	new_cc = ''
	if len(cc) <= 4:
		return cc
	else:
		limit = len(cc) - 4
		for _ in range(limit):
			new_cc += '#'
		
		for _ in range(limit, len(cc)):
			new_cc += cc[_]
	
	return new_cc
	

print(maskify('1234567890'))
