import random

start, end = 1, 10
entered_number = -1
secret_number = str(random.randint(start, end))

print(f'I am thinking of a number between {start} and {end}')
while entered_number != secret_number:
    entered_number = input('Type in your guess: ')
