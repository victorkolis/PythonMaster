#!/usr/bin/env python3

def palindromization(pattern: str, amount: int) -> str:
	if pattern == '' or amount == 1:
		return 'Error!'
	
	palindromized = []
	index = 0
	for iteration in range(amount):
		if len(palindromized) >= 2:
			try:
				palindromized.insert(len(palindromized)//2, pattern[index])
			except IndexError:
				index = 0
				palindromized.insert(len(palindromized) // 2, pattern[index])
		else:
			palindromized += [pattern[0]]
		
		if iteration % 2 != 0:
			index += 1
		
	return ''.join(palindromized)
		
		
print(palindromization("123", 9))


"""
For elements = "123" 
n = 2 => result = "11"
n = 3 => result = "121"
n = 4 => result = "1221"
n = 5 => result = "12321"
n = 6 => result = "123321"
n = 7 => result = "1231321"
n = 8 => result = "12311321"
n = 9 => result = "123121321"
n = 10=> result = "1231221321"
"""