#!/usr/bin/env python3

import random


def ask_number(min_number, max_number):
	counter = 0
	try:
		while True:
			if counter == 4:
				print(f'Game Over!\nTry Again!\nThe Magic Number Was {magic_number}')
				break
				
			users_guess = int(input(f'What is the number between {min_number} and {max_number}? '))
			if users_guess == magic_number:
				print('Correctamundo!')
				break
			elif users_guess > magic_number:
				print('Higher')
			else:
				print('Lower')
				
			print('Try again')
			counter += 1
	except ValueError:
		print('Enter A Whole Number!')
		return -1
		
	return 0

MIN_NUMBER = 1
MAX_NUMBER = 10
magic_number = random.randint(MIN_NUMBER, MAX_NUMBER)


ask_number(MIN_NUMBER, MAX_NUMBER)
