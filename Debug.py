from PaintEngine import *
import keyboard
import random as ran

PaintLoad()

draw_obj(50, 20, 20, 20, False)
draw_text(100, 29, 'sas')

while True:
	if MouseLeftClick():
		x, y=MousePos()
		if x>500:
			print(True)

	if keyboard.is_pressed('space'):
		x, y=MousePos()
		print(f'{x}, {y}')

	if keyboard.is_pressed('r'):
		Clear()

	if keyboard.is_pressed('esc'):
		Exit()