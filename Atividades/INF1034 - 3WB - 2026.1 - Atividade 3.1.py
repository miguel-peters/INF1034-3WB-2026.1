from turtle import *
from random import randint

t = Turtle()

#FUNÇÃO DO TRIÂNGULO
def Draw1(x,y,tamanho,color):
    t.pu() 
    t.goto(x,y)
    t. pd() 
    t.color('black') 
    t.begin_fill() 
    t.fillcolor(color)
    for _ in range(3):
        t.fd(tamanho)
        t.lt(120)
    t.end_fill()

#FUNÇÃO DO PENTÁGONO
def Draw2(x,y,tamanho,color):
    t.pu() 
    t.goto(x,y)
    t. pd() 
    t.color('black') 
    t.begin_fill() 
    t.fillcolor(color)
    for _ in range(5):
        t.fd(tamanho)
        t.lt(72)
    t.end_fill()

#FUNÇÃO DO HEXÁGONO
def Draw3(x,y,tamanho,color):
    t.pu() 
    t.goto(x,y)
    t. pd() 
    t.color('black') 
    t.begin_fill() 
    t.fillcolor(color)
    for _ in range(6):
        t.fd(tamanho)
        t.lt(60)
    t.end_fill()

#FUNÇÃO DO OCTÓGONO
def Draw4(x,y,tamanho,color):
    t.pu() 
    t.goto(x,y)
    t. pd() 

    t.color('black') 
    t.begin_fill() 
    t.fillcolor(color)
    for _ in range(8):
        t.fd(tamanho)
        t.lt(45)
    t.end_fill()

#FUNÇÃO DO PLANO CARTESIANO
def PlanoCart():    
    t.pu() 
    t.goto(300,00)
    t. pd()
    t.stamp ()
    t.lt(180)
    t.fd(600)
    t.stamp ()
    t.pu() 
    t.goto(00,-300)
    t. pd() 
    t.lt(90)
    t.stamp()
    t.lt(180)
    t.fd(600)
    t.stamp()

#FUNÇÃO GENÉRICA
def DrawSqr(x, y, z, tamanho, ângulo, color):
    t.pu() 
    t.goto(x,y)
    t. pd() 
    t.color('black') 
    t.begin_fill() 
    t.fillcolor(color)
    for _ in range(z):
        t.fd(tamanho)
        t.lt(ângulo)
    t.end_fill()

#RANDOMIZAÇÃO DAS COORDENADAS
x1 = randint(100,300)
y1 = randint(100,300)
x2 = randint(-300,-100)
y2 = randint(100,300)
x3 = randint(-300,100)
y3 = randint(-300,-100)
x4 = randint(150,300)
y4 = randint(-300,-150)

#BLOCO PRINCIPAL
PlanoCart()
color = textinput('Obter cor', 'Digite a cor: ')
DrawSqr(x1,y1, 3, 100, 120, color)
color = textinput('Obter cor', 'Digite a cor: ')
DrawSqr(x2,y2, 5, 70, 72, color)
color = textinput('Obter cor', 'Digite a cor: ')
DrawSqr(x3,y3, 6, 70, 60, color)
color = textinput('Obter cor', 'Digite a cor: ')
DrawSqr(x4,y4, 8, 70, 45, color)

mainloop()