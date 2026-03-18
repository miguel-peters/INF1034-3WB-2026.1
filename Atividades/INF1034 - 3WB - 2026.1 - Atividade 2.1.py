from turtle import *

#desenhando um quadrado usando repetição
t = Turtle ()



#PLANO CARTESIANO
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

#FIGURAS GEOMÉTRICA 1

t.pu() 
t.goto(200,100)
t. pd() 

color = textinput('Obter cor', 'Digite a cor: ')
t.color('black') 
t.begin_fill() 
t.fillcolor(color)

for _ in range(3):
    t.fd(100)
    t.lt(120)
t.end_fill()

#FIGURA GEOMÉTRICA 2

t.pu() 
t.goto(-100, 100)
t. pd() 

color = textinput('Obter cor', 'Digite a cor: ')
t.color('black') 
t.begin_fill() 
t.fillcolor(color)

for _ in range (5):
    t.fd(70)
    t.lt(72)
t.end_fill()

#FIGURA GEOMÉTRICA 3

t.pu() 
t.goto(-100, -200)
t. pd() 

color = textinput('Obter cor', 'Digite a cor: ')
t.color('black') 
t.begin_fill() 
t.fillcolor(color)

for _ in range (6):
    t.fd(70)
    t.lt(60)
t.end_fill()

#FIGURA GEOMÉTRICA 4
t.pu() 
t.goto(200, -200)
t. pd() 

color = textinput('Obter cor', 'Digite a cor: ')
t.color('black') 
t.begin_fill() 
t.fillcolor(color)

for _ in range (8):
    t.fd(70)
    t.lt(45)
t.end_fill()

t.pu() 
t.goto(300, -200)
t. pd() 

t.color('black') 

for i in range (30):
    t.fd (i*2)
    t.left(45)

mainloop()


