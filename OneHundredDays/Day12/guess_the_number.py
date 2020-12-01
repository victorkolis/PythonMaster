# guess_the_number.py

from random import randint

random_number = randint(1, 100)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
level = input("choose the difficulty. Type 'easy' or 'hard': ").lower()


if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
elif level == '':
    print('\n\nSUPER HARD MODE ACTIVATED!!!\n\n')
    attempts = 3
else:
    print('Invalid request!')
    attempts = 0

player_guess = ''

while player_guess != random_number and attempts > 0:
    print(f'You have {attempts} attempts.')
       
    try:
        player_guess = int(input('Make a guess: '))
    except ValueError:
        print('Enter a number!')
        break
        
    if player_guess > random_number:
        print('Too high!')
    elif player_guess < random_number:
        print('Too low!')
    
    if attempts == 0:
        print(f'Never mind. The number I was thinking of was {random_number}.')
        break
    
    elif player_guess == random_number:
        print('Good job!')
    attempts -= 1
