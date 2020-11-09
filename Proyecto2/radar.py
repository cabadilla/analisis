import pygame
from pygame.locals import *
import math
import random
import threading
import sys
from PIL import Image, ImageChops, ImageEnhance, ImageOps

def Desplazarse(X, Y, Angulo, listaTiempos, Tiempo, Rebotes):
	'''
	Objetivo: Recrea el desplazamiento del rayo dependiendo del angulo que recibe
	Recibe: X posicion inicial, Y posicion inicial, Angulo hacia donde se dirige, Tiempo que dura en chocar contra un objeto y devolverse
	'''
	try:
		if X>=0 and Y>=0:
			if Rebotes==0:
				return listaTiempos
			elif pixelesCono[X, Y]!=(255,255,255) and pixelesCono[X, Y]!=(254,252,0):
				listaTiempos.append(Tiempo)
				listaTiempos=CrearRebotes(X, Y, Angulo, listaTiempos, Tiempo, Rebotes-1)
			else:
				'''if Rebotes<3:
					pixelesResultado[X,Y]=255
				else:
					pixelesResultado[X,Y]=155'''
				X+=1*math.sin(Angulo)
				Y+=1*math.cos(Angulo)
				return Desplazarse(X, Y, Angulo, listaTiempos, Tiempo+1, Rebotes)
		else:
			return []
	except (IndexError):
		return listaTiempos
	finally:
		return listaTiempos

def CrearRebotes(X, Y, Angulo, listaTiempos, Tiempo, Rebotes):
	Angulo=random.uniform(0, 2*PI)
	X+=1*math.sin(Angulo)
	Y+=1*math.cos(Angulo)
	listaTiempos=Desplazarse(X,Y,Angulo,listaTiempos,Tiempo+1,Rebotes)
	return listaTiempos

def FabricAngulos(X, Y):
	Angulo=random.uniform(2.3, PI/4)
	Hilo=threading.Thread(target=LanzarRayo(X, Y, Angulo))
	Hilo.start()

def FabricAngulosSec(X, Y,Ang):
	Angulo=random.uniform(Ang+0.4, Ang-0.4)
	Hilo=threading.Thread(target=LanzarRayoSec(X, Y, Ang,Angulo))
	Hilo.start()


def LanzarRayoSec(X, Y, AnguloPrin,Angulo):
	listaTiempos=Desplazarse(X, Y, Angulo, [], 0,3)
	contador=0
	try:
		if listaTiempos!=[]:
			for Tiempos in listaTiempos:
				XFinal=Tiempos*math.sin(AnguloPrin)+X
				YFinal=Tiempos*math.cos(AnguloPrin)+Y
				pixelesResultado[XFinal, YFinal]=CalcularColor(Tiempos-contador*Tiempos*1/4)
				contador+=1
	except (IndexError):
		pass

def LanzarRayo(X, Y, Angulo):
	listaTiempos=Desplazarse(X, Y, Angulo, [], 0,3)
	contador=0
	for i in range(5):
		FabricAngulosSec(X,Y,Angulo)
	try:
		if listaTiempos!=[]:
			for Tiempos in listaTiempos:
				XFinal=Tiempos*math.sin(Angulo)+X
				YFinal=Tiempos*math.cos(Angulo)+Y
				pixelesResultado[XFinal, YFinal]=CalcularColor(Tiempos-contador*1/7)
				contador+=1
	except (IndexError):
		pass

def CalcularColor(Tiempo):
	intensidad=Tiempo*1/8
	return int(abs(155-intensidad))

def Borrar():
	'''
	Objetivo: Borra la imagen anterior para que inicie limpia
	Recibe: No recibe
	Retorna: La imagen limpia
	'''
	for i in range(500):
		for j in range(500):
			pixelesResultado[i,j]=(0)
	imagenResultado.save("nueva_imagen.png")

def creaCono(Coords, n, sonar):
	imagenLocal=Image.open('imagen.png')
	imagenLocal=imagenLocal.convert("RGB")
	pixelesLocal=imagenLocal.load()

	sonar.append((Coords[0], Coords[1]))
	var=1
	fila=Coords[1]-1
	columna=Coords[0]+1
	for j in range(n):
		var+=2
		MemoriaFila=fila
		MemoriaColumna=columna
		for i in range(var):
			sonar.append((columna, fila))
			fila+=1
		fila=MemoriaFila-1
		columna=MemoriaColumna+1

	for i in sonar:
		pixelesLocal[i[0],i[1]]=(254,252,0)

	imagenLocal.save("imagenCono.png")


#Inicio de la pantalla de pygame
pygame.init()

#Escala de colores que se va a utilizar en el programa
ColorNegro=(0, 0, 0)
ColorBlanco=(255, 255, 255)
ColorGris=(155,155,155)

VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

#Numero PI para el calculo de angulos
PI=3.141592653

#Dimensiones de la pantalla grande
Dimensiones=[1000, 500]

#Creacion de la pantalla con las dimensiones antes especificadas
Screen=pygame.display.set_mode(Dimensiones)

#Reloj utilizado para bajarle la velocidad al programa
Clock=pygame.time.Clock()

#El programa corre hasta que se cierre la pantalla
Close=False

#Angulo inicial del cono 
Angulo=0

# imagenCono contiene la imagen del cono y imagenResultado contiene la imagen que se va creando
imagenCono=Image.open('imagenCono.png')
imagenCono=imagenCono.convert("RGB")
imagenResultado=Image.open('nueva_imagen.png')
imagenResultado=imagenResultado.convert("L")

#Matrices de pixeles de ambas imagenes
pixelesCono=imagenCono.load()
pixelesResultado=imagenResultado.load()

Screen.fill(ColorBlanco)
creaCono((50, 250), 40, [])
Borrar()
FabricAngulos(50,250)
while not Close:
	for evento in pygame.event.get():  # El usuario hizo algo
		if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
			Close=True                 # Marca que ya lo hemos hecho, de forma que abandonamos el bucle


	FabricAngulos(50,250)
	
	imagenResultado.save("nueva_imagen.png")
	imagenNueva = pygame.image.load("nueva_imagen.png")
	Screen.blit(imagenNueva,(0,0))

	imagenCono = pygame.image.load("imagenCono.png")
	Screen.blit(imagenCono,(501,0))

	# Avancemos y actualicemos la pantalla con lo que hemos dibujado.
	pygame.display.flip()

	# Limitamos a 60 fotogramas por segundo
	Clock.tick(60)

pygame.quit()