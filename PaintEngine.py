import pyautogui
import os
import time
import mouse

min_x=25
min_y=164
sW, sH = pyautogui.size()
max_x=sW-23
max_y=sH-200

def PaintLoad():
	os.system('start mspaint.exe 1.png')
	time.sleep(1)
	pyautogui.hotkey('win', 'up')
	pyautogui.click(175, 72)
	time.sleep(0.1)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')

def draw_obj(x0, y0, x_s, y_s, fill):
	if min_x>x0+min_x or x0>max_x or min_y>y0+min_y or y0>max_y:
		pyautogui.alert('Error the object is not included in the Paint frame "draw_obj()"')
		Exit()
	pyautogui.click(525, 63)
	pyautogui.moveTo(min_x+x0, min_y+y0)
	pyautogui.dragTo(min_x+x0+x_s, min_y+y0+y_s, duration=0.001)
	pyautogui.click(min_x-3, min_y-3)
	if fill: 
		pyautogui.click(360, 71)
		pyautogui.click((min_x+x0)+(x_s/2), (min_y+y0)+(y_s/2))

def Clear():
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.hotkey('esc')

def Exit():
	pyautogui.hotkey('alt', 'f4')
	pyautogui.hotkey('right')
	pyautogui.hotkey('enter')
	os._exit(0)

def MousePos():
	return pyautogui.position()

def MouseLeftClick():
	return mouse.is_pressed(button='left')

def MouseRightClick():
	return mouse.is_pressed(button='right')

def MouseMiddleClick():
	return mouse.is_pressed(button='middle')

def MouseSetPos(x1, y1):
	pyautogui.moveTo(x1, y1)

def draw_text(xT, yT, text):
	pyautogui.click(381, 71)
	pyautogui.click(min_x+xT, min_y+yT)
	pyautogui.write(text, interval=0.01)
	pyautogui.click(92, 35)
	pyautogui.click(525, 63)