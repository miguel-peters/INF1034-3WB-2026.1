from turtle import *
from time import sleep


def Draw_rect1(x,y,alt,larg,cor):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color('black') 
    t.begin_fill() 
    t.fillcolor(cor)
    t.fd(alt)
    t.lt(90)
    t.fd(larg)
    t.lt(90)
    t.fd(alt)
    t.lt(90)
    t.fd(larg)
    t.lt(90)
    t.end_fill()

def Draw_rect2(x,y,larg,alt,cor):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color('black') 
    t.begin_fill() 
    t.fillcolor(cor)
    for _ in range(2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()


def Draw_circle(x,y,raio,cor):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color('black') 
    t.begin_fill() 
    t.fillcolor(cor)
    t.rt(90)
    t.circle(raio)
    t.end_fill()

def indonésia():
    Draw_rect1(00,00,300,100,'white')
    Draw_rect2(00,100,300,100,'red')
    sleep(3)
    t.clear()

def japao():
    Draw_rect2(00,00,300,200,'white')
    Draw_circle(100,100,50,'red')
    t.lt(90)
    sleep(3)
    t.clear()

def india():
    Draw_rect2(00,00,300,100,'green')
    Draw_rect2(00,100,300,100,'white')
    Draw_rect2(00,200,300,100,'orange')
    Draw_circle(120,150,40,'orange')
    t.lt(90)
    sleep(3)
    t.clear()

def EAU():
    Draw_rect2(00,00,300,100,'black')
    Draw_rect2(00,100,300,100,'white')
    Draw_rect2(00,200,300,100,'green')
    Draw_rect2(00,00,100,300,'red')
    sleep(3)
    t.clear()

def russia():
    Draw_rect2(00,00,300,65,'red')
    Draw_rect2(00,65,300,65,'blue')
    Draw_rect2(00,130,300,65,'white')
    sleep(3)
    t.clear()

def ucrania():
    Draw_rect2(00,00,300,100,'yellow')
    Draw_rect2(00,100,300,100,'blue')
    sleep(3)
    t.clear()

def armenia():
    Draw_rect2(00,00,300,65,'orange')
    Draw_rect2(00,65,300,65,'blue')
    Draw_rect2(00,130,300,65,'red')
    sleep(3)
    t.clear()

def alemanha():
    Draw_rect2(00,00,300,65,'yellow')
    Draw_rect2(00,65,300,65,'red')
    Draw_rect2(00,130,300,65,'black')
    sleep(3)
    t.clear()

def holanda():
    Draw_rect2(00,00,300,65,'blue')
    Draw_rect2(00,65,300,65,'white')
    Draw_rect2(00,130,300,65,'red')
    sleep(3)
    t.clear()

def lituania():
    Draw_rect2(00,00,300,65,'red')
    Draw_rect2(00,65,300,65,'green')
    Draw_rect2(00,130,300,65,'yellow')
    sleep(3)
    t.clear()

def polonia():
    Draw_rect2(00,00,300,100,'red')
    Draw_rect2(00,100,300,100,'white')
    sleep(3)
    t.clear()

def bulgaria():
    Draw_rect2(00,00,300,65,'red')
    Draw_rect2(00,65,300,65,'green')
    Draw_rect2(00,130,300,65,'white')
    sleep(3)
    t.clear()

def yemen():
    Draw_rect2(00,00,300,65,'black')
    Draw_rect2(00,65,300,65,'white')
    Draw_rect2(00,130,300,65,'red')
    sleep(3)
    t.clear()

def bolivia():
    Draw_rect2(00,00,300,65,'yellow')
    Draw_rect2(00,65,300,65,'green')
    Draw_rect2(00,130,300,65,'red')
    sleep(3)
    t.clear()

def hungria():
    Draw_rect2(00,00,300,65,'green')
    Draw_rect2(00,65,300,65,'white')
    Draw_rect2(00,130,300,65,'red')
    sleep(3)
    t.clear()

def gabao():
    Draw_rect2(00,00,300,65,'blue')
    Draw_rect2(00,65,300,65,'yellow')
    Draw_rect2(00,130,300,65,'green')
    sleep(3)
    t.clear()

def serraleoa():
    Draw_rect2(00,00,300,65,'blue')
    Draw_rect2(00,65,300,65,'white')
    Draw_rect2(00,130,300,65,'green')
    sleep(3)
    t.clear()

def austria():
    Draw_rect2(00,00,300,65,'red')
    Draw_rect2(00,65,300,65,'white')
    Draw_rect2(00,130,300,65,'red')
    sleep(3)
    t.clear()

t = Turtle()
t.speed(0)

indonésia()
japao()
india()
EAU()
russia()
ucrania()
armenia()
alemanha()
holanda()
lituania()
polonia()
bulgaria()
yemen()
bolivia()
hungria()
gabao()
serraleoa()
austria()


bandeira = textinput('Bandeira', 'Qual a bandeira: ')
if bandeira == 'indonésia': 
    indonésia()
elif bandeira == 'japão':
    japao()
elif bandeira == 'níger':
    india()
elif bandeira == 'EAU':
    EAU()
elif bandeira == 'rússia':
    russia()
elif bandeira == 'ucrânia':
    ucrania()
elif bandeira == 'armênia':
    armenia()
elif bandeira == 'alemanha':
    alemanha()
elif bandeira == 'holanda':
    holanda()
elif bandeira == 'lituânia':
    lituania()
elif bandeira == 'polônia':
    polonia()
elif bandeira == 'bulgária':
    bulgaria()
elif bandeira == 'yemen':
    yemen()
elif bandeira == 'bolívia':
    bolivia()
elif bandeira == 'hungria':
    hungria()
elif bandeira == 'gabão':
    gabao()
elif bandeira == 'serra leoa':
    serraleoa()
elif bandeira == 'áustria':
    austria()

mainloop()