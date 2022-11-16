import pygame
import random
import os;
from pygame.locals import *
from sys import exit;
from random import randint

pygame.init()

# declaraçao de variaveis

#cores

PRETO = (0,0,0)
BRANCO = (255,255,255)

# DIMENSOES DA JANELA

largura = 640
altura = 480

# movimento das bolas

xb = 10
yb = random.randint(0,400)

xv = 250
yv = 80

xv1 = 50
yv1 = 200

xv2 = 300
yv2 = 150

xv3 = 550
yv3 = 70
pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)
comandos = pygame.key.get_pressed();
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption ('Chuva de Bolas')



#criando um loop infinito

while True:
    
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
    
    # contrução de linhas e da bola
    
    bola_verde1 = pygame.draw.circle(tela, (80,200,80), (xv,yv),25)
    if yv>= altura:
        yv = 0
    yv = yv + 8
    
    bola_verde2 = pygame.draw.circle(tela, (80,200,80), (xv1,yv1),25)
    if yv1>= altura:
        ya1 = 0
    yv1 = yv1 + 10
    
    bola_verde3 = pygame.draw.circle(tela, (80,200,80), (xv2,yv2),25)
    if yv2>= altura:
        yv2 = 0
    yv2 = yv2 + 30
    
    bola_verde4 = pygame.draw.circle(tela, (80,200,80), (xv3,yv3),25)
    if yv3>= altura:
        yv3 = 0
    yv3 = yv3 + 35
    
        
    bola_branca = pygame.draw.circle(tela, (255,255,255), (xb,yb), 10)
 
           
    if bola_branca.colliderect(bola_verde1):
          print('colidiu')
          pontos = pontos - 1
    if bola_branca.colliderect(bola_verde2):
          print('colidiu')
          pontos = pontos - 1
    if bola_branca.colliderect(bola_verde3):
          print('colidiu')
          pontos = pontos - 1 
    if bola_branca.colliderect(bola_verde4):
          print('colidiu')
          pontos = pontos - 1
    tela.blit(texto_formatado,(450,40))
    pygame.display.update() # atualiza o jogo
    