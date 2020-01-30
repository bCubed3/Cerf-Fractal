n = 7
import turtle
turtle.speed(0)
turtle.penup()
steps = 10
dist = 50

def drawHorn(x, y, n, a=0):
  if(n > 0):
    pos = []
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.forward(dist)
    pos.append(turtle.pos())
    turtle.pendown()
    turtle.left(180)
    turtle.forward(dist/2)
    turtle.left(210)
    turtle.forward(dist/2)
    pos.append(turtle.pos())
    turtle.penup()
    turtle.setpos(x, y)
    turtle.right(30)
    px = pos[0][0]
    py = pos[0][1]
    drawHorn(px, py, n - 1, turtle.towards(px, py))
    px = pos[1][0]
    py = pos[1][1]
    drawHorn(px, py, n - 1, turtle.towards(px, py))

drawHorn(-200, 0, n)
