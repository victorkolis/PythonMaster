#!/usr/bin/env python3

import pygame
import sys
import random
from pygame.locals import *

WIDTH, HEIGHT = 720, 720
FPS = 24

# Common colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
DARK_GRAY = (30, 30, 30)
YELLOW = (255, 255, 0)


class Player(pygame.sprite.Sprite):
    # Sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))  # Must have self.image
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()  # Must have self.rect
        self.rect.center = (WIDTH * 0.5, HEIGHT * 0.5)
        self.player_speed = 10

    def update(self):
        self.rect.x += self.player_speed
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Initializes pygame and create a window
pygame.init()
pygame.mixer.init()  # For audios
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GAME TITLE')
clock = pygame.time.Clock()

# Sprites
sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)  # Adding the player to the group of sprites

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
