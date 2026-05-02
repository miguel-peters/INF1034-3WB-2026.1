from random import randint

def adivinha(numA, numB):
    if numA > numB:
        print('1')
    elif numA < numB:
        print('-1')
    else:
        print('0 - Número de tentativas = 1')

    if escolha == 'Humano':
        numCH  = int(input('Adivinhe outro número: '))
        tentativa = 1
        while numCH != numB:
            if numCH > numB:
                print('1')
            elif numCH < numB:
                print('-1')
            tentativa += 1
            numCH = int(input('Adivinhe outro número: '))
        print(f'0 - Número de tentativas: {tentativa}')
    elif escolha == 'Computador':
        numCC = randint(1,1023)
        tentativa = 1
        while numCC != numB:
            if numCC > numB:
                print('1')
            elif numCC < numB:
                print('-1')
            tentativa += 1
            numCC = randint(1,1023)
        print(f'0 - Número de tentativas: {tentativa}')

escolha = input('QUEM TENTARÁ ADIVINHAR - Humano ou Computador?')
numEscolhido = randint(1,1023)

if escolha == 'Humano':
    num = int(input('Adivinhe um número de 1 a 1023: '))
    adivinha(num,numEscolhido)
elif escolha == 'Computador':
    numH = int(input('Escolha um número para o computador adivinhar: '))
    adivinha(numEscolhido,numH)