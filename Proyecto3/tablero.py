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
    '''
    Objetivo: Calcula el limite inferior de la vision de las abejas
    Recibe: Una direccion, unas coordenadas
    Retorna: El proceso que tenga que realizar dependiendo de la direccion
    '''
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
    '''
    Objetivo: Calcula el limite superior de la vision de las abejas
    Recibe: Una direccion, unas coordenadas
    Retorna: El proceso que tenga que realizar dependiendo de la direccion
    '''
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
    '''
    Objetivo: Calcula todos los puntos matriz que se encuentran dentro de la vision de las abejas
    Recibe: Una direccion, unas coordenadas
    Retorna: El proceso que debe realizar para poder calcular el relleno
    '''
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
    '''
    Objetivo: Encuentra todo el triangulo de vision de las abejas, depende de la direccion fav
    Recibe: Una abeja
    Retorna: La lista de todos los puntos de la matriz en vision de esa abeja
    '''
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
    '''
    Objetivo: Simula el recorrido de la abeja para encontrar flores
    Recibe: Una abeja y la matriz del Tablero que es el campo de flores
    Retorna: La abeja con su recorrido modificado
    '''
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

def recorridoGeneracion(generacionAbejas,matriz,gen):
    '''
    Objetivo: Realiza el recorrido de todas las abejas utilizando su funcion auxiliar
    Recibe: La generaccion actual de abejas y la matriz del campo
    Retorna: La nueva generacion de abejas
    '''
    finalGeneracion=[]
    for i in generacionAbejas:
        finalGeneracion.append(recorridoUnaAbeja(i,matriz))
    ControladorDeTXT.escribirTXT(finalGeneracion, gen)
    nuevaGeneracion=(cruceAbejas(finalGeneracion))
    return nuevaGeneracion

def inciarGeneraciones(panal,flores,matrizT,gen):
    '''
    Objetivo: Realiza la primera generacion de abejas y flores
    Recibe: El panall de abejas, las flores y el campo del trabajo
    Retorna: El panall y todas las flores nuevas
    '''
    nueva=recorridoGeneracion(panal.enjambre,matrizT,gen)
    panal.enjambre=nueva
    floresNuevas=cruceFlores(flores)
    return panal,floresNuevas


#Se crea el panal con la primera generacion inicial de abejas
panal=panal((25,25),generarPoblacionInicialDeAbejas(10,(25,25)))
#Primera generacion de flores
flores=generarPoblacionInicialDeFlores(50,49)
hacer=True
#Controlador de los archivos de texto
ControladorDeTXT=controladorTXT()

#loop de la simulacion
while True:
    if(hacer):
        for gen in range(30):
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

            for flor in flores:
                matriz[flor.posicion[0]][flor.posicion[1]]=flor
                pygame.draw.rect(screen,flor.colorDeFlor,[flor.posicion[0]*14,flor.posicion[1]*14,14,14])
            
            panal,flores=inciarGeneraciones(panal,flores,matriz,gen)
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