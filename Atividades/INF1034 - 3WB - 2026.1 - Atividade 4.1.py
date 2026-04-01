from turtle import*
from time import sleep


#FUNÇÕES
def função1(x):
    return x**(1/2)

def função2(x):
    return 1/x

def função3(x):
    return 2**x

def função4(x):
    return 5 - x**2

def função5(x):
    return x**2 -5*x + 6

def função6(x):
    return x**3 - x**2 - x + 1

t = Turtle()

def planoCart():
    t.color('black')
    t.pu()
    t.goto(-300,0)
    t.pd()
    t.goto(300,0)
    t.stamp()
    t.pu()
    t.goto(0,-300)
    t.pd()
    t.goto(0,300)
    t.lt(90)
    t.stamp()
    t.rt(90)

# #EXECUÇÃO FUNÇÃO1
planoCart()
t.color('red')
t.pu()
t.goto(0, função1(0))
t.pd()
for x in range(0,101):
    t.goto(x, função1(x))
sleep(3)
t.clear()

#EXECUÇÃO FUNÇÃO2
planoCart()
t.color('red')
t.pu()
t.goto(-100, função2(-100))
t.pd()
for x in range(-99,0):
    t.goto(x, função2(x))
t.pu()
t.goto(1, função2(1))
t.pd()
for x in range(1,101):
    t.goto(x, função2(x))
sleep(3)
t.clear()

#EXECUÇÃO FUNÇÃO3
planoCart()
t.color('red')
t.pu()
t.goto(-100, função3(-100))
t.pd()
for x in range(-99,9):
    t.goto(x, função3(x))
sleep(3)
t.clear()

#EXECUÇÃO FUNÇÃO4
planoCart()
t.color('red')
t.pu()
t.goto(-10, função4(-10))
t.pd()
for x in range(-10,11):
    t.goto(x, função4(x))
sleep(3)
t.clear()

#EXECUÇÃO FUNÇÃO5
planoCart()
t.color('red')
t.pu()
t.goto(-10, função5(-10))
t.pd()
for x in range(-10,16):
    t.goto(x, função5(x))
sleep(3)
t.clear()

#EXECUÇÃO FUNÇÃO6
planoCart()
t.color('red')
t.pu()
t.goto(-5, função6(-5))
t.pd()
for x in range(-5,6):
    t.goto(x, função6(x))
sleep(3)
t.clear()



mainloop()