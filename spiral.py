import pyautogui
import time

time.sleep(5)
pyautogui.click()
distance = 300
while distance > 0:
	pyautogui.dragRel(distance, 0, 1, button="left")#distance to move with x as 400 and y disabled)
	disance = distance - 20 #reduces the distance for the time alloted
	pyautogui.dragRel(0, distance, 1, button="left")#for the y axis
	pyautogui.dragRel(-distance, 0, 1, button="left")#for they x
	distance = distance - 20
	pyautogui.dragRel(0, -distance, 1, button="left")#for the x