# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
fnt_dir = path.join(path.dirname(__file__), 'Fonte')

# Dados gerais do jogo.
TITULO = 'Peter Kong'
WIDTH = 1024 #largura da tela
HEIGHT = 800 # Altura da tela é 800, coloquei 600 pra rodar no meu pc
TILE_SIZE = 32 # Tamanho de cada tile (cada tile é um quadrado) 32 #24
PLAYER_WIDTH = 32  #32 #24    
PLAYER_HEIGHT = 32 #32 #24
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 2
# Define a velocidade inicial no pulo
JUMP_SIZE = 20
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
	[0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
	[0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
	[0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
	[0,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,2,3,0],
	[0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0],
	[0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0],
	[0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0],
	[0,0,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,0,0],
	[0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
	[3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,2,3,3,3,3],
	[0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0],
	[0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0],
	[0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	
]

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
CLIMBING = 3
MENU = 4
JOGO = 5
ENDGAME = 6
INIT = 7
QUIT = 10

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
	def __init__(self, player_img, row, column, blocks, stairs, speedx, speedy):

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

		self.speedx = speedx
		self.speedy = speedy
  

	# Metodo que atualiza a posição do personagem
	def update(self):
		# Função para tratar dos movimentos em X e Y.

		# Codigo que trata as colisoes com escada
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


# Classe do Thanos
class Thanos(pygame.sprite.Sprite):

	# Construtor da classe.
	def __init__(self, thanos_img, row, column, blocks):


		# Construtor da classe pai (Sprite).
		pygame.sprite.Sprite.__init__(self)

		# Ajusta o tamanho da imagem

		thanos_img = pygame.transform.scale(thanos_img, (96, 96))#96,96 - Luca #48,48 - Lucca

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
		self.speedx = 3
		self.speedy = 3

	# Metodo que atualiza a posição do personagem
	def update(self):
		# Função de atualizar o movimento em x e em y

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
			self.speedx = 3
		elif self.rect.right >= WIDTH:
			self.rect.right = WIDTH - 1
			self.speedx = -3
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

# Classe Gamora que representa a personagem Gamora
class Gamora(pygame.sprite.Sprite):

	# Construtor da classe.
	def __init__(self, gamora_img, row, column, blocks):

		# Construtor da classe pai (Sprite).
		pygame.sprite.Sprite.__init__(self)

		# Define estado atual
		# Usamos o estado para decidir se o jogador pode ou não pular
		self.state = STILL

		# Ajusta o tamanho da imagem
		gamora_img = pygame.transform.scale(gamora_img, (PLAYER_WIDTH *2, PLAYER_HEIGHT *2))

		# Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
		self.image = gamora_img
		# Detalhes sobre o posicionamento.
		self.rect = self.image.get_rect()

		# Guarda o grupo de blocos para tratar as colisões
		self.blocks = blocks

		# Posiciona o personagem
		# row é o índice da linha embaixo do personagem
		self.rect.x = column * TILE_SIZE
		self.rect.bottom = row * TILE_SIZE

		self.speedx = 0
		self.speedy = 0

	def update(self):
		# Função que define as colisões com blocos

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
				

class Meteor(pygame.sprite.Sprite):
	
	# Construtor da classe.
	def __init__(self, meteor_img, X, Y, blocks):
		
		# Construtor da classe pai (Sprite).
		pygame.sprite.Sprite.__init__(self)

		meteor_img = pygame.transform.scale(meteor_img, (64, 64))
		
		# Carregando a imagem de fundo.
		self.image = meteor_img
		
		# Deixando transparente.
		self.image.set_colorkey(BLACK)
		
		# Detalhes sobre o posicionamento.
		self.rect = self.image.get_rect()

		self.blocks = blocks
		
		# Coloca no lugar inicial definido em x, y do constutor
		self.rect.centerx = X
		self.rect.centery = Y
		self.speedx = 2
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
			self.speedx = 2
		elif self.rect.right >= WIDTH:
			self.rect.right = WIDTH - 1
			self.speedx = -2
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

# Classe Tiro que representa a Chuva de Meteoros
class Fireball(pygame.sprite.Sprite):
	
	# Construtor da classe.
	def __init__(self, fireball_img, X, Y):
		
		# Construtor da classe pai (Sprite).
		pygame.sprite.Sprite.__init__(self)
		
		fireball_img = pygame.transform.scale(fireball_img, (32, 64))

		# Carregando a imagem de fundo.
		self.image = fireball_img
		
		# Deixando transparente.
		self.image.set_colorkey(BLACK)
		
		# Detalhes sobre o posicionamento.
		self.rect = self.image.get_rect()
		
		# Coloca no lugar inicial definido em x, y do constutor
		self.rect.centerx = X
		self.rect.centery = Y
		self.speedy = +10

	# Metodo que atualiza a posição da navinha
	def update(self):
		self.rect.y += self.speedy
		
		
		# Se o tiro passar do inicio da tela, morre.
		if self.rect.bottom < 0:
			self.kill()


		
# Carrega todos os assets de uma vez.
def load_assets(img_dir):
	assets = {}
	assets["PLAYER_IMG"] = pygame.image.load(path.join(img_dir, 'StarLord.png')).convert_alpha()
	assets["BLOCK"] = pygame.image.load(path.join(img_dir, 'platform.png')).convert()
	assets["ESCADA"] = pygame.image.load(path.join(img_dir, 'escada.png')).convert()
	assets["BLOCK2"] = pygame.image.load(path.join(img_dir, 'esteira.png')).convert()
	assets["THANOS_IMG"] = pygame.image.load(path.join(img_dir, "Thanos_0.png")).convert()
	assets["THANOS_IMG"].set_colorkey(BLACK) 
	assets["GAMORA_IMG"] = pygame.image.load(path.join(img_dir, "Gamora2.png")).convert()
	assets["GAMORA_IMG"].set_colorkey(BLACK)
	assets["METEOR_IMG"] = pygame.image.load(path.join(img_dir, "Meteor.png")).convert()
	assets["FIREBALL_IMG"] = pygame.image.load(path.join(img_dir, "Fireball.png")).convert()
	assets["background"] = pygame.image.load(path.join(img_dir, "background.png")).convert()
	assets["menu"] = pygame.image.load(path.join(img_dir, "background2.png")).convert()
	assets["boom_sound"] = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))

	return assets


def menu(screen):
	
	#Carrega a musica do jogo
	pygame.mixer.music.load(path.join(snd_dir, 'CarelessWhisper.mp3'))
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(loops=-1)

	assets = load_assets(img_dir)
	background = pygame.transform.scale(assets["menu"], (WIDTH, HEIGHT))
	background_rect = background.get_rect()
	state = MENU
	while state == MENU:
		screen.blit(background,background_rect)
		score_font= pygame.font.Font(path.join(fnt_dir, "i_fink_u_freeky.ttf"),50)
		text_surface= score_font.render("Peter Kong", True, WHITE)
		text_rect= text_surface.get_rect()
		text_rect.centery = (HEIGHT/2)
		text_rect.centerx = (WIDTH/2)
		screen.blit(text_surface, text_rect)
		score_font= pygame.font.Font(path.join(fnt_dir, "i_fink_u_freeky.ttf"),28)
		text_surface= score_font.render("Aperte espaço para começar", True, WHITE)
		text_rect = text_surface.get_rect()
		text_rect.bottom = (HEIGHT -68)
		text_rect.centerx = (WIDTH/2)
		screen.blit(text_surface, text_rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					state = JOGO
		pygame.display.flip()
	return (state)

def endgame(screen):

	#Carrega a musica do jogo
	pygame.mixer.music.load(path.join(snd_dir, 'GloboRural.mp3'))
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(loops=-1)

	assets = load_assets(img_dir)
	background = pygame.transform.scale(assets["menu"], (WIDTH, HEIGHT))
	background_rect = background.get_rect()
	state = MENU
	while state == MENU:
		screen.blit(background,background_rect)
		score_font= pygame.font.Font(path.join(fnt_dir, "i_fink_u_freeky.ttf"),50)
		text_surface= score_font.render("FIM DE JOGO", True, WHITE)
		text_rect= text_surface.get_rect()
		text_rect.centery = (HEIGHT/2)
		text_rect.centerx = (WIDTH/2)
		screen.blit(text_surface, text_rect)
		score_font= pygame.font.Font(path.join(fnt_dir, "i_fink_u_freeky.ttf"),28)
		text_surface= score_font.render("Aperte Espaço para fechar.", True, WHITE)
		text_rect = text_surface.get_rect()
		text_rect.bottom = (HEIGHT -68)
		text_rect.centerx = (WIDTH/2)
		screen.blit(text_surface, text_rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					state = QUIT
		pygame.display.flip()
	return (state)

def game_screen(screen):
	# Variável para o ajuste de velocidade
	clock = pygame.time.Clock()

	# Carrega a musica do jogo
	pygame.mixer.music.load(path.join(snd_dir, 'AvengersTheme8bit.mp3'))
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(loops=-1)
	

	# Carrega assets
	assets = load_assets(img_dir)

	# Carrega o fundo do jogo
	background = pygame.transform.scale(assets["background"] , (WIDTH, HEIGHT))
	background_rect = background.get_rect()

	# Carrega sons do jogo
	boom_sound = assets["boom_sound"]
	
	# Cria um grupo de todos os sprites.
	all_sprites = pygame.sprite.Group()

	# Cria um grupo somente com os sprites de bloco.
	blocks = pygame.sprite.Group()
	# Cria um grupo somente com os sprites de escadas.
	stairs = pygame.sprite.Group()
	# Grupo de inimigos
	inimigos = pygame.sprite.Group()
	# Grupo de meteoros
	mobs = pygame.sprite.Group()


	# Cria Sprite do jogador
	player = Player(assets["PLAYER_IMG"], 24, 1, blocks, stairs, 0, 0)
	# Cria Sprite do Thanos
	thanos = Thanos(assets["THANOS_IMG"], 9, 6, blocks)
	# Cria Sprite da Gamora
	gamora = Gamora(assets["GAMORA_IMG"], 4, 13, blocks)



	#Adiciona o thanos e a gamora no grupo de inimigos
	inimigos.add(thanos, gamora)


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


	
	# Adiciona o player, gamora e thanos por último
	all_sprites.add(player)
	all_sprites.add(inimigos)

	# Estado que define o jogo rodando
	PLAYING = 0
	# Estado que define quando o jogo acaba
	DONE = 1
	#
	COLLISION = 2

	ENDGAME = 6
	# Vidas do jogador
	lives = 3

	#Tempo no jogo
	t0 = pygame.time.get_ticks()
	t3 = pygame.time.get_ticks()

	state = PLAYING
	while state != QUIT and state != ENDGAME:

		# Ajusta a velocidade do jogo.
		clock.tick(FPS)

		# Processa os eventos (mouse, teclado, botão, etc).
		for event in pygame.event.get():

			# Verifica se foi fechado.
			if event.type == pygame.QUIT:
				state = QUIT

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
					else:
						player.jump()
						 

				elif event.key == pygame.K_DOWN:
					player.rect.y+=5
					colidiu_escada = pygame.sprite.spritecollide(player, stairs, False)
					player.rect.y-=5
					if colidiu_escada:
						player.rect.centerx= colidiu_escada[0].rect.centerx
						player.speedy = 5
						player.state = CLIMBING

			# Verifica se soltou alguma tecla.
			if event.type == pygame.KEYUP:

				# Dependendo da tecla, altera o estado do jogador.
				if event.key == pygame.K_LEFT:
					player.speedx += SPEED_X
				elif event.key == pygame.K_RIGHT:
					player.speedx -= SPEED_X
				elif event.key == pygame.K_UP:
					player.speedy = 0 
			
					

		# FAZER CÓDIGO PARA LANÇAR METEOROS AO TEMPO

		
		#Adiciona meteoros ao grupo dos inimigos
		t1 = pygame.time.get_ticks()
		if t1 - t0 > 12500:
			m = Meteor(assets["METEOR_IMG"], thanos.rect.centerx, thanos.rect.centery, blocks)
			all_sprites.add(m)
			mobs.add(m)
			t0 = pygame.time.get_ticks()

		#Adiciona fireballs ao grupo de inimigos
		t2 = pygame.time.get_ticks()
		if t2 - t3 > 500:
			f = Fireball(assets["FIREBALL_IMG"], thanos.rect.centerx, thanos.rect.centery)
			all_sprites.add(f)
			mobs.add(f)
			t3 = pygame.time.get_ticks()
		# Depois de processar os eventos.
		# Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
		all_sprites.update()

		if state == PLAYING:
			# Colisões
			# Verifica se houve colisão entre Thanos e Gamora (Perder, e Ganhar o jogo)
			hits = pygame.sprite.spritecollide(player, inimigos, False)
			if hits:
				player.kill()
				state = ENDGAME

				#pygame sprite collide mask
			hits_M = pygame.sprite.spritecollide(player, mobs, False, collided = None)
			if hits_M:
				# Toca o som da colisão
				boom_sound.play()
				player.kill()
				lives -= 1
				state = COLLISION

		elif state == COLLISION:
			if lives == 0:
				state = ENDGAME
			else:
				state = PLAYING
				player = Player(assets["PLAYER_IMG"], 24, 1, blocks, stairs, player.speedx, player.speedy)
				all_sprites.add(player)
		

		# A cada loop, redesenha o fundo e os sprites
		screen.fill(BLACK)
		screen.blit(background, background_rect)

		# Desenha a imagem maior do player mantendo o tamanho do retângulo
		img = player.image
		rect = player.rect
		player.image = pygame.transform.scale(img, (PLAYER_WIDTH+8, PLAYER_HEIGHT+8))
		player.rect = player.image.get_rect()
		player.rect.centerx = rect.centerx
		player.rect.bottom = rect.bottom	
		# Desenha todos sprites		
		all_sprites.draw(screen)
		# Redefine o retângulo e a imagem do player e do meteoro
		player.image = img
		player.rect = rect

		# Desenha as vidas
		score_font= pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
		text_surface = score_font.render(chr(9829) * lives, True, RED)
		text_rect = text_surface.get_rect()
		text_rect.topleft = (10, 10)
		screen.blit(text_surface, text_rect)

		# Depois de desenhar tudo, inverte o display.
		pygame.display.flip()
	return state
