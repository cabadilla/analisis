import sys, pygame
from pygame.locals import *
from Casillas import Casillas
from pygame import surface

pygame.init()

#definiendo colores
NEGRO=[0,0,0]
BLANCO=[255,255,255]

#tamano ventana
size = (1200,500)
global screen
screen=pygame.display.set_mode(size)
screen.fill(BLANCO)


class Tablero:
    def __init__(self):
        self.matrizCasillas=[]
        self.matrizLogica=[]
        self.crearTablero()
        

    
    def crearTablero(self):
        for i in range(0,11):
            arreglo=[]
            for j in range(0,11):
                casilla=Casillas([i*50,j*50])
                arreglo.append(casilla)
                screen.blit(casilla.image,casilla.coor)
            self.matrizCasillas.append(arreglo)
            
    def verClick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                


tablero=Tablero()


#loop del juego
while True:
    
    tablero.verClick()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #imprime en la consola el botón presionado y su posición en ese momento
            print(u'botón {} presionado en la posición {}'.format(event.button, event.pos))

    
  

   


   

    #se actualiza
    pygame.display.flip()
    
