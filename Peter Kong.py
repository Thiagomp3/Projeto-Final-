# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')


# Dados gerais do jogo.
TITULO = 'Exemplo de Pulo com obstáculos'
WIDTH = 1024 # Largura da tela
HEIGHT = 600 # Altura da tela é 800, coloquei 600 pra rodar no meu pc
TILE_SIZE = 24 # Tamanho de cada tile (cada tile é um quadrado) 32
PLAYER_WIDTH = 24  #32    
PLAYER_HEIGHT = 24 #32
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 5
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE
# Define a velocidade em x
SPEED_X = 5


# Define o mapa com os tipos de tiles
MAP = [
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3],
    [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,2,3,3],
    [0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,1,1,1,1,1,1,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
    [3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3],
    [0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0],
    [0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0],
    [0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    
]

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
CLIMBING = 3

# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img, row, column, blocks,stairs):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Ajusta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks

        # Bloco da escadas
        self.stairs = stairs

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE

        self.speedx = 0
        self.speedy = 0

    # Metodo que atualiza a posição do personagem
    def update(self):
        # Vamos tratar os movimentos de maneira independente.
        # Primeiro tentamos andar no eixo y e depois no x.
        colidiu_escada = pygame.sprite.spritecollide(self, self.stairs, False)
        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        jr= int(self.rect.right/32)
        jl= int(self.rect.left/32)
        i= int(self.rect.bottom/32)
        
        tl= MAP[i][jl]
        tr= MAP[i][jr]
        
        if not (colidiu_escada or (self.rect.bottom % 32==0 and tl==2 or tr==2)): 
            self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    # Subir escada
    def climb(self):
        if self.state == STILL:
            self.spee


#classe do Thanos
class Thanos(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, thanos_img, row, column, blocks):


# Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Ajusta o tamanho da imagem

        thanos_img = pygame.transform.scale(thanos_img, (96, 96))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = thanos_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE

        #for mudar velocidade 
        self.speedx = 5
        self.speedy = 5

    # Metodo que atualiza a posição do personagem
    def update(self):
        # Vamos tratar os movimentos de maneira independente.
        # Primeiro tentamos andar no eixo y e depois no x.

        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 5
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
            self.speedx = -5
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:

            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
                
# Classe Bullet que representa os tiros
class Tiro(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, tiro_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        tiro_img = pygame.image.load(path.join(img_dir, "Meteoro.png")).convert()
        self.image = tiro_img
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

class Meteoro(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, meteoro_img, blocks):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = pygame.transform.scale(meteoro_img, (30, 30))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        self.blocks = blocks
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centery = y
        self.rect.bottom = x
        self.speedx = 1.5
        self.speedy = 0
    # Metodo que atualiza a posição do meteoro
    def update(self):


        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 5
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
            self.speedx = -5
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:

            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.right < 0 and self.rect.left > 0:
            self.kill()

        
# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets["PLAYER_IMG"] = pygame.image.load(path.join(img_dir, 'AvatarPeterQuill.png')).convert_alpha()
    assets["BLOCK"] = pygame.image.load(path.join(img_dir, 'platform.png')).convert()
    assets["ESCADA"] = pygame.image.load(path.join(img_dir, 'escada.png')).convert()
    assets["BLOCK2"] = pygame.image.load(path.join(img_dir, 'esteira.png')).convert()
    assets["THANOS_IMG"] = pygame.image.load(path.join(img_dir, "Thanos_0.png")).convert()
    assets["METEORO_IMG"] = pygame.image.load(path.join(img_dir, "Meteoro.png")).convert()
    assets["TIRO_IMG"] = pygame.image.load(path.join(img_dir, "Meteoro.png")).convert()
     
     #dps trocar o sprite do tiro

    return assets


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de escadas.
    # Sprites de escada são aqueles que possibilitam a movimentação vertical do personagem.
    stairs = pygame.sprite.Group()    
    

    # Cria Sprite do jogador
    player = Player(assets["PLAYER_IMG"], 24, 3, blocks, stairs)
    # Cria Sprite do Thanos
    thanos = Thanos(assets["THANOS_IMG"], 9, 6, blocks)
    #Cria Sprite do Meteoro
    meteoro = Meteoro(16, 6, assets["METEORO_IMG"], blocks)
    #Cria Sprite do Tiro    
    tiro= Tiro(9, 6, assets["TIRO_IMG"])

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == 1:
                tile = Tile(assets["BLOCK"], row, column)
                all_sprites.add(tile)
                blocks.add(tile)
            if tile_type == 2:
                tile = Tile(assets["ESCADA"], row, column)
                all_sprites.add(tile)
                stairs.add(tile)
            if tile_type == 3:
                tile = Tile(assets["BLOCK2"], row, column)
                all_sprites.add(tile)
                blocks.add(tile)


    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    
    # Adiciona o Thanos no grupo de sprites por último
    all_sprites.add(player,thanos, meteoro,tiro)


    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                
                elif event.key == pygame.K_UP:
                    colidiu_escada = pygame.sprite.spritecollide(player, stairs, False)
                    if colidiu_escada:
                        player.rect.centerx= colidiu_escada[0].rect.centerx
                        player.speedy = -5
                        player.state = CLIMBING
                        
                    else:
                        player.speedy = -25
                        
                elif event.key == pygame.K_DOWN:
                    colidiu_escada = pygame.sprite.spritecollide(player, stairs, False)
                    if colidiu_escada:
                        player.rect.centerx= colidiu_escada[1].rect.centerx
                        player.speedy = 5
                        player.state = CLIMBING


            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X
                elif colidiu_escada:
                    if event.key == pygame.K_UP:
                        player.speedy = 0 

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

#Carrega a musica do jogo
pygame.mixer.music.load(path.join(snd_dir, 'TheAvengersTheme.mp3'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)




# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize as setas do teclado para andar e pular.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
