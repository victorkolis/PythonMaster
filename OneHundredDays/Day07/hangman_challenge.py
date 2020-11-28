# hangman_challenge.py

import random

print('''

|  |  /\  |\  | /~~\|\  /|  /\  |\  |
|--| /__\ | \ ||  __| \/ | /__\ | \ |
|  |/    \|  \| \__/|    |/    \|  \|
                                     
''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# list to be used for random collection
colors = ['blue', 'black', 'brown', 'beige', 'birch', 'purple', 'orange', 'white', 'gray', 'green', 'red', 'indigo', 'yellow']

# variables (for better visual search only comment)
random_word = random.choice(colors)
blank_list = []
player_has_already_entered = []
lives = 6

for _ in range(len(random_word)):
    blank_list += "_"


while "_" in blank_list and lives > 0:
    print(f"\n\n{blank_list}")
    player_input = input("\nGuess a letter: ").lower()


    for index in range(len(random_word)):
        if player_input[0] == random_word[index]:
            blank_list[index] = random_word[index]
    if not player_input in random_word:
        lives -= 1
        print(stages[lives])
    
    if not "_" in blank_list:
        print("You win!")
    elif lives == 0:
        print("You lose!")

print(f"\nRandom word was {random_word}")
