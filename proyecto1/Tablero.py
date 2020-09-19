import sys, pygame
from pygame.locals import *
from Casillas import Casillas
from Player import Player
from pygame import surface
from fichas import *

pygame.init()

#definiendo colores
NEGRO=[0,0,0]
BLANCO=[255,255,255]

#tamano ventana
size = (1250,500)
global screen
screen=pygame.display.set_mode(size)
screen.fill(BLANCO)

global fichaEl

class Tablero:
    def __init__(self):
        self.fabricaDeFichas=fabricaDeFichas()
        self.matrizCasillas=[]
        self.matrizLogica=[]
        self.jugadores=[]
        self.crearTablero()
        self.crearJugadores()
        self.turno=0
        
        
        
    def crearTablero(self):
        for i in range(0,11):
            arreglo=[]
            for j in range(0,11):
                casilla=Casillas([i*50,j*50],"imagenes/cuadro.png")
                arreglo.append(casilla)
                screen.blit(casilla.image,casilla.coor)
            self.matrizCasillas.append(arreglo)


    def agregarFichas(self):
        array=[]
        for i in range(5):
            array.append(self.fabricaDeFichas.bolsa.pop())

        return array

    def agregarUnaFicha(self):
        return self.fabricaDeFichas.bolsa.pop()

    def crearJugadores(self):
        rect1 = (750, 50, 250, 50)
        rect2 = (750, 140, 250, 50)
        rect3 = (750, 230, 250, 50)

        pygame.draw.rect(screen, NEGRO, rect1, 2)
        pygame.draw.rect(screen, NEGRO, rect2, 2)
        pygame.draw.rect(screen, NEGRO, rect3, 2)

        Hplayer=Player("Player", pygame.Color(51, 133, 255),rect1)                  #Creacion del jugador Humano
        Hplayer.fichasDisponibles=self.agregarFichas()

        A1player=Player("Algoritmo 1", pygame.Color(255, 106, 51),rect2)            #Creacion del jugador Algoritmo 1
        A1player.fichasDisponibles=self.agregarFichas()

        A2player=Player("Algoritmo 2", pygame.Color(157, 255, 51),rect3)            #Creacion del jugador Algoritmo 2
        A2player.fichasDisponibles=self.agregarFichas()
       
        NormalFont=pygame.font.SysFont("monospace", 18)
        screen.blit(NormalFont.render(Hplayer.nombre+": "+str(Hplayer.puntuacion), 1, Hplayer.color), (650, 22))
        screen.blit(NormalFont.render(A1player.nombre+": "+str(A1player.puntuacion), 1, A1player.color), (650, 112))
        screen.blit(NormalFont.render(A2player.nombre+": "+str(A2player.puntuacion), 1, A2player.color), (650, 212))
        self.jugadores.append(Hplayer)
        self.jugadores.append(A1player)
        self.jugadores.append(A2player)

        
    def cambiarTurno(self):
        if(self.turno==2):
            self.turna=0
        else:
            self.turno+=1

    def dibujarTablero(self):
        for i in self.matrizCasillas:
            for j in i:
                screen.blit(j.image,j.coor)


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


    def dibujarFichasDisponibles(self):
        #pone dentro del rectangulo las fichas que tienen los jugadores
        cont1=50
        for i in self.jugadores:
            cont2=750
            for j in i.fichasDisponibles:
                j.coor[0]=cont2
                j.coor[1]=cont1
                screen.blit(j.image,j.coor)
                cont2+=50
            cont1+=90

    def fichaSeleccionada(self,x,y):
                for i in self.jugadores[self.turno].fichasDisponibles:
                    if (x>i.coor[0]) & (x<(i.coor[0]+50)):
                        fichaEl=i
                        screen.blit(i.image,[610,400])


    '''def ponerFicha(self,x,y):
        for i in self.matrizCasillas:
            for j in i:
                if ((x>=j.coor[0]) && (x<=(j.coor[0]+50)) && (y<=j.coor[1]) && (y<=(j.coor[1]+50))):
                    self.matrizCasillas[i][j]='''


    def verClick(self,x,y):
        if(x>730):
            self.fichaSeleccionada(x,y)
        '''else:
            self.ponerFicha(x,y)'''

                    

            
#letras de donde va la ficha a escoger
NormalFont=pygame.font.SysFont("monospace", 18)
screen.blit(NormalFont.render("Ficha seleccionada: ", 1, NEGRO), (610, 350))

#crea el tablero y llama a las funciones
tablero=Tablero()


#loop del juego
while True:
    
    #tablero.verClick()
    #tablero.plusPuntuacion()
    #tablero.updateJugadores()

    tablero.dibujarFichasDisponibles()
    tablero.dibujarTablero()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            tablero.verClick(x,y)
            

    #se actualiza
    pygame.display.flip()
    
