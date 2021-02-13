#!/usr/bin/env python3

# Pygame template - delete this line

import pygame
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
DARK_GRAY = (110, 110, 110)

# Initializes pygame and create a window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GAME TITLE')
clock = pygame.time.Clock()

# Game loop
while True:
	screen.fill(DARK_GRAY)
	
	