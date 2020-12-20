import sys, pygame
from pygame.locals import *
from pygame import surface
from algoritmoGenetico import *
from clases import *

#tamano ventana
size = (700,700)
global screen
BLANCO=(255,255,255)
screen=pygame.display.set_mode(size)
screen.fill(BLANCO)
run=True

#matriz de objetos en el tablero
matriz=[]
image=pygame.image.load("imagenes/cuadro.png")
image=pygame.transform.scale(image,(14,14))

#Se cuadricula  el tablero
for i in range(0,50):
    arreglo=[]
    for j in range(0,50):
        screen.blit(image,(i*14,j*14))
        arreglo.append(None)
    matriz.append(arreglo)

#cordenadas del panal
panal=panal((25,25),generarPoblacionInicialDeAbejas(10,(25,25)))
matriz[25][25]=panal
screen.blit(panal.imagen,(14*25,14*25))

#se crea las primeras flores
flores=generarPoblacionInicialDeFlores(25)
print(flores)
for i in flores:
    pygame.draw.rect(screen,i.colorFavorito,[i.posicion[0]*14,i.posicion[1]*14,14,14])

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