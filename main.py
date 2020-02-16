import turtle

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

def drawHorn(x, y, n, pos=[], a=0):
  if(n > 0):
    turtle.setpos(x, y)
    turtle.seth(a)
    turtle.pendown()
    turtle.forward(dist)
    pos.append((turtle.pos(), turtle.heading()))
    turtle.pendown()
    turtle.left(180)
    turtle.forward(dist/2)
    turtle.left(210)
    turtle.forward(dist/2)
    pos.append((turtle.pos(), turtle.heading()))
    turtle.penup()
    turtle.setpos(x, y)
    turtle.right(30)
    return pos

mutant = input("mutant ?")
if mutant == "oui":
	n = int(input("nombre d'annees :"))
	turtle.speed(0)
	turtle.penup()
	steps = 10
	dist = 30
	draw_fractal(-250, 0, 8)
else:
	n = int(input("nombre d'annees :"))
	turtle.speed(0)
	turtle.penup()
	dist = 50
	pos = drawHorn(-200, 0, n)
	for j in range(n - 2):
		posn = []
		for i in pos:
			posn = posn + drawHorn(i[0][0], i[0][1], 1, [], i[1])
		pos = posn

