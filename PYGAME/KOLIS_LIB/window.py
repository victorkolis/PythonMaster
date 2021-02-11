#!/usr/bin/env python3

import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()  # Initiates pygame

pygame.display.set_caption('Simple Window')

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # Set/Initiate the window

# Game loop
while True:
	
	# Event loop
	for event in pygame.event.get():
		if event.type == QUIT:
			print(2)
			pygame.quit()
			sys.exit()
	
	pygame.display.update()
	clock.tick(24)
