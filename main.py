# import pygame

# # Inicialização
# pygame.init()
# tela = pygame.display.set_mode((400, 100))
# fonte = pygame.font.SysFont(None, 40)
# clock = pygame.time.Clock()

# # Variáveis do Input
# texto = ''
# input_ativo = True

# # Loop principal
# rodando = True
# while rodando:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             rodando = False
        
#         # Capturar digitação
#         if event.type == pygame.KEYDOWN and input_ativo:
#             if event.key == pygame.K_RETURN:
#                 print(f"Texto final: {texto}")
#                 texto = '' # Limpa após enter
#             elif event.key == pygame.K_BACKSPACE:
#                 texto = texto[:-1] # Apaga último caractere
#             else:
#                 texto += event.unicode # Adiciona caractere digitado

#     # Desenhar na tela
#     tela.fill((255, 255, 255)) # Fundo branco
#     superficie_texto = fonte.render(texto, True, (0, 0, 0)) # Texto preto
#     tela.blit(superficie_texto, (10, 30)) # Posição
#     pygame.display.flip()
#     clock.tick(30)

# pygame.quit()

senha = 'senha: tudobem'
print(senha[7:])
