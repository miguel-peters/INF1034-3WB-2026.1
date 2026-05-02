from math import inf

def conta():
    num1 = float(input(''))
    operador = input('')
    num2 = float(input(''))
    if operador == '+':
        resposta = num1 + num2
    elif operador == '-':
        resposta = num1 - num2
    elif operador == 'x':
        resposta = num1 * num2
    elif operador == '/':
        resposta = num1 / num2
    while num1 > -inf:
        print(resposta)
        operador = input('')
        num3 = float(input(''))
        if operador == '+':
            resposta += num3
        elif operador == '-':
            resposta -= num3
        elif operador == 'x':
            resposta *= num3
        elif operador == '/':
            resposta /= num3

conta()