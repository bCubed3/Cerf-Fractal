n = int(input("nombre d'annees :"))
import turtle
turtle.speed(0)
turtle.penup()
steps = 10
dist = 30

def draw_fractal(x, y, n, a=0):
	turtle.setpos(x, y)
	if n == 1:
		turtle.pendown()
		turtle.forward(dist)
		turtle.penup()
		return turtle.pos()
	if n == 2:
		draw_fractal(x, y, 1)
		turtle.pendown()
		turtle.left(45)
		turtle.forward(dist / 3)
		turtle.backward(dist / 3)
		turtle.right(45)
		turtle.forward(dist / 3)
		turtle.penup()	
		return turtle.pos()
	if n > 2:
		p = draw_fractal(x, y, n - 1)
		turtle.left(45)
		draw_fractal(p[0], p[1], n - 2)
		turtle.right(45)
		draw_fractal(p[0], p[1], n - 2)
		return turtle.pos()


draw_fractal(-250, 0, 8)