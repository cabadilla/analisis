import sys, pygame
from pygame.locals import *
from Casillas import Casillas
from Player import Player
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
        self.jugadores=[]
        self.crearTablero()
        self.crearJugadores()
        
    def crearTablero(self):
        for i in range(0,11):
            arreglo=[]
            for j in range(0,11):
                casilla=Casillas([i*50,j*50])
                arreglo.append(casilla)
                screen.blit(casilla.image,casilla.coor)
            self.matrizCasillas.append(arreglo)

    def crearJugadores(self):
        Hplayer=Player("Player", pygame.Color(51, 133, 255))                  #Creacion del jugador Humano
        A1player=Player("Algoritmo 1", pygame.Color(255, 106, 51))            #Creacion del jugador Algoritmo 1
        A2player=Player("Algoritmo 2", pygame.Color(157, 255, 51))            #Creacion del jugador Algoritmo 2
        NormalFont=pygame.font.SysFont("monospace", 18)
        screen.blit(NormalFont.render(Hplayer.nombre+": "+str(Hplayer.puntuacion), 1, Hplayer.color), (620, 22))
        screen.blit(NormalFont.render(A1player.nombre+": "+str(A1player.puntuacion), 1, A1player.color), (620, 142))
        screen.blit(NormalFont.render(A2player.nombre+": "+str(A2player.puntuacion), 1, A2player.color), (620, 262))
        self.jugadores.append(Hplayer)
        self.jugadores.append(A1player)
        self.jugadores.append(A2player)

    def verClick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("")  #Daba error porque no habia nada aqui entonces puse un print vacio 

    def plusPuntuacion(self):            # metodo de prueba para aumentar la puntuacion de los jugadores y que se pueda actualizar
        for player in self.jugadores:
            player.aumentaPuntuacion(1)

    def updateJugadores(self):           #metodo que actualiza los labels de cada jugador
        i=22
        screen.fill(pygame.Color(255,255,255), (600,20,600,270)) # elimina todo lo que tenga en esas cordenadas para poder reemplazar el label
        NormalFont=pygame.font.SysFont("Times New Roman", 22)
        for player in self.jugadores:
            screen.blit(NormalFont.render(player.nombre+": "+str(player.puntuacion), 1, player.color), (620, i))
            i+=120

tablero=Tablero()

#loop del juego
while True:
    
    #tablero.verClick()
    tablero.plusPuntuacion()
    tablero.updateJugadores()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #imprime en la consola el botón presionado y su posición en ese momento
            print(u'botón {} presionado en la posición {}'.format(event.button, event.pos))

    #se actualiza
    pygame.display.flip()
    
