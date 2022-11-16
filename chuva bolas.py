import os # faz operaçoes  e automaçoes
import random # numeros aleatorios
from random import randint
from sys import exit # fechar janela

import pygame # inicializa todas as funçoes
from pygame.locals import * #submodulo local importando todas as funcoes

pygame.init()

# musica de fundo

pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load('BoxCat Games - Passing Time.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_jump.wav')
barulho_colisao.set_volume(1)


#cores

PRETO = (0,0,0)
BRANCO = (255,255,255)

# Tela de start


# DIMENSOES DA JANELA
largura = 640
altura = 480
tela = pygame.display.set_mode((largura,altura))



# Posição das bolas
xb = 10; yb = random.randint(0,400)
xv = 250; yv = 80
xv1 = 50; yv1 = 50
xva = 200; yva = 400
xv2 = 300; yv2 = 150
xv3 = 350; yv3 = 100
xve = 500; yve = 100
xr = 550; yr = 70


gameover = pygame.image.load('gameover.png')
pontos = 0
fonte = pygame.font.SysFont ('arial', 40, True, True)
comandos = pygame.key.get_pressed()
relogio = pygame.time.Clock()
pygame.display.set_caption ('Chuva de bolas')

#criando um loop infinito

inicio = True
while inicio:
    
    relogio.tick(10)
    tela.fill((0,0,0)) 
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get(): # LOOp´DE CONTROLE DE EVENTO
        if event.type == QUIT: #janela fecha
            pygame.quit() #terminando a aplicaçao pygame    
            exit()
                    
    if pygame.key.get_pressed()[K_a]:
          xb = xb - 10
    if pygame.key.get_pressed()[K_d]:
          xb = xb + 10
    if pygame.key.get_pressed()[K_w]:
          yb = yb - 10 
    if pygame.key.get_pressed()[K_s]:
          yb = yb + 10
    
    # contrução da bola
    
    bola_verde = pygame.draw.circle(tela, (80,200,80), (xv,yv),25)
    if yv>= altura:
        yv = 0
    yv = yv + 35

    bola_verde1 = pygame.draw.circle(tela, (100,200,80), (xv1,yv1),25)
    if yv1>= altura:
        yv1 = 0
    yv1 = yv1 + 35
    
    bola_verde2 = pygame.draw.circle(tela, (80,200,80), (xv2,yv2),25)
    if yv2>= altura:
        yv2 = 0
    yv2 = yv2 + 25
    
    bola_verde3 = pygame.draw.circle(tela, (80,200,80), (xv3,yv3),25)
    if yv3>= altura:
        yv3 = 0
    yv3 = yv3 + 25

    bola_vermelha = pygame.draw.circle(tela, (255,0,0), (xve,yve),25)
    if yve>= altura:
        yve = 0
    yve = yve + 35
    
    bola_rosa = pygame.draw.circle(tela, (200,0,200), (xr,yr),25)
    if yr>= altura:
        yr = 0
    yr = yr + 25

    bola_azul = pygame.draw.circle(tela, (20,20,200), (xva,yva),25)
    if yva>= altura:
        yva = 0
    yva = yva + 35  

    bola_branca = pygame.draw.circle(tela, (255,255,255), (xb,yb), 10)
 
     # Colisoes
           
    if bola_branca.colliderect(bola_verde):
          print('colidiu')
          pontos = pontos - 30
          barulho_colisao.play
    if bola_branca.colliderect(bola_verde1):
          print('colidiu')
          pontos = pontos - 30
          barulho_colisao.play
    if bola_branca.colliderect(bola_verde2):
          print('colidiu')
          pontos = pontos - 30
          barulho_colisao.play
    if bola_branca.colliderect(bola_verde3):
          print('colidiu')
          pontos = pontos - 30
          barulho_colisao.play
    if bola_branca.colliderect(bola_rosa):
          print('+10')
          pontos = pontos + 50 
          barulho_colisao.play

    if bola_branca.colliderect(bola_vermelha):
          print('colidiu')
          pontos = pontos - 40
          barulho_colisao.play

    if bola_branca.colliderect(bola_azul):
        print('colidiu')
        pontos = pontos + 10
        barulho_colisao.play

    tela.blit(texto_formatado, (400,40))
    
# gameover 		
   
    if(pontos <= -200):
        inicio = False
    pygame.display.update() # atualiza o jogo

    tela.blit(texto_formatado,(400,40))
   
    # <<<<<<<<<<<< FAZ O DESENHO DO GAME OVER AQUI E FECHA O JOGO >>>>>>>>>>>>>>>>>

tela.blit (gameover, (0, 0))	# <<<<<<<<<<<< faz exibir a imagem do gameover na tela
pygame.display.update ()	#<<<<<<<<<<<<<<  Atualiza a tela (exibir a imagem)
pygame.time.delay (3000)	# <<<<<<<<<< Espera 3 segundos para poder fechar a janela
pygame.quit () 			# <<<<<<<<< Fecha a janela