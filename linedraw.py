import pyautogui
import time

time.sleep(5)
pyautogui.click()
distance = 400
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.2)#distance to move with x as 400 and y disabled)
	disance = distance - 50 #reduces the distance for the time alloted
	pyautogui.dragRel(0, distance, duration=0.2)#for the y axis
	pyautogui.dragRel(-distance, 0, duration=0.2)#for they x
	distance = distance - 50
	pyautogui.dragRel(0, -distance, duration=0.2)#for the x