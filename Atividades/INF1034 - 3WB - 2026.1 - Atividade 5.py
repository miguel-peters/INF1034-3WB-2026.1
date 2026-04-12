from pygame import *
import sys

init()

#Carregar imagem PNG do programa
#Criar variável 
mario_img = image.load('mario.png')#mostrar caminho para pegar imagem (pasta/batman.png)

#Criar fonte
mario_font = font.Font('SuperMario256.ttf', 25)

#Carregar música
mixer.music.load('mario_musica_tema.mp3')
mixer.music.play(-1)

window = display.set_mode((1100,720))
# relogio = time.Clock()

window.fill((152, 209, 250))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()


    draw.rect(window, (72, 157, 37), (0, 600, 1280, 120))
    
    # Desenhar casa
    draw.rect(window, (100, 100, 100), (200, 400, 200, 200))
    draw.polygon(window, (166, 60, 15), ((190, 400), (230, 300), (370,300), (410,400)))
    draw.rect(window, (13,22,100), (230, 480, 50, 80))
    draw.rect(window, (121,77,27), (300, 465, 65, 135))
    draw.circle(window, (0,0,0), (310, 530), 5)

    # Desenhar árvore
    draw.rect(window, (121,77,27), (680,460,40,140))
    draw.circle(window, (72, 157, 37), (700,400), 75)
    
    #Desenhar sol
    draw.circle(window, (235, 242, 17), (100,100), 60)
    draw.line(window, (235, 242, 17), (100,160), (100,230), (5))
    draw.line(window, (235, 242, 17), (160, 100), (230, 100), (5))
    draw.line(window, (235, 242, 17), (100, 40), (100, 0), (5))
    draw.line(window, (235, 242, 17), (40, 100), (0, 100), (5))

    #Desenhar nuvem    
    draw.circle(window, (235,235,235), (450,100), 50)
    draw.circle(window, (235,235,235), (500,100), 50)
    draw.circle(window, (235,235,235), (550,100), 50)
    draw.circle(window, (235,235,235), (600,100), 50)

    draw.circle(window, (235,235,235), (700,200), 50)
    draw.circle(window, (235,235,235), (750,200), 50)
    draw.circle(window, (235,235,235), (800,200), 50)
    draw.circle(window, (235,235,235), (850,200), 50)


    #Desenhar imagens
    mario_img = transform.scale(mario_img, (100,150))
    window.blit(mario_img, (450, 470))
    
    #Desenhar texto
    mario_text = mario_font.render('It is me, MARIO!', True, (0,0,0))
    window.blit(mario_text, (410,650))

    # relogio.tick(60)
    display.update()
    