#n = int(input("nombre d'annees :"))
n = 6
import turtle
turtle.speed(0)
turtle.penup()
steps = 10
dist = 100

def draw_fractal(x, y, n, a=0):
	turtle.penup()
	turtle.setpos(x, y)
	turtle.seth(a)
	if n == 1:
    	turtle.pendown()
		turtle.forward(forward)
		turtle.penup()
	if n == 2:
    	turtle.pendown()
		turtle.forward(dist/4)
	draw_fractal(x, y, n - 1)
	draw_fractal(x, y, n - 2)

draw_fractal(0, 0, 3)