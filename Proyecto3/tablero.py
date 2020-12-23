import sys, pygame
from pygame.locals import *
from pygame import surface
from algoritmoGenetico import *
from clases import *
from random import randint
import time

#Tamano ventana
size = (700,700)
BLANCO=(255,255,255)
screen=pygame.display.set_mode(size)
screen.fill(BLANCO)
run=True



def calcularPuntosDif(dir,x,y):
    diccionario={
        'N':(x-1,y+1),
        'S':(x+1,y-1),
        'E':(x+1,y+1),
        'O':(x-1,y-1),
        'NE':(x,y+1),
        'NO':(x-1,y),
        'SE':(x+1,y),
        'SO':(x,y-1)
    }
    return diccionario[dir]
    
def calcularPuntos(dir,x,y):
    diccionario={
        'N':(x-1,y),
        'S':(x+1,y),
        'E':(x,y+1),
        'O':(x,y-1),
        'NE':(x-1,y+1),
        'NO':(x-1,y-1),
        'SE':(x+1,y+1),
        'SO':(x+1,y-1)
    }

    return diccionario[dir]

def calcularPuntosRelleno(dir,x,y):
    diccionario={
        'N':(x,y+1),
        'S':(x,y-1),
        'E':(x+1,y),
        'O':(x-1,y),
        'NE':(x+1,y),
        'NO':(x,y+1),
        'SE':(x,y-1),
        'SO':(x-1,y)
    }
    return diccionario[dir]

def hallarTriangulo(abeja):
    listaPuntosLimiteSuperior=[]
    listaPuntosLimitesInferior=[]
    listaTriangulo=[]
    actual=(25,25)
    for i in range(20):
        actual=calcularPuntos(abeja.direccionFavorita[0],actual[0],actual[1])
        listaPuntosLimiteSuperior.append(actual)
        
    actual=(25,25)
    for i in range(20):
        actual=calcularPuntosDif(abeja.direccionFavorita[0],actual[0],actual[1])
        listaPuntosLimitesInferior.append(actual)

    for i in range (20):
        actual=listaPuntosLimiteSuperior[i]
        while actual !=listaPuntosLimitesInferior[i]:
            actual=(calcularPuntosRelleno(abeja.direccionFavorita[0],actual[0],actual[1]))
            listaTriangulo.append(actual)
    return listaTriangulo


#se inicia el recorrido
def recorridoUnaAbeja(abeja,matrizTablero):
    triangulo=hallarTriangulo(abeja)
    posiblesFlores=[]
    for i in range(15):
        posibleFlor=triangulo[randint(0,len(triangulo)-1)]
        posiblesFlores.append(posibleFlor)
    
    for i in posiblesFlores:
        if(matrizTablero[i[0]][i[1]]!=None):
            abeja.polem.append(i)
            matrizTablero[i[0]][i[1]].abejas.append(abeja)

    return abeja

def recorridoGeneracion(generacionAbejas,matriz):
    finalGeneracion=[]
    for i in generacionAbejas:
        finalGeneracion.append(recorridoUnaAbeja(i,matriz))

    nuevaGeneracion=(cruceAbejas(finalGeneracion))
    return nuevaGeneracion

def inciarGeneraciones(pana,flores,matrizT):
    nueva=recorridoGeneracion(pana.enjambre,matrizT)
    pana.enjambre=nueva
    floresNuevas=cruceFlores(flores)
    return pana,floresNuevas


#Se crea el panal con la primera generacion inicial de abejas
panal=panal((25,25),generarPoblacionInicialDeAbejas(10,(25,25)))
#Primera generacion de flores
flores=generarPoblacionInicialDeFlores(50,49)
hacer=True
#loop de la simulacion
while True:
    if(hacer):
        for i in range(30):
            screen.fill(BLANCO)#Matriz de objetos en el tablero
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

            matriz[25][25]=panal
            screen.blit(panal.imagen,(14*25,14*25))

            for i in flores:
                matriz[i.posicion[0]][i.posicion[1]]=i
                pygame.draw.rect(screen,i.colorDeFlor,[i.posicion[0]*14,i.posicion[1]*14,14,14])
            
            panal,flores=inciarGeneraciones(panal,flores,matriz)
            #se actualiza
            pygame.display.flip()
            time.sleep(3)
    hacer=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
    pygame.display.flip()

pygame.quit() #Se cierra pygame del todo, para rapido rendimiento