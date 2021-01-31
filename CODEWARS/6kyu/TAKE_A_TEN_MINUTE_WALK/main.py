#!/usr/bin/env python3

# Each direction is worth one minute (w, e, s, n)
# Calculate a route that takes you some place and take
# you back no longer than 10 minutes. (GPS, DIRECTIONS)
# Return True if walk is valid, otherwise False.

def is_valid_walk(walk: list) -> bool:
	# Declaring and treating variables
	walk.sort()
	walk_set = set(walk)
	walk_dictionary = {'n': 0, 's': 0, 'w': 0, 'e': 0}
	
	# Logic 1 - Creating a dicitionary for the latter comparison
	for element in walk_set:
		walk_dictionary[element] = walk.count(element)
	
	# If the length of the instructions is greater than 10 there is no need to verify the rest
	if len(walk) != 10:
		return False
	else:
		if walk_dictionary['n'] - walk_dictionary['s'] == 0 and walk_dictionary['w'] - walk_dictionary['e']  == 0 :
			return True
		else:
			return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
