#!/usr/bin/env python3

def result(p1, p2):
	p1 = p1.title()
	p2 = p2.title()
	
	elements = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
	
	if p1.isalpha() and p2.isalpha() and p1 in elements and p2 in elements:
		# Element = [defeats, defeats]
		rock = ['Scissor', 'Lizard']
		paper = ['Rock', 'Spock']
		scissor = ['Paper', 'Lizard']
		lizard = ['Spock', 'Paper']
		spock = ['Rock', 'Scissor']
		
		winner_1 = 'Player 1 won!'
		winner_2 = 'Player 2 won!'
		
		
		if p1 == p2:
			return 'Draw!'
		
		elif p1 == 'Rock':
			if p2 in rock:
				return winner_1
			else:
				return winner_2
		
		elif p1 == 'Paper':
			if p2 in paper:
				return winner_1
			else:
				return winner_2
		
		elif p1 == 'Scissor':
			if p2 in scissor:
				return winner_1
			else:
				return winner_2
		
		elif p1 == 'Lizard':
			if p2 in lizard:
				return winner_1
			else:
				return winner_2
		
		elif p1 == 'Spock':
			if p2 in spock:
				return winner_1
			else:
				return winner_2
		
	else:
		return 'Oh, Unknown Thing'
	
	
print(result('ra', 'ra'))
	
# rock > scissor and lizard
# paper > rock and spock
# scissor > paper and lizard
# lizard > spock and paper
# spock > rock and scissor
