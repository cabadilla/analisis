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
        self.jugadores=[]
        self.crearTablero()
        self.crearJugadores()
        self.turno=0
        self.fichaEl=Casillas([0,0],"imagenes/cuadro.png")
        self.xy=[]
        self.pixeles=50
        self.colFil=11
        self.fichasPuestas=[]
        
        
        
    def crearTablero(self):
        for i in range(0,11):
            arreglo=[]
            for j in range(0,11):
                casilla=Casillas([i*50,j*50],"imagenes/cuadro.png")
                arreglo.append(casilla)
                screen.blit(casilla.image,casilla.coor)
                #casilla.cordenadasMatriz=(i,j)
            self.matrizCasillas.append(arreglo)


    def agrandarTablero(self):
        self.pixeles=self.pixeles-5
        self.colFil+=1
        nuevaMatriz=[]

        rect = (0, 0, 600, 1000)
        pygame.draw.rect(screen, BLANCO, rect,0)
        #pygame.display.flip()

        for i in range(0,self.colFil):
            arreglo=[]
            for j in range(0,self.colFil):
                casilla=Casillas([i*self.pixeles,j*self.pixeles],"imagenes/cuadro.png")
                arreglo.append(casilla)
                screen.blit(casilla.image,casilla.coor)
                casilla.cordenadasMatriz=(i,j)
                pygame.display.flip()
            nuevaMatriz.append(arreglo)
        
        self.matrizCasillas=nuevaMatriz

        for i in self.fichasPuestas:
            i.coor=self.matrizCasillas[i.cordenadasMatriz[0]][i.cordenadasMatriz[1]].coor
            i.cambiarEscala((self.pixeles,self.pixeles))
            self.matrizCasillas[i.cordenadasMatriz[0]][i.cordenadasMatriz[1]]=i
            screen.blit(i.image,i.coor)

        

        

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
            self.turno=0
        else:
            self.turno+=1


    def sacarFicha(self):
        for i in self.jugadores[self.turno].fichasDisponibles:
            if i.coor==self.xy:
                self.jugadores[self.turno].fichasDisponibles.remove(i)
                self.jugadores[self.turno].fichasDisponibles.append(self.fabricaDeFichas.bolsa.pop())
                tablero.dibujarFichasDisponibles()


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
            if ((x>i.coor[0]) & (x<(i.coor[0]+50)) & (y>=i.coor[1]) & (y<=(i.coor[1]+50))):
                self.xy=i.coor
                self.fichaEl=i
                screen.blit(i.image,[610,400])

    #mueve las fichas dependiendo el numero lo hace a la derecha o a la izquierda
    def moverFichas(self,x):
        for i in self.matrizCasillas:
            for j in i:
                if j.estado!=0:
                    if x==1:
                        j.cordenadasMatriz=(j.cordenadasMatriz[0],j.cordenadasMatriz[1]+1)
                    else:
                        j.cordenadasMatriz=(j.cordenadasMatriz[0]+1,j.cordenadasMatriz[1])       
     
#calcula  si tiene que correr las fichas hacia algun lado
    def calcular(self):
        for i in self.matrizCasillas:
            if (i[0].estado!=0):
                self.moverFichas(1)
                return True

            elif (i[self.colFil-2].estado!=0):
                return True
        
        for i in self.matrizCasillas[0]:
            if (i.estado!=0):
                self.moverFichas(0)
                return True
                
        for i in self.matrizCasillas[self.colFil-1]:
            if (i.estado!=0):
                return True

        return False

    def ponerFicha(self,x,y):
        for i in range(len(self.matrizCasillas)):
            for j in range (len(self.matrizCasillas[i])):
                if (x>=self.matrizCasillas[i][j].coor[0]) & (x<=(self.matrizCasillas[i][j].coor[0]+50)) & (y>=self.matrizCasillas[i][j].coor[1]) & (y<=(self.matrizCasillas[i][j].coor[1]+50)):
                    self.sacarFicha()
                    self.fichaEl.coor=self.matrizCasillas[i][j].coor
                    self.fichaEl.cordenadasMatriz=(i,j)
                    self.matrizCasillas[i][j]=self.fichaEl
                    self.fichasPuestas.append(self.fichaEl)
                    screen.blit(self.fichaEl.image,self.fichaEl.coor)
        self.cambiarTurno()


    def verClick(self,x,y):
        if(x>730):
            self.fichaSeleccionada(x,y)
        else:
            self.ponerFicha(x,y)

                    

            
#letras de donde va la ficha a escoger
NormalFont=pygame.font.SysFont("monospace", 18)
screen.blit(NormalFont.render("Ficha seleccionada: ", 1, NEGRO), (610, 350))

#crea el tablero y llama a las funciones
tablero=Tablero()
tablero.dibujarFichasDisponibles()

#loop del juego
while True:
    
    #tablero.verClick()
    #tablero.plusPuntuacion()
    #tablero.updateJugadores()

    #ve constantemente si tiene que correr las fichas
    if tablero.calcular():
        tablero.agrandarTablero()


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            tablero.verClick(x,y)
            

    #se actualiza
    pygame.display.flip()
    
