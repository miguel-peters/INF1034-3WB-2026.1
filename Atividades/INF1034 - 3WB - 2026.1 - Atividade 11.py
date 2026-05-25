import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello World')


#herro_walk_list = [] - começar vazia e ir inserindo as imagens dentro da lista
# for i in range(4):
    # herro_walk_list.append(pygame.image.load(f'Hero_Walk_0{i+1}'))

#criar variável
#current_frame = 0 - Representa o frame da animação que está sendo desenhado no momento
# run_animation = False

#prox animação
#current_fram_mm = 0 - controla os frames cada pedaço da imagem
#anim_time_mm = 0
#imagem = pygame.image.load(imagem) - Como é uma spritesheet nao precisa de lista(assets/assets/imagem)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.qui()
            sys.exit()
        # if event.ype == KEYDOWN:
            #if event.key == pygame.K_SPACE:
                #run animation = TRUE
    clock.tick(60)
    dt = clock.get_time()

    #anim_time = anime_time + dt
    #anime_time_sec = anim_time/1000

    #if anim_time_sec > 0.2: 
        #current_frame += 1
        # if current_frame > len(herro_walk_list) - 1:
            #current_frame = 0
        #anim_time_sec = 0

    # REPETE A ESTRUTURA PARA A SEGUNDA ANIMAÇÃO


    screen.fill((255,255,255))

    #screen.blit(variável da imagem, (coordenadas)) - Forma errada pois tem vários frames
    #screen.blit(herro_walk_lis[current_frame], (coordenadas))

    #se for um spreadsheet:
    # if current fram < 5:
        #screen.blit(imagem, (coordenadas), (area - 60 * current_frame,0,60,60- x,y, altura e largura)))
    # else:
        #mexe na coordenada y e current_frame - 5

    # OU faz que nem a foto que eu tirei
    
    # if run_animation == True:
        #FAZ O CÓDIGO DA ANIMAÇÂO usando um run_animation = False

    pygame.display.update()