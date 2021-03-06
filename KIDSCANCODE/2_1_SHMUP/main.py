#!/usr/bin/env python3

# SHMUP

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
pygame.display.set_caption('SHMUP')
clock = pygame.time.Clock()

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((20, 20))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 20
		self.speedx = 0
		self.height = 0
		
	def update(self):
		# Setting the speed aways to stopped
		self.speedx = 0
		self.height = 0
		
		# Getting a list of all the keys that are being held down
		key_pressed = pygame.key.get_pressed()
		
		# Movin' sideways
		if key_pressed[pygame.K_LEFT]:
			self.speedx = -5
		elif key_pressed[pygame.K_RIGHT]:
			self.speedx = 5
		
		# Movin' up & down
		if key_pressed[pygame.K_UP]:
			# Increasing speed
			if key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]:
				self.height = -20
			else:
				self.height = -5
		elif key_pressed[pygame.K_DOWN]:
			self.height = 5
		
		self.rect.x += self.speedx
		self.rect.y += self.height
		
		
		# Collision detection
		


# SPRITES
sprites = pygame.sprite.Group()
ship = Ship()
sprites.add(ship)

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
	