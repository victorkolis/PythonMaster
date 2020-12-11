# Pygame has two ways to represent rectangular areas
# 1. XY Width in pixels Height in pixels
# 2. pygame.Rect()

import pygame

rect1 = (10, 40, 60, 60)
rect2 = pygame.Rect(10, 40, 60, 60)

print(rect1 == rect2)

# The advantageous thing about a pygame.Rect is it automatically calculates the coordinates\
# for other features of the rectangle

"""
The Pygame code for the Rect object automatically calculated that if the left
edge is at the X coordinate 10 and the rectangle is 200 pixels wide,
then the right edge must be at the X coordinate 210.
If you reassign the right attribute, all the other attributes are automatically recalculated
"""

