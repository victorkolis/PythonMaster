#!/usr/bin/env python3

# Replace the heads of chuck norris opponents for an empty space _O_ -> _ _

def head_smash(arr):
	if type(arr) == int:
		return 'This isn\'t the gym!!'
	
	elif not any(arr):
		return 'Gym is empty'
	else:
		for index, element in enumerate(arr):
			arr[index] = element.replace('O', ' ')
			
		return arr
	

print(head_smash(
	[
		'*****************************************',
		'**  _O_   *   _O_   *   _O_   *   _O_  **',
		'** /(.)J  *  C(.)J  *  /(.)J  *  C(.)J **',
		'** _| |_  *  _| |_  *  _( )_  *  _( )_ *']
))
