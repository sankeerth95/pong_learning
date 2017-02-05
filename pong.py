#blit: to draw on the screen.
#
#render() tells the program that screen is
#the canvas. All surfaces ae blit onto thiss canvas. 

import pygame
import sys

pygame.init()

bcgr = (0, 0, 0)

height = 480
width = 640
rod_clearance = 20

vrod = 4
v1 = [0, 0]
v2 = [0, 0]
vpuck = [2, 2]

screen = pygame.display.set_mode((width, height))



#puck = pygame.image.load("./assets/puck.jpg").convert()
stick1 = pygame.image.load("./assets/rod.jpg").convert()
stick1_rect = stick1.get_rect()
stick1_rect.x, stick1_rect.y = (width-rod_clearance, height/2)

stick2 = pygame.image.load("./assets/rod.jpg").convert()
stick2_rect = stick2.get_rect()
stick2_rect.x, stick2_rect.y = (rod_clearance, height/2)

puck = pygame.image.load("./assets/puck.png").convert()
puck_rect = puck.get_rect()
puck_rect.x, puck_rect.y = (width/2, height/2)

screen.fill(bcgr)
screen.blit(stick1, stick1_rect )
screen.blit(stick2, stick2_rect )
screen.blit(puck, puck_rect )

pygame.display.update()

key_status1 = {"K_UP" : False, "K_DN" : False}

#game loop
pygame.time.delay(2000)

while True:


	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				key_status1["K_DN"] = True
			if event.key == pygame.K_UP:
				key_status1["K_UP"] = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				key_status1["K_DN"] = False
			if event.key == pygame.K_UP:
				key_status1["K_UP"] = False

		if(not key_status1["K_UP"] and not key_status1["K_DN"]): v1[1] = 0
		if(key_status1["K_UP"] and key_status1["K_DN"]): v1[1] = 0
		if(key_status1["K_UP"] and not key_status1["K_DN"]): v1[1] = -vrod
		if(not key_status1["K_UP"] and key_status1["K_DN"]): v1[1] = vrod



	if(puck_rect.top < 0):
		vpuck[1] = abs(vpuck[1])
	if(puck_rect.bottom > height):
		vpuck[1] = -abs(vpuck[1])
	if(puck_rect.right > width-rod_clearance):
		vpuck[0] = -abs(vpuck[0])
	if(puck_rect.left < rod_clearance):
		vpuck[0] = abs(vpuck[0])


	if( (stick1_rect.top < 0 and key_status1["K_UP"]) or (stick1_rect.bottom > height and key_status1["K_DN"]) ):
		v1[1] = 0

	stick1_rect = stick1_rect.move(v1);
	stick2_rect = stick2_rect.move(v2);
	puck_rect = puck_rect.move(vpuck);

	screen.fill(bcgr)
	screen.blit(stick1, stick1_rect)
	screen.blit(puck, puck_rect)
	screen.blit(stick2, stick2_rect)

	pygame.display.update()
	pygame.time.delay(10)


