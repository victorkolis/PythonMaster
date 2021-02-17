#!/usr/bin/env python3

# Add the ints and subtract by the strings added up

def div_con(x):
	
	subtracted = 0
	subtractor = 0
	
	for element in x:
		try:
			if element.isnumeric():
				subtractor += int(element)
		except AttributeError:
			subtracted += int(element)
			
	return subtracted - subtractor
	

print(div_con([9, 3, '7', '3']))
