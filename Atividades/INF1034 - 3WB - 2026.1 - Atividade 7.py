import random

lista_jogo = ['pedra', 'papel', 'tesoura']

jogada_jogador = input('Qual a sua jogada? ')
jogada_computador = random.choice(lista_jogo)

jogador = 0
computador = 0

def jogo():
    if jogada_jogador == 'papel' and jogada_computador == 'pedra':
        jogador += 1
    elif jogada_jogador == 'tesoura' and jogada_computador == 'papel':
        jogador += 1
    elif jogada_jogador == 'pedra' and jogada_computador == 'tesoura':
        jogador += 1
    elif jogada_jogador == 'papel' and jogada_computador == 'tesoura':
        computador += 1
    elif jogada_jogador == 'tesoura' and jogada_computador == 'pedra':
        computador += 1
    elif jogada_jogador == 'pedra' and jogada_computador == 'papel':
        computador += 1
    else:
        jogador += 0
        computador += 0

print(jogada_computador)
print(jogador)
print(computador)