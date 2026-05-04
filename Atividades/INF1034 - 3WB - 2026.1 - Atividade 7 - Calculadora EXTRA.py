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
mostrar_contaINI = True

mostrar_op = False
operador = ''

conta3 = '0'
conta4 = '0'
mostrar_contaFIN = False

mostrar_resultado = False
resultadoSTR = '0'


while running:

    conta = input('')

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