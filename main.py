n = int(input("nombre d'années :"))
import turtle
turtle.speed(0)
turtle.penup()
steps = 10
dist = 50

def drawHorn(x, y, n):
  if(n > 0):
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.forward(dist)
    p = turtle.pos()
    drawHorn(p[0], p[1], n - 1)
    turtle.pendown()
    turtle.left(180)
    turtle.forward(dist/2)
    turtle.left(210)
    turtle.forward(dist/2)
    p = turtle.pos()
    drawHorn(p[0], p[1], n - 1)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.right(30)

drawHorn(-200, 0, n)
