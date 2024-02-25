import pygame
import random
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255,255,255]
WIDTH = 1200
HEIGHT = 650
screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.RESIZABLE)
pygame.display.set_caption("SNOWFALL")

snowFall = []
for i in range(1200):
	x = random.randrange(0, 1200)
	y = random.randrange(0, 650)
	snowFall.append([x, y])

clock = pygame.time.Clock()
done = False
while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(BLACK)

	for i in range(len(snowFall)):
		pygame.draw.circle(screen, WHITE, snowFall[i], 2)

		snowFall[i][1] += 1
		if snowFall[i][1] > 1200:
			y = random.randrange(-50, -10)
			snowFall[i][1] = y
		
			x = random.randrange(0, 1200)
			snowFall[i][0] = x

	pygame.display.flip()
	clock.tick(45)
pygame.quit()
