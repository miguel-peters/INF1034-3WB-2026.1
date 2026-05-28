from pygame import *
import sys

clock = time.Clock()

estado = 'idle'



# ANIMAÇÃO 1
curr_frame_idle = 0
anim_time_idle = 0
knight_idle = image.load('Imagens/IDLE.png')

# ANIMAÇÃO 2
curr_frame_run = 0
anim_time_run = 0
knigth_run = image.load('Imagens/RUN.png')
pos_x = 200

curr_frame_runLFT = 0
anim_time_runLFT = 0
knigth_runLFT = image.load('Imagens/RUNLFT.png')

# ANIMAÇÃO 3
curr_frame_jump = 0
anim_time_jump = 0
knigth_jump = image.load('Imagens/JUMP.png')

init()

mixer.music.load('pokemon.mp3')
mixer.music.play(-1)
screen = display.set_mode((800, 600))
display.set_caption('Hello World!')

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                estado = 'jump'

    clock.tick(60)
    dt = clock.get_time()
    keys = key.get_pressed()

    if keys[K_d]:
        estado = 'run'
        pos_x = pos_x + 0.1*dt
    elif not keys[K_d] and estado == 'run':
        estado = 'idle'
    if keys[K_a]:
        estado = 'runLFT'
        pos_x = pos_x - 0.1*dt
    elif not keys[K_a] and estado == 'runLFT':
        estado = 'idle'

    if estado == 'idle':
        anim_time_idle = anim_time_idle + dt
        anim_time_idle_sec = anim_time_idle/1000

        if anim_time_idle > 100:
            curr_frame_idle = curr_frame_idle + 1
            if curr_frame_idle > 6:
                curr_frame_idle = 0
            anim_time_idle = 0
    
    if estado == 'run':
        anim_time_run = anim_time_run + dt
        anim_time_run_sec = anim_time_run/1000
        
        if anim_time_run_sec > 0.1:
            curr_frame_run = curr_frame_run + 1
            if curr_frame_run > 7:
                curr_frame_run = 0
            anim_time_run = 0

    if estado == 'runLFT':
        anim_time_runLFT = anim_time_runLFT + dt
        anim_time_run_secLFT = anim_time_runLFT/1000
        
        if anim_time_run_secLFT > 0.1:
            curr_frame_runLFT = curr_frame_runLFT + 1
            if curr_frame_runLFT > 7:
                curr_frame_runLFT = 0
            anim_time_runLFT = 0

    if estado == 'jump':
        anim_time_jump =  anim_time_jump + dt
        anim_time_jump_sec = anim_time_jump/1000

        if anim_time_jump_sec > 0.1:
            curr_frame_jump = curr_frame_jump + 1
            if curr_frame_jump > 4:
                curr_frame_jump = 0
                estado = 'idle'
            anim_time_jump = 0

    # Desenho dos elementos na tela
    screen.fill((50, 4, 179))

    # screen.blit(dog_img, (0, 0))
    # screen.blit(hero_walk_list[curr_frame], (0, 0))

    # if curr_frame_mm < 5:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * curr_frame_mm, 0, 60, 60))
    # else:
    #     screen.blit(megaman_spritesheet, (200, 200), (60 * (curr_frame_mm - 5), 60, 60, 60))
    
    draw.rect(screen, (72, 157, 37), (0, 400, 1280, 200))

    draw.rect(screen, (121,77,27), (500,300,40,140))
    draw.circle(screen, (72, 157, 37), (520,270), 75)

    draw.rect(screen, (121,77,27), (100,300,40,140))
    draw.circle(screen, (72, 157, 37), (120,270), 75)

    draw.rect(screen, (121,77,27), (250,270,40,140))
    draw.circle(screen, (72, 157, 37), (270,240), 75)

    if estado == 'run':
        knigth_scale_run = transform.scale(knigth_run, (1200,150))
        screen.blit(knigth_scale_run, (pos_x, 400), (150*(curr_frame_run), 0, 150, 150))

    if estado == 'runLFT':
        knight_scale_runLFT = transform.scale(knigth_runLFT, (1200, 150))
        screen.blit(knight_scale_runLFT, (pos_x, 400), (150*(curr_frame_runLFT), 0, 150, 150))

    if estado == 'idle':
        knight_scale_idle = transform.scale(knight_idle, (1200,150))
        screen.blit(knight_scale_idle, (pos_x,400), (171.5*(curr_frame_idle), 0, 171.5, 171.5))

    if estado == 'jump':
        knigth_scale_jump = transform.scale(knigth_jump, (1000,150))
        screen.blit(knigth_scale_jump, (pos_x, 400), (200*(curr_frame_jump), 0, 200, 200))


    display.update()