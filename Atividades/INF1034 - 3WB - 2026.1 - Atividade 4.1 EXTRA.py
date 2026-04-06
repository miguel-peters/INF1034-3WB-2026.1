from random import randint, choice
from turtle import*

# Corrida de Tartarugas
def corridaTurtle(n):
    lista = []
    cores = ['red', 'blue', 'black', 'yellow']
    for i in range(n):
        lista.append(Turtle())
        lista[i].shape("turtle")
        lista[i].speed(1)
        lista[i].pu()
        lista[i].color(choice(cores))
        lista[i].goto(-200, 50 * i)
    for num in range(30):
        for i in range(n):
            lista[i].fd(randint(5, 10))
 
corridaTurtle(3)
