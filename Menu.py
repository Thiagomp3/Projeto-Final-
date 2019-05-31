import pygame
from PeterKong import menu,WIDTH,HEIGHT,JOGO,QUIT,game_screen,INIT


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen= pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Peter Kong")

try:
    state= INIT
    while state != QUIT:
        if state == INIT:
            state= menu(screen)
        if state== QUIT:
            pygame.quit()
        if state == JOGO:
            state = game_screen(screen)
            state = QUIT
            
finally:
    pygame.quit()
            