#!/usr/bin/env python3

import pygame
import sys
import random
import os
from pygame.locals import *


WIDTH, HEIGHT = 720, 720
FPS = 24

# Set up assets
game_folder = os.path.dirname(__file__)

# Common colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
DARK_GRAY = (30, 30, 30)


class Player(pygame.sprite.Sprite):
	# Sprite for the Player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH * 0.5, HEIGHT * 0.5)
	
	def update(self):
		self.rect.x += 20
		if self.rect.left > WIDTH:
			self.rect.right = 0

# Initializes pygame and create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GAME TITLE')
clock = pygame.time.Clock()

# Sprites
sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)

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
	sprites.update()
	
	# 3. Draw/Render
	screen.fill(BLACK)
	sprites.draw(screen)
	
	# Board
	pygame.display.flip()
