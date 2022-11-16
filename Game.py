import os
import random
from random import randint
from sys import exit

import pygame
from pygame.locals import *

pygame.init()

# declaraçao de variaveis
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')
print(diretorio_principal)

#cores
PRETO = (0,0,0)
BRANCO = (255,255,255)

# DIMENSOES DA JANELA
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))		#<<<<<<<<<<<<<<<<< Movi a tela para cá <<<<<<<<<<<<<<<<

# Posição das bolas			<<<<<<<<<<<<<<<< agrupei em uma linha só por coordendas na forma (x,y) <<<<<<<<<<<<<<<<
xb = 10; yb = random.randint(0,400)
xv = 250; yv = 80
xv1 = 50; yv1 = 50
xva = 200; yva = 400
xv2 = 300; yv2 = 150
xv3 = 350; yv3 = 100
xve = 500; yve = 100
xr = 550; yr = 70

#minhas imagens				<<<<<<<<<<<<<<<<<<<< Imagens adicionadas aqui >>>>>>>>>>>>>>>>>>>>>
gameover = pygame.image.load ('gameover.png')

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)
comandos = pygame.key.get_pressed();
relogio = pygame.time.Clock()
pygame.display.set_caption ('Chuva de Bolas')

#criando um loop infinito
inicio = True		# <<<<<<<<<<< uma variável para começar o jogo no while, e ajudar a sair do jogo para um gameover quando false >>>>>>>>>>
while inicio:
    
    relogio.tick(10)
    tela.fill((0,0,0)) # pércepcao do movimento do circulo
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get(): # LOO´DE CONTROLE DE EVENTO
        if event.type == QUIT:
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
    yv = yv + 30

    bola_verde1 = pygame.draw.circle(tela, (100,200,80), (xv1,yv1),25)
    if yv1>= altura:
        yv1 = 0
    yv1 = yv1 + 30
	    
    bola_verde2 = pygame.draw.circle(tela, (80,200,80), (xv2,yv2),25)
    if yv2>= altura:
        yv2 = 0
    yv2 = yv2 + 20
    
    bola_verde3 = pygame.draw.circle(tela, (80,200,80), (xv3,yv3),25)
    if yv3>= altura:
        yv3 = 0
    yv3 = yv3 + 20

    bola_vermelha = pygame.draw.circle(tela, (255,0,0), (xve,yve),25)
    if yve>= altura:
        yve = 0
    yve = yve + 30
    
    bola_rosa = pygame.draw.circle(tela, (200,0,200), (xr,yr),25)
    if yr>= altura:
        yr = 0
    yr = yr + 20

    bola_azul = pygame.draw.circle(tela, (20,20,200), (xva,yva),25)
    if yva>= altura:
        yva = 0
    yva = yva + 35  

    bola_branca = pygame.draw.circle(tela, (255,255,255), (xb,yb), 10)
 
    # Colisoes
    if bola_branca.colliderect(bola_verde):
          print('colidiu')
          pontos = pontos - 10
    if bola_branca.colliderect(bola_verde1):
          print('colidiu')
          pontos = pontos - 1
    if bola_branca.colliderect(bola_verde2):
          print('colidiu')
          pontos = pontos - 10

    if bola_branca.colliderect(bola_verde3):
          print('colidiu')
          pontos = pontos - 10

    if bola_branca.colliderect(bola_rosa):
          print('+10')
          pontos = pontos + 20 

    if bola_branca.colliderect(bola_vermelha):
          print('colidiu')
          pontos = pontos - 10

    if bola_branca.colliderect(bola_azul):
        print('colidiu')
        pontos = pontos + 10
    
    tela.blit(texto_formatado,(400,40))
    
    # gameover 		<<<<<<<<<<<<<<<<<< aqui coloquei um gameover se tiver com -200 ou menos <<<<<<<<<<<<<<<<
    if (pontos <= -200) :
        inicio = False
        
    pygame.display.update() # atualiza o jogo

# <<<<<<<<<<<< FAZ O DESENHO DO GAME OVER AQUI E FECHA O JOGO >>>>>>>>>>>>>>>>>

tela.blit (gameover, (0, 0))	# <<<<<<<<<<<< faz exibir a imagem do gameover na tela
pygame.display.update ()		#<<<<<<<<<<<<<<  Atualiza a tela (exibir a imagem)
pygame.time.delay (3000)		# <<<<<<<<<< Espera 3 segundos para poder fechar a janela
pygame.quit () 					# <<<<<<<<< Fecha a janela