#!/usr/bin/env python3

import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()  # Initiates pygame

pygame.display.set_caption('Simple Window')

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # Set/Initiate the window

#PLAYER
# Loads the image into the code
player = pygame.image.load('kolis.png')

# Player location
player_location = [50, 50]


moving_left = False
moving_right = False


# Game loop
while True:
	screen.fill((0, 0, 0))
	
	
	# Set player onto the screen
	screen.blit(player, player_location)
	
	
	if moving_right == True:
		player_location[0] += 10
		
	if moving_left == True:
		player_location[0] -= 10
	
	# Event loop
	for event in pygame.event.get():
		if event.type == QUIT:
			print(2)
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				moving_right = True
			if event.key == K_LEFT:
				moving_left = True
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				moving_right = False
			if event.key == K_LEFT:
				moving_left = False
	
	
	pygame.display.update()
	clock.tick(24)
	