#!/usr/bin/env python3

# letters and its opposites are in a battle, the goal is to keep track of hits and who wins the battle

def alphabet_war(fight):
	left_side = {
		'w': 4,
		'p': 3,
		'b': 2,
		's': 1
	}
	
	right_side = {
		'm': 4,
		'q': 3,
		'd': 2,
		'z': 1
	}
	
	left_score = 0
	right_score = 0
	
	for letter in fight:
		if letter in left_side:
			try:
				left_score += left_side[letter]
			except KeyError:
				pass
			except TypeError:
				pass
		else:
			try:
				right_score += right_side[letter]
			except KeyError:
				pass
			except TypeError:
				pass

	result = left_score - right_score
	
	if result > 0:
		return 'Left side wins!'
	
	elif result < 0:
		return 'Right side wins!'
	
	elif result == 0:
		return 'Let\'s fight again!'


print(alphabet_war('z'))
