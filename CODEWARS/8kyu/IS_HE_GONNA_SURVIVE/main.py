#!/usr/bin/env python3

# Each dragon takes 2 bullets to kill

def hero(bullets, dragons):
	return bullets / 2 >= dragons


print(hero(10, 5))
