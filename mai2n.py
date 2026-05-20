import pygame
import random

# Inicializa o Pygame
pygame.init()

# Cores iniciais
tela = pygame.display.set_mode((400, 300))

# Função para gerar uma cor aleatória
def cor_aleatoria():
    vermelho = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    return (vermelho, verde, azul)

# Game loop
rodando = True
cor_atual = cor_aleatoria()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        # Clica na tela para mudar a cor para uma nova cor aleatória
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            cor_atual = cor_aleatoria()

    # Preenche a tela com a cor aleatória gerada
    tela.fill(cor_atual)
    pygame.display.flip()

pygame.quit()
