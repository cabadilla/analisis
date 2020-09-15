import sys, pygame
from pygame.locals import *
from Casillas import Casillas
from pygame import surface
pygame.init()

#definiendo colores
NEGRO=[0,0,0]
BLANCO=[255,255,255]
size = (1500,800)
global screen
screen=pygame.display.set_mode(size)


#loop del juego
while True:
    
    image=pygame.image.load("imagenes/cuadro.pgn")
    image=

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #imprime en la consola el botón presionado y su posición en ese momento
            print(u'botón {} presionado en la posición {}'.format(event.button, event.pos))

    
    
    
    screen.fill(BLANCO)


   

    #se actualiza
    pygame.display.flip()