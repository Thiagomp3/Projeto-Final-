# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path


# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')


# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



mapa= [[0,1,2],
       [0]*10,
       [0]*10,
       [0]*10,
       [0]*10,]

linha=0
for e in mapa:
    for i in mapa[linha]:
        if i == 0:
            print("espaco vazio feature")
        elif i == 1:
            print("chao")
        elif i == 2:
            print("escada")
    linha+=1
    

        
    


       
       
       
    

   