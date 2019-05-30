import pygame
from os import path
from Peter_Kong import Menu,WIDTH,HEIGHT,INIT,QUIT


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
            state= Menu(screen)
        if state== QUIT:
            pygame.quit()
            
finally:
    pygame.quit()
            