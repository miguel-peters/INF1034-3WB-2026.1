# EXEMPLO DE FUNÇÃO RECURSIVA

# def mostra_palavra_rec(palavra):
#     if palavra == '': #Sempre botar esse limite, senão da problema de recursão
#         return 
#     print(palavra)
#     mostra_palavra_rec(palavra[:-1])
#     print(palavra)

import turtle
from random import randint
from time import sleep

def randomColor(): #Essa função randomiza a cor que será preenchida em cada forma geométrica
  return (randint(0, 255), randint(0, 255), randint(0, 255))

# Fácil
def drawTriFractal(t,tam):
    if tam < 10:
        return # Para a função quando o tamanho for menor que 10
    t.pd()
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(3): # Cria um triângulo usando o tamanho divido por 2, e faz isso sucessivamente por meio da recursão
        t.fd(tam)
        drawTriFractal(t,tam/2)
        t.lt(120)
    t.end_fill()

# Médio
def drawSquare(t, size):
  t.pd()
  t.begin_fill()
  t.fillcolor(randomColor())
  for i in range(5): # Cria um pentágono
    t.fd(size)
    t.right(108)
  t.end_fill()
  t.pu()

def drawSquareFractal(t, size, step=50):
  if step < 0 or size < 1:
    return
  t.pd()
  t.fd(size / 1.5)
  t.lt(10)
  drawSquare(t, size) # Utiliza a função para criar um pentágono
  drawSquareFractal(t, size - 1, step - 1) # Repete os código acima com um tamanho menor que o apresentado

# Difícil
def treeFractal(t, size, angle, nivel):
    if size < 40: # Caso base para a ocorrência a função
        return
    t.pd()
    t.fd(size)

    # right tree
    t.rt(angle)
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size) # Cria o ramo direito da árvore

    turtle.pencolor(0, 255 // nivel, 0)

    # left tree
    t.lt(2 * angle)
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size) # Cria o ramo esquerdo da árvore

    turtle.pencolor(0, 255 // nivel, 0)
    t.lt(-angle)
    t.back(size)

    # middle tree
    t.fd(size)
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size) # Cria o ramo do meio da árvore, que fica tanto na parte direita como na esquerda

    turtle.pencolor(0, 255 // nivel, 0)
    
t = turtle.Turtle()
turtle.colormode(255)
# t.speed("slowest")
t.speed(0)
t.pu()

# Fácil
t.goto(-100,0)
t.pd()
drawTriFractal(t,200)
sleep(3)
t.clear()


# Médio
t.goto(-100,0)
t.pd()
drawSquareFractal(t, 100, 90)
sleep(3)
t.clear()

# Difícl
t.goto(0, -200)
t.pd()
t.lt(90)
treeFractal(t, 80, 40, 20)
sleep(3)
t.clear()

turtle.mainloop()