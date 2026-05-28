import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

# dog_img = pygame.image.load("chiens-funnyanimals.gif")

# hero_img = pygame.image.load("assets/assets/Hero_Walk_01.png")

# hero_walk_list = [
#     pygame.image.load("assets/assets/Hero_Walk_01.png"),
#     pygame.image.load("assets/assets/Hero_Walk_02.png"),
#     pygame.image.load("assets/assets/Hero_Walk_03.png"),
#     pygame.image.load("assets/assets/Hero_Walk_04.png")
# ]

# curr_frame = 0
# anim_time = 0
# hero_walk_list = []
# for i in range(4):
#     hero_walk_list.append(pygame.image.load(f"assets/assets/Hero_Walk_0{i+1}.png"))


curr_frame_mm = 0
anim_time_mm = 0
megaman_spritesheet = pygame.image.load("RUN.png")

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                run_animation = True

    clock.tick(60)
    dt = clock.get_time()
    
    anim_time_mm = anim_time_mm + dt
    anim_time_mm_sec = anim_time_mm/1000

    if anim_time_mm_sec > 0.1:
        curr_frame_mm = curr_frame_mm + 1
        # curr_frame_mm += 1
        if curr_frame_mm > 7:
            curr_frame_mm = 0
        anim_time_mm = 0

    # Desenho dos elementos na tela
    screen.fill((255,255,255))

    # screen.blit(dog_img, (0, 0))
    # screen.blit(hero_walk_list[curr_frame], (0, 0))

    # if curr_frame_mm < 5:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * curr_frame_mm, 0, 60, 60))
    # else:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * (curr_frame_mm - 5), 60, 60, 60))
    
    screen.blit(megaman_spritesheet, (200, 200), (96*(curr_frame_mm), 0, 96, 84))

    pygame.display.update()