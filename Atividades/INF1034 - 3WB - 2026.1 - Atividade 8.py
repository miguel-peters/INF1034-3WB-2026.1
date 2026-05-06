from pygame import *
import sys

# Definição das funções
#COMENTAR O QUE ESTÁ SENDO FEITO NAS FUNÇÕES!!

def valida_email(email):
    return email[-8:] == '@puc.com'

def possui_maiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': # letra.isupper()
            return True
    return False

def possui_minuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': # letra.islower()
            return True
    return False

def possui_numero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True
    return False

def valida_senha(senha):
    tamanho = len(senha) >= 8
    letra_M = possui_maiuscula(senha)
    letra_m = possui_minuscula(senha)
    num = possui_numero(senha)
    return tamanho and letra_M  and letra_m and num

def criptografa_senha(senha):
    senha_cripto = ''
    for carac in senha:
        if carac.isdigit():
            ref = ord('0') #65
            ascii_carac = ord(carac) #passo 1
            pos_alf = ascii_carac - ref #passo 2
            pos_cesar = pos_alf + 3 #passo 3
            pos_resto = pos_cesar % 10 #passo 4
            letra_cesar = chr(ref + pos_resto)#passo 5
            senha_cripto += letra_cesar #passo 5
        elif 'A' <= carac <= 'Z':
            ref = ord('A') #65
            ascii_carac = ord(carac) #passo 1
            pos_alf = ascii_carac - ref #passo 2
            pos_cesar = pos_alf + 3 #passo 3
            pos_resto = pos_cesar % 26 #passo 4
            letra_cesar = chr(ref + pos_resto)#passo 5
            senha_cripto += letra_cesar #passo 5
        elif 'a' <= carac <= 'z':
            ref = ord('a') #65
            ascii_carac = ord(carac) #passo 1
            pos_alf = ascii_carac - ref #passo 2
            pos_cesar = pos_alf + 3 #passo 3
            pos_resto = pos_cesar % 26 #passo 4
            letra_cesar = chr(ref + pos_resto)#passo 5
            senha_cripto += letra_cesar #passo 5
        else:
            senha_cripto += carac
    return senha_cripto

window = display.set_mode((1100,700))
init()
fonte = font.SysFont(None, 25)
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

# Definição de variáveis 8
modo_login = True
texto = 'email: '
senha = ''
estado_login = 'email'
texto_cripto = ''



# Definição de variáveis 6
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
        if ev.type == KEYDOWN and modo_login:
            if ev.key == K_RETURN:
                if estado_login == 'email':
                    if valida_email(texto) == True:
                        texto = 'senha: '
                        estado_login = 'senha'
                    else:
                        texto = 'email inválido, digite novamente: '
                else:
                    if valida_senha(texto[7:]) == True:
                        senha_cripto = criptografa_senha(texto[7:])
                        texto_cripto = f'A senha criptografada é: {senha_cripto}'
                        modo_login = False #FAZER COM QUE CLICANDO EM UM LOCAL, O MODO CASA APARECE
                    else:
                        texto = 'senha não atende os critérios, digite novamente: '
            elif ev.key == K_BACKSPACE:
                texto = texto[:-1]
            else:
                texto += ev.unicode
        
        if modo_login == False:
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


    window.fill((255, 255, 255)) # Fundo branco
    superficie_texto = fonte.render(texto, True, (0, 0, 0)) # Texto preto
    window.blit(superficie_texto, (440, 250)) # Posição


    if modo_login == False:
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

        superficie_texto = fonte.render(texto_cripto, True, (0, 0, 0)) # Texto preto
        window.blit(superficie_texto, (0, 600)) # Posição

    display.update()


# senha = input('Digite a sua senha: ')
# print(valida_senha(senha))

# #Pegar a letra e converter para decimal ('Z' --> '90')
# #Subtrair o valor decimal de 65 (para ficar na faixa de 0 - 25) --> 'Z' = '25'
# #Somar 3 ao resultado do passo 2
# #Obter o resto da divisão do resultado do passo 3 por 26
# #Somar o resto a 65 e converter o valor de volta para a letra



# print(criptografa_senha(senha))
