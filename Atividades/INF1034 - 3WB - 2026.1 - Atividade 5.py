from pygame import *
import sys

init()

#Carregar imagem PNG do programa
#Criar variável 
#batman_img = image.load('batman.png')#mostrar caminho para pegar imagem (pasta/batman.png)

#Criar fonte
#batman_font = font.Font('batmfa__.ttf', 50)

#Carregar música
#mixer.music.load('batman_1966.mp3')
#mixer.music.play(-1)

window = display.set_mode((1150,720))

window.fill((152, 209, 250))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    #Desenhar casa
    draw.rect(window, (72, 157, 37), (0, 600, 1280, 120))
    draw.rect(window, (100, 100, 100), (200, 400, 200, 200))
    draw.polygon(window, (242, 136, 59), ((200, 400), (300, 250), (400,400)))
    draw.rect(window, (13,22,100), (230, 480, 50, 80))
    draw.rect(window, (121,77,27), (300, 465, 65, 135))
    draw.circle(window, (0,0,0), (310, 530), 5)

    #Desenhar árvore
    draw.rect(window, (121,77,27), (680,460,40,140))
    draw.circle(window, (72, 157, 37), (700,400), 75)
    
    #Desenhar sol
    draw.circle(window, (235, 242, 17), (100,100), 60)

    #Desenhar imagens
    #window.blit(batman_img, (0,0))
    #batman_img = transform.scale(batman_img, (200,200))

    #Desenhar texto
    #batman_text = batman_font.render('I am Batman', True, (0,0,0))
    #window.blit(batman_text, 100,200)

    display.update()