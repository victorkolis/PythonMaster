import pygame
import sys
from pygame.locals import *

pygame.init()

SURFACE = pygame.display.set_mode((800, 600)).convert_alpha()
pygame.display.set_caption('convert_alpha() method')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
