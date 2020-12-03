# higher_lower_game.py

import art
import game_data
import random
import subprocess


#(01 - Print the logo import the art)#################
print(art.logo)
# You're right! Current score: [] current_score += 1


#02 - Print the first comparison. Which is a data from the game_data.py
    # Compare A: Dictionary data Random number

# Generates a random number in order to get a random artist from the game_data.data dicionary

def random_index():
    return random.randint(0, len(game_data.data) - 1)



on = True

while on:
    artist_a = game_data.data[random_index()]
    print(f"Compare A: {artist_a['name']}, {artist_a['description']}, from {artist_a['country']}.")

    print(art.vs)
    artist_b = game_data.data[random_index()]
    if artist_a == artist_b:
        artist_b = game_data.data[random_index() + 1]
    print(f"Against B: {artist_b['name']}, {artist_b['description']}, from {artist_a['country']}.")
    break






#03 - Print the VS (import the art)

    
#04 - Print the second comparison. Which is another data from the game_data.py
    # Against B: Dictionary data - Random number


#05 - Input:
    # Who has more followers? Type 'A' or 'B':
    # If the guess is wrong print: Sorry, that's wrong. Final score: 0
    # If the guess is correct clean the screen and start  afresh with the previously compared

# Clears the previous game/guess and reprints the logo
def game_reloader():
    subprocess.call('clear')
    print(art.logo)
