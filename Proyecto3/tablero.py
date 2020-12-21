import sys, pygame
from pygame.locals import *
from pygame import surface
from algoritmoGenetico import *
from clases import *

#Tamano ventana
size = (700,700)
BLANCO=(255,255,255)
screen=pygame.display.set_mode(size)
screen.fill(BLANCO)
run=True

#Matriz de objetos en el tablero
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



#Se crea el panal con la primera generacion inicial de abejas
panal=panal((25,25),generarPoblacionInicialDeAbejas(10,(25,25)))
matriz[25][25]=panal
screen.blit(panal.imagen,(14*25,14*25))




#Primera generacion de flores
flores=generarPoblacionInicialDeFlores(25)
for i in flores:
    pygame.draw.rect(screen,i.colorDeFlor,[i.posicion[0]*14,i.posicion[1]*14,14,14])




#loop de la simulacion
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos

    #se actualiza
    pygame.display.flip()

pygame.quit() #Se cierra pygame del todo, para rapido rendimiento