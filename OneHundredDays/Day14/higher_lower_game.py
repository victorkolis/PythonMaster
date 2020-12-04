# higher_lower_game.py
# AUTHOR : Victor Kolis
# This software objective is to figure out which artist's got the most followers on a given SNW


import art
import game_data
import random
import subprocess


print(art.logo)


def random_index():
    return random.randint(0, len(game_data.data) - 1)

# Clears the previous game/guess and reprints the logo
def game_reloader():
    subprocess.call('clear')
    print(art.logo)

game_reloader()
score = 0
game_is_on = True

# Gets an artist at random from the game_data list
artist_a = game_data.data[random_index()]

while game_is_on:
    
    print(f"Compare A: {artist_a['name']}, {artist_a['description']}, from {artist_a['country']}.")
    
    # Prints vs ascii
    print(art.vs)
    
    # Gets an artist at random from the game_data list and later compares to to the artist_a in order not to repeat the artists picked out
    artist_b = game_data.data[random_index()]
    if artist_a == artist_b:
        artist_b = game_data.data[random_index() + 1]
    print(f"Against B: {artist_b['name']}, {artist_b['description']}, from {artist_a['country']}.")
    
    
    player_guess = input('Who has more followers? Type \'A\' or \'B\': ').upper()
    
    if artist_a['follower_count'] > artist_b['follower_count']:
        greater_artist = 'A'
    else:
        greater_artist = 'B'
        artist_a = artist_b
    
    if player_guess == greater_artist:
        score += 1
        game_reloader()
        print(f'You\'re right! Current score: {score}')
    else:
        print(f'Sorry, that\'s wrong. Final score: {score}')
        break
