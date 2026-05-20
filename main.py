import pygame, sys
from pygame.locals import QUIT

nums = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130
]
num_cat = 4
num_min = min(nums)
num_max = max(nums)
tam_cat = (num_max - num_min) / num_cat
lista_total = [0] * num_cat


def contabiliza_totais(nums, lista_total):
    # Para cada número na minha lista
    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        # Para cada faixa/categoria
        for i_cat in range(num_cat):
            # Obtém os limites inferior e superior
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            # Checa em qual faixa/categoria o número está com base nesses limites
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total

print(lista_total)
print(contabiliza_totais(nums, lista_total))


def draw(screen):
    screen_h = screen.get_height()
    for i in range(len(lista_total)):
        x = 100 + i * 50
        h = 20 * lista_total[i]
        pygame.draw.rect(screen, (255, 0, 0), (x, screen_h - h - 80, 25, h))
        
lista_nums = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, #170, 130
]
num = int(input("Digite um número"))
lista_nums.append(num)
print(nums)


pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    draw(screen)
    pygame.display.update()