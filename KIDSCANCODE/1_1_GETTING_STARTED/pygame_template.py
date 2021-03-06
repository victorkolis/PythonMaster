#!/usr/bin/env python3

# Pygame template - delete this line

import pygame
import sys
import random
from pygame.locals import *

import random

WIDTH, HEIGHT = 360, 480
FPS = 24

# Common colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
DARK_GRAY = (30, 30, 30)
DARK_GRAY = (110, 110, 110)

# Initializes pygame and create a window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GAME TITLE')
clock = pygame.time.Clock()

# SPRITES
all_sprites = pygame.sprite.Group()

# Game loop
# Game loop
while True:
	# keeping the loop within the correct speed
	clock.tick(FPS)
	
	# 1. Process input (events)
	for event in pygame.event.get():
		# check for window closure
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	# 2. Update
	all_sprites.update()
	
	# 3. Draw/Render
	screen.fill(BLACK)
	all_sprites.draw(screen)
	
	# Board
	pygame.display.flip()
	