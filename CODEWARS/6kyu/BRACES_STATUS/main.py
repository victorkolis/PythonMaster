#!/usr/bin/env python3

def braces_status(string):
	# Variable(s)
	braces = '{}()[]'
	new_string = ''
	
	# Single brace cases
	if string[0] == '}' or string[0] == ')' or string[0] == ']':
		return False
	elif string[len(string) - 1] == '{' or string[len(string) - 1] == '(' or string[len(string) - 1] == '[':
		return False
	
	# Removing any character other than braces
	else:
		for element in string:
			if element in braces:
				new_string += element
		
		# Removing braces pairs
		for element in new_string:
			new_string = new_string.replace('{}', '').replace('()', '').replace('[]', '')
		
		if len(new_string) > 0:
			return False
		else:
			return True
	
	
print(braces_status('[]'))

