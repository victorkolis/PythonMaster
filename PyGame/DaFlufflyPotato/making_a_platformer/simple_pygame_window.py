# simple_pygame_window

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("My Pygame Window")

WINDOW_SIZE = (400, 400)

# create the display
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    # Controls fps
    clock.tick(60)
