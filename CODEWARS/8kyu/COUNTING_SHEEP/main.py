#!/usr/bin/env python3


def count_sheeps(sheep):
	sheeps = 0
	for element in sheep:
		if element:
			sheeps += 1
			
	return sheeps
	
	
print(count_sheeps([True,  True,  True,  False,
		True,  True,  True,  True ,
		True,  False, True,  False,
		True,  False, False, True ,
		True,  True,  True,  True ,
		False, False, True,  True ]))
