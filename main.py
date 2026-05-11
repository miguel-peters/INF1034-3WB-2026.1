import pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((400, 300))
# Definir um retângulo (área clicável)
button_rect = pygame.Rect(150, 100, 100, 50) # x, y, largura, altura

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 1. Verificar se o mouse foi clicado
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 = botão esquerdo
                # 2. Obter posição do clique
                mouse_pos = event.pos
                
                # 3. Verificar se o clique foi dentro do retângulo
                if button_rect.collidepoint(mouse_pos):
                    print("Botão clicado!")

    # Desenhar
    screen.fill((0, 0, 0)) # Fundo preto
    pygame.draw.rect(screen, (255, 0, 0), button_rect) # Retângulo vermelho
    pygame.display.flip()

pygame.quit()
