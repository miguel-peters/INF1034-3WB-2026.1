import turtle
from random import randint


def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))


def drawSquare(t, size):
  # t.goto(x, y)
  t.pd()
  t.begin_fill()
  t.fillcolor(randomColor())
  for i in range(4):
    t.fd(size)
    t.right(90)
  t.end_fill()
  t.pu()


def drawSquareFractal(t, size, step=50):
  if step < 0 or size < 1:
    return
  t.pd()
  t.fd(size / 1.5)
  t.lt(10)
  drawSquare(t, size)
  drawSquareFractal(t, size - 1, step - 1)


def drawSpiral(t):
  for i in range(100):
    t.fd(i)
    t.lt(15)


def drawStarFractal(t, size):
  if size < 10:
    return
  for i in range(5):
    t.fd(size)
    drawStarFractal(t, size / 3)
    t.lt(216)


def treeFractal(t, size, angle, nivel):
  if size < 40:
    return
  t.pd()
  t.fd(size)

  # right tree
  t.rt(angle)
  t.fd(size)
  treeFractal(t, size * 0.8, angle, nivel - 1)
  t.back(size)

  turtle.pencolor(0, 255 // nivel, 0)

  # left tree
  t.lt(2 * angle)
  t.fd(size)
  treeFractal(t, size * 0.8, angle, nivel - 1)
  t.back(size)

  turtle.pencolor(0, 255 // nivel, 0)
  t.lt(-angle)
  t.back(size)


t = turtle.Turtle()
turtle.colormode(255)
# t.speed("slowest")
t.speed(0)
t.pu()

# # Desenhando o "chifre"
# t.goto(-100, -200)
# t.pd()
# drawSquareFractal(t, 70, 60)

# # Desenhando a estrela
# t.goto(-100, 0)
# t.pd()
# drawStarFractal(t, 200)

# Desenhando a árvore
t.goto(0, -200)
t.lt(90)
treeFractal(t, 80, 40, 20)

# # Desenhando uma espiral
# drawSpiral(t)

turtle.mainloop()
