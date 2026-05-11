from pygame import *
import sys

# Definição das funções

def valida_email(email):
    return email[-8:] == '@puc.com' # A função está retornando se o e-mail é válido ou não

def possui_maiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': # Se a palavra possui letra maiúscula, a função retorna True
            return True
    return False

def possui_minuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': # Se a palavra possui letra minúscula, a função retorna True
            return True
    return False

def possui_numero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9': # Se a palavra possui número, a função retorna True
            return True
    return False

def valida_senha(senha):
    tamanho = len(senha) >= 8
    letra_M = possui_maiuscula(senha)
    letra_m = possui_minuscula(senha)
    num = possui_numero(senha)
    return tamanho and letra_M  and letra_m and num # Se a senha possuir todas as especificações de cima, a função retorna True


#Pegar a letra e converter para decimal ('Z' --> '90')
#Subtrair o valor decimal de 65 (para ficar na faixa de 0 - 25) --> 'Z' = '25'
#Somar 3 ao resultado do passo 2
#Obter o resto da divisão do resultado do passo 3 por 26
#Somar o resto a 65 e converter o valor de volta para a letra
def criptografa_senha(senha):
    senha_cripto = ''
    for carac in senha:
        if carac.isdigit():
            ref = ord('0') 
            ascii_carac = ord(carac) #passo 1
            pos_alf = ascii_carac - ref #passo 2
            pos_cesar = pos_alf + 3 #passo 3
            pos_resto = pos_cesar % 10 #passo 4
            letra_cesar = chr(ref + pos_resto)#passo 5
            senha_cripto += letra_cesar #passo 5
        elif 'A' <= carac <= 'Z':
            ref = ord('A') 
            ascii_carac = ord(carac) #passo 1
            pos_alf = ascii_carac - ref #passo 2
            pos_cesar = pos_alf + 3 #passo 3
            pos_resto = pos_cesar % 26 #passo 4
            letra_cesar = chr(ref + pos_resto)#passo 5
            senha_cripto += letra_cesar #passo 5
        elif 'a' <= carac <= 'z':
            ref = ord('a') 
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

# Carregar música de fundo
mario = mixer.Sound('mario_musica_tema.mp3')


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
mensagem = ''
jogo = ''
jogo2 = ''
jogo3 = ''
estado_jogo = False
modo_jogo = ''
textodesc = ''

# Definição de variáveis 6
pos_x = 450
pos_x2 = 700
pos_x3= 850
background_color = (152, 209, 250)
direçao = 1
sol_x = 100
sol_y = 100
estado = 'teclado'

# Definição de variáveis CALC

