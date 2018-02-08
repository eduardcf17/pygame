import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg=pygame.image.load("paisaje.jpg").convert()
bgWidth,bgHeight=bg.get_rect().size

stageWidth= bgWidth*2
stagePosX=0

startScrollingPosX = HW

circleRadius=25
circlePosX=cicleRadius

playerPosX=circleRadius
playerPosX=585

playerVelocityX=0
# main loop
while True:
	events()
	k=pygame.key.get_pressed()
	if k[K_RIGHT]:
		playerVelocityX=1
	elif k[K_LEFT]:
		playerVelocityX=-1
	else:
		playerVelocityX=0
	
	playerPosX+=playerVelocityX
	if playerPosX>stageWidth-circleRadius:playerPosX=stageWidth-circleRadius
	pygame.draw.circle(DS,WHITE,(playerPosX,playerPosY-circleRadius),circleRadius,0)
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)
