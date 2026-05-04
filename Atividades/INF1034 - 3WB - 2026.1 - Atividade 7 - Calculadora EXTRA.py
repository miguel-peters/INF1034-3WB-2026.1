from pygame import *
import sys

window = display.set_mode((1100,700))
init()
running = True

# Imagens
calculadora_img = image.load('calculadoraFINAL.png')

# Fonte
calculadora_fonte = font.Font('Calculator.ttf', 70)

# Variável
conta = '0'
conta2 = '0'

while running:

    for ev in event.get():
        if ev.type == QUIT:
            running = False
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
                    conta2 = '0'
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
            

            if key_pressed == K_PLUS:
                conta2 = ''
                conta = '+'
            
            
    window.fill((252,252,252))

    calculadora_img = transform.scale(calculadora_img, (600,600))
    window.blit(calculadora_img, (200,50))

    calculadora_text = calculadora_fonte.render(conta, True, (0,0,0))
    window.blit(calculadora_text, (625,150))

    calculadora_text = calculadora_fonte.render(conta2, True, (0,0,0))
    window.blit(calculadora_text, (600,150))


    display.update()