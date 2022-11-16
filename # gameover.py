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