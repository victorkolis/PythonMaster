# Guess the game

import random as get


name = input("What is your name?\n")
print(f"Hi {name}, I am thinking of a number betwixt 1 - 10,")

random_number = get.randint(1, 10)

counter = 0

try:    
    while counter < 6:
        player_input = int(input("Take a guess: "))
        
        if player_input == random_number:
            counter += 1
            print(f"Good job, it took you {counter} guesses.")
            break                       
            
        elif counter == 5:
            print(f"Never mind, the number I was thinking of is {random_number}")
            break
        
        elif player_input > random_number:
            print("Too high.")
        
        elif player_input < random_number:
            print("Too low.")
            
        counter += 1
except ValueError:
    print("You need to enter an integer.")