from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
import keyboard
from numpy import *

replaybtn = (684, 390)
dinasour = (139, 431)

def restartGame():
	pyautogui.click(replaybtn)
	print("clicked play")

def image_grab():
	box = (dinasour[0]+55, dinasour[1], dinasour[0]+145, dinasour[1]+5)
	image = ImageGrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	a = array(grayImage.getcolors())
	#print(a.sum())
	return a.sum()
	if(a.sum() !=483):
		pressSpace()
		time.sleep(0.1)

def pressSpace():
	time.sleep(0.1)
	pyautogui.keyDown('space')

time.sleep(4)
restartGame()

while True:
	image_grab()
	