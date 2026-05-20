import pygame
import sys
from pygame.locals import QUIT
import random

# HISTOGRAMA 1

lista1 = [random.randint(100,200) for _ in range(50)]

num_categorias = 5
num_min = min(lista1)
num_max = max(lista1)
tam_categoria = (num_max - num_min)/num_categorias

lista1_final = [0] * num_categorias #"Biblioteca"

def organizaCateg(lista1, lista1_final):
    for i in range(len(lista1)):
        if lista1[i] == num_max:
            lista1_final[-1] += 1
            continue
        
        for i_categoria in range(num_categorias):
            lim_inf = num_min + i_categoria*tam_categoria
            lim_sup = lim_inf + tam_categoria

            if lim_inf <= lista1[i] < lim_sup:
                lista1_final[i_categoria] += 1
                break
    return lista1_final

print(organizaCateg(lista1, lista1_final))

# HISTOGRAMA 2

lista2 = [1,2,3,4,5,6,7,8,9,10]

num_categorias = 4
tam_categoria = random.randint(1, len(lista2))

lista2_final = [0] * num_categorias

def contaCateg(lista2, lista2_final,):
    for i in range(len(lista2)):

        for i_cat in range(num_categorias):
            escolha = random.sample(lista2, tam_categoria)
            soma = 0
            for i_escolha in range(len(escolha)):
                soma += escolha[i_escolha]
                if soma < len(lista2):
                    lista2_final[i_cat] += 1
                    break
    return lista2_final

print(contaCateg(lista2, lista2_final,))

# HISTOGRAMA 3

escolha_lista = input('Digite os números da lista: ')
lista3 = [int(item) for item in escolha_lista.split()]


num_categorias = 3
num_min = min(lista3)
num_max = max(lista3)
tam_categoria = (num_max - num_min)/num_categorias

lista3_final = [0] * num_categorias #"Biblioteca"

def organizaCateg(lista3, lista3_final):
    for i in range(len(lista3)):
        if lista3[i] == num_max:
            lista3_final[-1] += 1
            continue
        
        for i_categoria in range(num_categorias):
            lim_inf = num_min + i_categoria*tam_categoria
            lim_sup = lim_inf + tam_categoria

            if lim_inf <= lista3[i] < lim_sup:
                lista3_final[i_categoria] += 1
                break
    return lista3_final

print(organizaCateg(lista3, lista3_final))


def cor_aleatoria():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

cor_coluna = [cor_aleatoria(), cor_aleatoria(), cor_aleatoria(), cor_aleatoria(), cor_aleatoria()]

def draw1(screen):
    screen_altura = screen.get_height()
    for i in range(len(lista1_final)):
        x = 400 + i * 50
        h = 20 * lista1_final[i]
        pygame.draw.rect(screen, (cor_coluna[i]), (x, screen_altura - h - 220, 25, h))

def draw2(screen):
    screen_altura = screen.get_height()
    for i in range(len(lista2_final)):
        x = 400 + i * 50
        h = 20 * lista2_final[i]
        pygame.draw.rect(screen, (cor_coluna[i]), (x, screen_altura - h - 220, 25, h))

def draw3(screen):
    screen_altura = screen.get_height()
    for i in range(len(lista3_final)):
        x = 400 + i * 50
        h = 20 * lista3_final[i]
        pygame.draw.rect(screen, (cor_coluna[i]), (x, screen_altura - h - 220, 25, h))

pygame.init()
screen = pygame.display.set_mode((1100,700))
fonte = pygame.font.SysFont(None, 25)
running = True

# Variáveis

modo_hist = '1'

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running == False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                modo_hist = '1'
            elif event.key == pygame.K_2:
                modo_hist = '2'
            elif event.key == pygame.K_3:
                modo_hist = '3'
    
    screen.fill((255, 255, 255))

    # Desenhar medidas

    pygame.draw.line(screen, (0,0,0), (325,480),(325,100),(3))
    pygame.draw.line(screen, (0,0,0), (325,480),(750,480),(3))
    pygame.draw.line(screen, (0,0,0), (315,460),(335,460),(3))
    pygame.draw.line(screen, (0,0,0), (315,440),(335,440),(3))
    pygame.draw.line(screen, (0,0,0), (315,420),(335,420),(3))
    pygame.draw.line(screen, (0,0,0), (315,400),(335,400),(3))
    pygame.draw.line(screen, (0,0,0), (315,380),(335,380),(3))
    pygame.draw.line(screen, (0,0,0), (315,360),(335,360),(3))
    pygame.draw.line(screen, (0,0,0), (315,340),(335,340),(3))
    pygame.draw.line(screen, (0,0,0), (315,320),(335,320),(3))
    pygame.draw.line(screen, (0,0,0), (315,300),(335,300),(3))
    pygame.draw.line(screen, (0,0,0), (315,280),(335,280),(3))
    pygame.draw.line(screen, (0,0,0), (315,260),(335,260),(3))
    pygame.draw.line(screen, (0,0,0), (315,240),(335,240),(3))
    pygame.draw.line(screen, (0,0,0), (315,220),(335,220),(3))
    pygame.draw.line(screen, (0,0,0), (315,200),(335,200),(3))
    pygame.draw.line(screen, (0,0,0), (315,180),(335,180),(3))
    pygame.draw.line(screen, (0,0,0), (315,160),(335,160),(3))
    pygame.draw.line(screen, (0,0,0), (315,140),(335,140),(3))
    pygame.draw.line(screen, (0,0,0), (315,120),(335,120),(3))

    # Aplicar número nas medidas

    numero1 = fonte.render('1', True, (0,0,0))
    screen.blit(numero1, (305,455))

    numero2 = fonte.render('2', True, (0,0,0))
    screen.blit(numero2, (305,435))

    numero3 = fonte.render('3', True, (0,0,0))
    screen.blit(numero3, (305,415))

    numero4 = fonte.render('4', True, (0,0,0))
    screen.blit(numero4, (305,395))

    numero5 = fonte.render('5', True, (0,0,0))
    screen.blit(numero5, (305,375))

    numero6 = fonte.render('6', True, (0,0,0))
    screen.blit(numero6, (305,355))

    numero7 = fonte.render('7', True, (0,0,0))
    screen.blit(numero7, (305,335))

    numero8 = fonte.render('8', True, (0,0,0))
    screen.blit(numero8, (305,315))

    numero9 = fonte.render('9', True, (0,0,0))
    screen.blit(numero9, (305,295))

    numero10 = fonte.render('10', True, (0,0,0))
    screen.blit(numero10, (295,275))

    numero11 = fonte.render('11', True, (0,0,0))
    screen.blit(numero11, (295,255))

    numero12 = fonte.render('12', True, (0,0,0))
    screen.blit(numero12, (295,235))

    numero13 = fonte.render('13', True, (0,0,0))
    screen.blit(numero13, (295,215))

    numero14 = fonte.render('14', True, (0,0,0))
    screen.blit(numero14, (295,195))

    numero15 = fonte.render('15', True, (0,0,0))
    screen.blit(numero15, (295,175))

    numero16 = fonte.render('16', True, (0,0,0))
    screen.blit(numero16, (295,155))

    numero17 = fonte.render('17', True, (0,0,0))
    screen.blit(numero17, (295,135))

    numero18 = fonte.render('18', True, (0,0,0))
    screen.blit(numero18, (295,115))

    if modo_hist == '1':
        draw1(screen)
    elif modo_hist == '2':
        draw2(screen)
    elif modo_hist == '3':
        draw3(screen)

    pygame.display.update()