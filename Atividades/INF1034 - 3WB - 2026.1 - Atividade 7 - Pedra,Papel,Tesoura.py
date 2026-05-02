from random import choice

def jogo():
    jogadas = ('Pedra','Papel','Tesoura')
    jogadaH = input('Qual a sua jogada - Pedra, Papel ou Tesoura? ')
    jogadaC = choice(jogadas)
    pontH = 0
    pontC = 0
    cont = 0
    while cont != 1:
        if jogadaH == 'Pedra' and jogadaC == 'Papel':
            pontC += 1
        elif jogadaH == 'Pedra' and jogadaC == 'Tesoura':
            pontH += 1
        elif jogadaH == 'Papel' and jogadaC == 'Pedra':
            pontH += 1
        elif jogadaH == 'Papel' and jogadaC == 'Tesoura':
            pontC += 1
        elif jogadaH == 'Tesoura' and jogadaC == 'Pedra':
            pontC += 1
        elif jogadaH == 'Tesoura' and jogadaC == 'Papel':
            pontH += 1
        print(f'Placar: Humano {pontH} x {pontC} Computador')
        novamente = input('Revanche? ')
        if novamente == 'Não':
            cont = 1
        else: 
            jogadaH = input('Qual a sua jogada - Pedra, Papel ou Tesoura? ')
            jogadaC = choice(jogadas)

jogo()