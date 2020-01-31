#n = int(input("nombre d'annees :"))
import turtle
turtle.speed(0)
turtle.penup()
steps = 10
dist = 100

def drawSmall(x, y, a=0):
  turtle.setpos(x, y)
  turtle.seth(a)
  turtle.pendown()
  turtle.forward(dist/4)
  turtle.backward(dist/4)
  turtle.left(30)
  turtle.forward(dist/4)
  turtle.backward(dist/4)
  turtle.right(30)
  turtle.penup()
  return(0)

def drawLarge(x, y, a=0)
  turtle.setpos(x, y)
  turtle.seth(a)
  turtle.pendown()

def drawHorn(x, y, pos=[], a=0):
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

drawSmall(0, 0)
drawHorn(dist/4, 0)

#pos = drawHorn(-200, 0, n)
#for j in range(n):
#  posn = []
#  for i in pos:
#    posn = posn + drawHorn(i[0][0], i[0][1], 1, [], i[1])
#  pos = posn
