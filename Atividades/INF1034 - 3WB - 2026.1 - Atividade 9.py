# EXEMPLO DE FUNÇÃO RECURSIVA

# def mostra_palavra_rec(palavra):
#     if palavra == '': #Sempre botar esse limite, senão da problema de recursão
#         return 
#     print(palavra)
#     mostra_palavra_rec(palavra[:-1])
#     print(palavra)

import turtle
from random import randint

def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

# Fácil
def drawTriFractal(t,tam):
    if tam < 10:
        return
    t.pd()
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(3):
        t.fd(tam)
        drawTriFractal(t,tam/2)
        t.lt(120)
    t.end_fill()

# Médio
# def draw 


t = turtle.Turtle()
turtle.colormode(255)
# t.speed("slowest")
t.speed(0)
t.pu()


t.goto(-100,0)
t.pd()
drawTriFractal(t,200)


turtle.mainloop()