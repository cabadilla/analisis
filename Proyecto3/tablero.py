import sys, pygame
from pygame.locals import *
from pygame import surface
from algoritmoGenetico import *
from clases import *

#tamano ventana
size = (500,500)
global screen
BLANCO=(255,255,255)
screen=pygame.display.set_mode(size)
screen.fill(BLANCO)
run=True

#matriz de objetos en el tablero
matriz=[]
image=pygame.image.load("imagenes/cuadro.png")
image=pygame.transform.scale(image,(50,50))

#Se cuadricula  el tablero
for i in range(0,10):
    arreglo=[]
    for j in range(0,10):
        screen.blit(image,(i*50,j*50))
        arreglo.append(None)
    matriz.append(arreglo)

#cordenadas del panal
panal=panal((5,5),generarPoblacionInicialDeAbejas(10,(5,5)))
matriz[5][5]=panal
print(matriz)
#loop del juego
while run:

    #ve constantemente si tiene que correr las fichas


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos

    #se actualiza
    pygame.display.flip()