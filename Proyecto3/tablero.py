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

def triangulo(abeja):
    listaPuntosLimiteSuperior=[]
    listaPuntosLimitesInferior=[]
    listaTriangulo=[]
    actual=(25,25)
    print(abeja.direccionFavorita[0])
    for i in range(25):
        actual=calcularPuntos(abeja.direccionFavorita[0],actual[0],actual[1])
        listaPuntosLimiteSuperior.append(actual)
        
    actual=(25,25)
    for i in range(25):
        actual=calcularPuntosDif(abeja.direccionFavorita[0],actual[0],actual[1])
        listaPuntosLimitesInferior.append(actual)

    for i in range (25):
        actual=listaPuntosLimiteSuperior[i]
        while actual !=listaPuntosLimitesInferior[i]:
            actual=(calcularPuntosRelleno(abeja.direccionFavorita[0],actual[0],actual[1]))
            listaTriangulo.append(actual)
    return listaTriangulo
#se inicia el recorrido
def recorridoUnaAbeja(abeja,matrizTablero):
    pass
triangulo(panal.enjambre[0])

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