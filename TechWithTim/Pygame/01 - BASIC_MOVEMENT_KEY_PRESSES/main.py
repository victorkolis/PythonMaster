import pygame, sys
from pygame.locals import *
clock = pygame.time.Clock()

pygame.init()


WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Game Of Mine')

# Character's dimension and position
x = 50
y = 50
width = 50
height = 50
velocity = 20


while True:
	# Refilling the screen every iteration
	window.fill((0, 0, 0))
	
	# Checking for events
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT]:
		x -= velocity
	
	if keys[pygame.K_RIGHT]:
		x += velocity
		
	if keys[pygame.K_UP]:
		y -= velocity
		
	if keys[pygame.K_DOWN]:
		y += velocity
	
	# Character creation
	pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))

	
	pygame.display.update()
	clock.tick(24)
	