# Imagens
calculadora_img = image.load('calculadoraFINAL.png')
# Fonte
calculadora_fonte = font.Font('Calculator.ttf', 70)
# Variável
conta = '0'
conta2 = '0'
mostrar_contaINI = True
mostrar_op = False
operador = ''
conta3 = '0'
conta4 = '0'
mostrar_contaFIN = False
mostrar_resultado = False
resultadoSTR = '0'

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
                        mensagem = ''
                    else:
                        texto = 'email: '
                        mensagem = 'email inválido!'
                else:
                    if valida_senha(texto[7:]) == True:
                        senha = texto[7:]
                        senha_cripto = criptografa_senha(texto[7:])
                        texto = ''
                        texto= f'A senha criptografada é: {senha_cripto}'
                        jogo = 'Casinha inicial'
                        jogo2 = 'Casinha final'
                        jogo3 = 'Calculadora'
                        textodesc = 'Descriptografar senha'
                        mensagem = ''
                        estado_jogo = True
                    else:
                        texto = 'senha: '
                        mensagem = 'senha inválida!'
            elif ev.key == K_BACKSPACE:
                texto = texto[:-1]
            else:
                texto += ev.unicode
            
        if estado_jogo == True:
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    mouse_pos4 = ev.pos
                    if descriptografado.collidepoint(mouse_pos4):
                        texto = f'Senha descriptogradada = {senha}'

        if estado_jogo == True:
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    mouse_pos = ev.pos
                    if game2.collidepoint(mouse_pos):
                        modo_login = False #FAZER COM QUE CLICANDO EM UM LOCAL, O MODO CASA APARECE
                        modo_jogo = 'casa2'
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    mouse_pos2 = ev.pos
                    if game1.collidepoint(mouse_pos2):
                        modo_login = False
                        modo_jogo = 'casa1'
                        mario.play(-1)
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    mouse_pos3 = ev.pos
                    if game3.collidepoint(mouse_pos3):
                        modo_login = False
                        modo_jogo = 'calculadora'

            
        if modo_login == False and modo_jogo == 'casa2':
            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if key_pressed == K_m:
                    estado = 'mouse'
                elif key_pressed == K_l:
                        estado = 'teclado'
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    if sol_x > 366 and sol_x < 732:
                        pulo_mario.play()
                    elif sol_x > 732:
                        moeda_mario.play()
                    elif sol_x < 366:
                        toady.play()           

        if modo_login == False and modo_login == 'calculadora':
            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if conta2 == '0':
                    if key_pressed == K_1:
                        conta2  = '1'
                    if key_pressed == K_2:
                        conta2 = '2'
                    if key_pressed == K_3:
                        conta2 = '3'
                    if key_pressed == K_4:
                        conta2 = '4'
                    if key_pressed == K_5:
                        conta2 = '5'
                    if key_pressed == K_6:
                        conta2 = '6'
                    if key_pressed == K_7:
                        conta2  = '7'
                    if key_pressed == K_8:
                        conta2 = '8'
                    if key_pressed == K_9:
                        conta2 = '9'
                    if key_pressed == K_0:
                        conta2 = ''
                elif conta == '0':
                    if key_pressed == K_1:
                        conta  = '1'
                    if key_pressed == K_2:
                        conta = '2'
                    if key_pressed == K_3:
                        conta = '3'
                    if key_pressed == K_4:
                        conta = '4'
                    if key_pressed == K_5:
                        conta = '5'
                    if key_pressed == K_6:
                        conta = '6'
                    if key_pressed == K_7:
                        conta  = '7'
                    if key_pressed == K_8:
                        conta = '8'
                    if key_pressed == K_9:
                        conta = '9'
                    if key_pressed == K_0:
                        conta = '0'

            resultado = conta2 + conta
            resultadoINT = int(resultado)
            
            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if key_pressed == K_KP_PLUS:
                    mostrar_contaINI = False
                    mostrar_op = True
                    mostrar_contaFIN = False
                    operador = '+'
                if key_pressed == K_KP_MINUS:
                    mostrar_contaINI = False
                    mostrar_op = True
                    mostrar_contaFIN = False
                    operador = '-'
                if key_pressed == K_KP_DIVIDE:               
                    mostrar_contaINI = False
                    mostrar_op = True
                    mostrar_contaFIN = False
                    operador = '/'
                if key_pressed == K_KP_MULTIPLY:
                    mostrar_contaINI = False
                    mostrar_op = True
                    mostrar_contaFIN = False
                    operador = 'X'
                                
            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if conta4 == '0':
                    if key_pressed == K_1 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True                        
                        conta4  = '1'
                    if key_pressed == K_2 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '2'
                    if key_pressed == K_3 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '3'
                    if key_pressed == K_4 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '4'
                    if key_pressed == K_5 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '5'
                    if key_pressed == K_6 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '6'
                    if key_pressed == K_7 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '7'
                    if key_pressed == K_8 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '8'
                    if key_pressed == K_9 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = '9'
                    if key_pressed == K_0 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta4 = ''
                elif conta3 == '0':
                    if key_pressed == K_1 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3  = '1'
                    if key_pressed == K_2 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '2'
                    if key_pressed == K_3 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '3'
                    if key_pressed == K_4 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '4'
                    if key_pressed == K_5 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '5'
                    if key_pressed == K_6 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '6'
                    if key_pressed == K_7 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3  = '7'
                    if key_pressed == K_8 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '8'
                    if key_pressed == K_9 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '9'
                    if key_pressed == K_0 and mostrar_contaINI == False:
                        mostrar_op = False
                        mostrar_contaFIN = True
                        conta3 = '0'
            
            resultado2 = conta4 + conta3
            resultadoINT2 = int(resultado2)


            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if key_pressed == K_KP_ENTER and operador == '+':
                    mostrar_resultado = True
                    mostrar_contaFIN = False
                    resultadoFIN = resultadoINT + resultadoINT2
                    resultadoSTR = str(resultadoFIN)
                elif key_pressed == K_KP_ENTER and operador == '-':
                    mostrar_resultado = True
                    mostrar_contaFIN = False
                    resultadoFIN = resultadoINT - resultadoINT2
                    resultadoSTR = str(resultadoFIN)
                elif key_pressed == K_KP_ENTER and operador == '/':
                    mostrar_resultado = True
                    mostrar_contaFIN = False
                    resultadoFIN = resultadoINT / resultadoINT2
                    resultadoSTR = str(resultadoFIN)
                elif key_pressed == K_KP_ENTER and operador == 'X':
                    mostrar_resultado = True
                    mostrar_contaFIN = False
                    resultadoFIN = resultadoINT * resultadoINT2
                    resultadoSTR = str(resultadoFIN)

    window.fill((104, 50, 168)) # Fundo

    #Caixa
    draw.rect(window, (225,225,225), (190,230,750,50))
    
    if estado_jogo == True:
        game1 = draw.rect(window, (58, 22, 168), (200, 390, 150, 50))
        game2 = draw.rect(window, (58, 22, 168), (500, 390, 150, 50))
        game3 = draw.rect(window, (58, 22, 168), (800, 390, 150, 50))
        descriptografado = draw.rect(window, (225, 225, 225), (450, 90, 200, 50))

    #Textos
    superficie_texto = fonte.render(texto, True, (0, 0, 0)) # Texto preto
    window.blit(superficie_texto, (200, 250)) # Posição

    superficie_texto = fonte.render(mensagem, True, (242, 23, 7)) # Texto vermelho
    window.blit(superficie_texto, (200, 285)) # Posição

    superficie_texto = fonte.render(jogo, True, (0, 0, 0)) # Texto vermelho
    window.blit(superficie_texto, (210, 400)) # Posição

    superficie_texto = fonte.render(jogo2, True, (0, 0, 0)) # Texto vermelho
    window.blit(superficie_texto, (510, 400)) # Posição

    superficie_texto = fonte.render(jogo3, True, (0, 0, 0)) # Texto vermelho
    window.blit(superficie_texto, (810, 400)) # Posição

    superficie_texto = fonte.render(textodesc, True, (0, 0, 0)) # Texto preto
    window.blit(superficie_texto, (460, 100)) # Posição

    superficie_texto = fonte.render(texto_cripto, True, (0, 0, 0)) # Texto preto
    window.blit(superficie_texto, (200, 250)) # Posição


    if modo_login == False and modo_jogo == 'casa2':
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

        # Desenhar grama
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



    if modo_login == False and modo_jogo == 'casa1':

        window.fill((152, 209, 250))

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

    if modo_login == False and modo_jogo == 'calculadora':
        window.fill((252,252,252))

        calculadora_img = transform.scale(calculadora_img, (600,600))
        window.blit(calculadora_img, (200,50))

        calculadora_conta = calculadora_fonte.render(conta, True, (0,0,0))
        calculadora_conta2 = calculadora_fonte.render(conta2, True, (0,0,0))
        calculadora_op = calculadora_fonte.render(operador, True, (0,0,0))
        calculadora_conta3 = calculadora_fonte.render(conta3, True, (0,0,0))
        calculadora_conta4 = calculadora_fonte.render(conta4, True, (0,0,0))
        calculadora_res = calculadora_fonte.render(resultadoSTR, True, (0,0,0))

        if mostrar_contaINI:
            window.blit(calculadora_conta, (375,150))
            window.blit(calculadora_conta2, (350,150))

        if mostrar_resultado:
            window.blit(calculadora_res, (350,150))

        if mostrar_op:
            window.blit(calculadora_op, (600,150))

        if mostrar_contaFIN:
            window.blit(calculadora_conta3, (375,150))
            window.blit(calculadora_conta4, (350,150))


    display.update()