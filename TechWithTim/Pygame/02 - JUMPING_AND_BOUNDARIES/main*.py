#!/usr/bin/env python3

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Character actions and attributes
character_x_pos = 50
character_y_pos = 50
character_width = 50
character_height = 50
character_moving_speed = 20
is_jump = False

while True:
	screen.fill((0, 0, 0))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	# Handlig key events
	keys = pygame.key.get_pressed()
	
	
	if keys[K_LEFT] and character_x_pos > character_moving_speed:
		character_x_pos -= character_moving_speed
	if keys[K_RIGHT] and character_x_pos < SCREEN_WIDTH - character_width:
		character_x_pos += character_moving_speed
	if not is_jump:
		if keys[K_UP] and character_y_pos > character_moving_speed:
			character_y_pos -= character_moving_speed
		if keys[K_DOWN] and character_y_pos < SCREEN_HEIGHT - character_height:
			character_y_pos += character_moving_speed
		if keys[K_SPACE]:
			is_jump = True
	else:
		if character_y_pos > 10:
			character_y_pos += -20 ** 2
		is_jump = False
		
	# Character creation
	pygame.draw.rect(screen, (255, 255, 255), (character_x_pos, character_y_pos, character_width, character_height))
	
	
	pygame.display.update()
	clock.tick()
	