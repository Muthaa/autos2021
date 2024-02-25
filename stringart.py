from panel import *

DELAY = 100

def step(x):
	pt = [x, 0]
	draw (p1)
	delay(DELAY)
	draw(pB)
	delay(DELAY)
	p2 = [x + 1, 0]
	draw(p2)
	delay(DELAY)

make.panel(-10, 10, -10, 10)
pA = [0, 8]
pB = [0, 8]
move(pA)
for x in range(-9, 9, 2):
	step(x)