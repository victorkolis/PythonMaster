import pygame
import sys
from pygame.locals import *

pygame.init()

SURFACE = pygame.display.set_mode((600, 600), 0 , 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 100)


# draw on the surface object
SURFACE.fill(WHITE)
pygame.draw.polygon(SURFACE, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))


pygame.draw.line(SURFACE, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(SURFACE, BLUE, (120, 60), (60, 120))
pygame.draw.line(SURFACE, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(SURFACE, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(SURFACE, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(SURFACE, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(SURFACE)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
