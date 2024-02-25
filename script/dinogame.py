from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
import keyboard
from numpy import *

replaybtn = (684, 394)
dinasour = (137, 432)

def restartGame():
	pyautogui.click(replaybtn)
	print("clicked play")

def image_grab():
	box = (dinasour[0]+55, dinasour[1], dinasour[0]+145, dinasour[1]+5)
	image = ImageGrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	a = array(grayImage.getcolors())
	return a.sum() 

def pressSpace():
	time.sleep(0.1)
	pyautogui.keyDown('space')

time.sleep(5)
restartGame() 

while True:
	image_grab()
	if(image_grab() !=483):
		pressSpace()
		time.sleep(0.1)