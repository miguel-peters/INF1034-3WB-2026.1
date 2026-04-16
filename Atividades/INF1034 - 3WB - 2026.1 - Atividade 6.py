from pygame import *
import sys


window = display.set_mode((1100,720))
init()
running = True
clock = time.Clock()

# Carregar imagem PNG do programa
# Criar variável 
mario_img = image.load('mario.png')#mostrar caminho para pegar imagem (pasta/batman.png)

# Criar fonte
mario_font = font.Font('SuperMario256.ttf', 25)

# # Carregar música
# mixer.music.load('mario_musica_tema.mp3')
# mixer.music.play(-1)
pulo_mario = mixer.Sound('pulo_mario.mp3')
moeda_mario = mixer.Sound('moeda_mario.mp3')
toady = mixer.Sound('toady.mp3')

# Definição de variáveis
pos_x = 450
pos_x2 = 700
pos_x3= 850
background_color = (152, 209, 250)
direçao = 1
sol_x = 100
sol_y = 100
estado = 'teclado'

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_m:
                estado = 'mouse'
            elif key_pressed == K_l:
                estado = 'teclado'
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                if sol_x > 366 and sol_x < 732:
                    pulo_mario.play()
                elif sol_x > 732:
                    moeda_mario.play()
                elif sol_x < 366:
                    toady.play()

    # Update
    dt = clock.get_time()/1000 #em segundos
    keys = key.get_pressed()
    
    # Sol se mexendo com o teclado e mouse
    if estado == 'mouse':
        sol_x, sol_y = mouse.get_pos()
    elif estado == 'teclado':
        if keys[K_d]:
            sol_x = sol_x + 300 * dt
        elif keys[K_a]:
            sol_x = sol_x - 300 * dt
        elif keys[K_w]:
            sol_y = sol_y - 300 * dt
        elif keys[K_s]:
            sol_y = sol_y + 300 * dt

    if sol_x > 1100:
        sol_x = 1100
    elif sol_x < 0:
        sol_x = 0

    # Cor mudando de acordo com a posição do sol
    if sol_x > 366 and sol_x < 732:
        background_color = (227, 162, 11 )
    elif sol_x > 732:
        background_color = (50, 68, 168)
    else:
        background_color = (152, 209, 250)

    # Nuvens se mexendo
    pos_x = pos_x + (100 * direçao) * dt
    pos_x2 = pos_x2 + (100 * direçao) * dt 
    pos_x3 = pos_x3 + (100*direçao) * dt
    if pos_x3 > 1100:
        direçao = -1
    elif pos_x < 0:
        direçao = 1   
   
    # Desenhar tela
    window.fill(background_color)

    # Desenhar casa
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
    draw.circle(window, (235, 242, 17), (sol_x, sol_y), 60)
    draw.line(window, (235, 242, 17), (sol_x, sol_y + 60), (sol_x,sol_y + 130), (5))
    draw.line(window, (235, 242, 17), (sol_x + 60, sol_y), (sol_x + 130, sol_y), (5))
    draw.line(window, (235, 242, 17), (sol_x, sol_y - 60), (sol_x, sol_y - 100), (5))
    draw.line(window, (235, 242, 17), (sol_x - 60, sol_y), (sol_x - 100, sol_y), (5))

    #Desenhar nuvem    
    draw.circle(window, (235,235,235), (pos_x,100), 50)
    draw.circle(window, (235,235,235), (pos_x + 50,100), 50)
    draw.circle(window, (235,235,235), (pos_x + 100,100), 50)
    draw.circle(window, (235,235,235), (pos_x + 150,100), 50)

    draw.circle(window, (235,235,235), (pos_x2,200), 50)
    draw.circle(window, (235,235,235), (pos_x2 + 50,200), 50)
    draw.circle(window, (235,235,235), (pos_x2 + 100,200), 50)
    draw.circle(window, (235,235,235), (pos_x3,200), 50)


    #Desenhar imagens
    mario_img = transform.scale(mario_img, (100,150))
    window.blit(mario_img, (450, 470))
    
    #Desenhar texto
    mario_text = mario_font.render('It is me, MARIO!', True, (0,0,0))
    window.blit(mario_text, (410,650))

    display.update()