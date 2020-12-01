import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 500))
pygame.display.set_caption('2D Pixel Calculator')
background_image = pygame.image.load('background-scheme.png')
background_location = [0, 0]
while True:
    DISPLAYSURF.blit(background_image, background_location)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
