from PaintEngine import *
import keyboard
import random as ran

x=25

y_p=230

pipe_x=1050
pipe_y=0

def update():
	Clear()
	xs, ys=MousePos()

	draw_obj(pipe_x, 0, 80, 200+pipe_y, False)
	draw_obj(pipe_x, pipe_y+350, 80, 230-pipe_y, False)

	draw_obj(580, y_p, 50, 50, True)

	MouseSetPos(xs, ys)

PaintLoad()

while True:
	if keyboard.is_pressed('q'):
		y_p+=15
		pipe_x-=35
		update()

	if keyboard.is_pressed('w'):
		y_p-=50
		pipe_x-=35
		update()

	if pipe_x<x+150:
		pipe_x=1050
		pipe_y=ran.randint(-70, 150)

	if keyboard.is_pressed('esc'):
		Exit()