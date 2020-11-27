# my_game.py
# NYF (NOT YET FINISHED)

import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("The Legend Of Kolis")

WINDOW_SIZE = (400, 400)

# create the display
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# loads an image into the screen
player_image = pygame.image.load("kolis.png")

moving_right = False
moving_left = False

# sets the loaded image position
player_location = [0, 0]


player_y_momentum = 0

# loops infinitely do keep the window up
while True:
    screen.fill((0, 0, 0))
    
    # rerenders image after a keystroke move
    screen.blit(player_image, player_location)
    
    # bouncing gravity like
    if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    
    # player moves
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
    
    # quiting
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() # it is a better alternative than breaking or changing the condiiton to False
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            moving_right = True
        if event.key == K_LEFT:
            moving_left = True
    if event.type == KEYUP:
        if event.key == K_RIGHT:
            moving_right = False
        if event.key == K_LEFT:
            moving_left = False
            
    
    pygame.display.update() # updates display
    clock.tick(60) # controls fps
