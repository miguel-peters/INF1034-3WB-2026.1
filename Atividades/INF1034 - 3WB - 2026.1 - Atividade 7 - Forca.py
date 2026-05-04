from random import choice

temas = ['time de futebol', 'comida', 'pokemon', 'pais', 'time de basquete']
tema_escolhido = choice(temas)

if tema_escolhido == 'time de futebol':
    palavras = ['flamengo', 'vasco', 'fluminense', 'botafogo', 'palmeiras', 'corinthians']
elif tema_escolhido == 'comida':
    palavras = ['frango', 'carne', 'peixe', 'macarrao', 'arroz', 'feijao']
elif tema_escolhido == 'pokemon':
    palavras = ['pikachu', 'blastoise', 'pidgey', 'gyarados', 'raikou', 'gardevoir']
elif tema_escolhido == 'pais':
    palavras = ['brasil', 'espanha', 'portugal', 'alemanha', 'franca', 'argentina']
elif tema_escolhido == 'time de basquete':
    palavras = ['heat', 'suns', 'lakers', 'warriors', 'spurs', 'thunder']

palavra_escolhida = choice(palavras)
letras = ['_'] * len(palavra_escolhida)
vidas = 6

def forca():
    global vidas
    letra = input('Chute uma letra: ')
    if letra in palavra_escolhida:
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras[i] = letra
    else:
        vidas -= 1
        print(f'Letra errada! - Vidas: {vidas}')
    print(' '.join(letras)) #O JOIN SE USA PARA UNIR ELEMENTOS DE UMA LISTA! (iliteráveis)

print(f'Seu tema é: {tema_escolhido}')
print(' '.join(letras))

while vidas > 0:
    forca()
    if palavra_escolhida == ''.join(letras):
        print('Você ganhou!')
        break
if vidas == 0:
    print(f'Você perdeu! A palavra era {palavra_escolhida}')