import pygame
from pygame.locals import *
import math
import random
import threading
import sys
from PIL import Image, ImageChops, ImageEnhance, ImageOps

#Numero PI para el calculo de angulos
PI=3.141592653

#Limite superior e inferior del cono para lanzar los rayos
lim1=1.8
lim2=PI/4

def Desplazarse(X, Y, Angulo, listaTiempos, Tiempo, Rebotes):
	'''
	Objetivo: Recrea el desplazamiento del rayo dependiendo del angulo que recibe
	Recibe: X posicion inicial, Y posicion inicial, Angulo hacia donde se dirige, Tiempo que dura en chocar contra un objeto y devolverse, Posibles rebotes a realizar
	Restricciones: El X y el Y deben ser positivos
	'''
	try:
		if X>=0 and Y>=0:
			if Rebotes==0: #si los rebotes llegan a 0 el rayo muere y se retorna la lista de Tiempos
				return listaTiempos
			elif pixelesCono[X, Y]!=(255,255,255) and pixelesCono[X, Y]!=(0, 0, 255): #si encuentra algo diferente a blanco o azul el rayo choca
				listaTiempos.append(Tiempo)
				listaTiempos=CrearRebotes(X, Y, Angulo, listaTiempos, Tiempo, Rebotes-1)
			else:	
				#if Rebotes==3:
					#pixelesResultado[X,Y]=255
				#else:
					#pixelesResultado[X,Y]=100
				X+=1*math.sin(Angulo) #se aumenta la X en direccion al angulo
				Y+=1*math.cos(Angulo) #se aumenta la Y en direccion al angulo
				return Desplazarse(X, Y, Angulo, listaTiempos, Tiempo+1, Rebotes) #Llamada recursiva de la funcion 
		else:
			return []
	except (IndexError):
		return listaTiempos #si el rayo se va de la imagen se retornan los tiempos que se tuvieron
	finally:
		return listaTiempos #si en tiempo de ejecucion sucede otro acontecimiento se retornan los tiempos

def CrearRebotes(X, Y, Angulo, listaTiempos, Tiempo, Rebotes):
	'''
	Objetivo: Dados los angulos con los que salio, se crean rebotes dependiendo de la estructura con la que choca el objeto
	Recibe: X posicion inicial, Y posicion inicial, Angulo hacia donde se dirige, Tiempo que dura antes de volver a chocar y los rebotes que le quedan a ese rayo
	Restricciones: No tiene
	'''
	Angulo=random.uniform(lim1-2.5, lim2-(7*PI/4))
	X+=1*math.sin(Angulo)
	Y+=1*math.cos(Angulo)
	listaTiempos=Desplazarse(X,Y,Angulo,listaTiempos,Tiempo+1,Rebotes)
	return listaTiempos

def FabricAngulos(X, Y):
	'''
	Objetivo: Dada la posicion inicial del punto y un cono especificado por los limites, se utiliza un .uniform para crear angulos aleatorios y se lanzar rayos
	Recibe: X posicion inicial, Y posicion inicial
	Restricciones: No hay
	'''
	global lim1, lim2

	Angulo=random.uniform(lim1, lim2)
	Hilo=threading.Thread(target=LanzarRayo(X, Y, Angulo))
	Hilo.start()

def FabricAngulosSec(X, Y,Ang):
	'''
	Objetivo: Crea los rayos secundarios que parten de un rayo principal
	Recibe: X posicion inicial, Y posicion inicial, Angulo del rayo principal
	Restricciones: No hay
	'''
	Angulo=random.uniform(Ang+0.4, Ang-0.4)
	Hilo=threading.Thread(target=LanzarRayoSec(X, Y, Ang,Angulo))
	Hilo.start()


def LanzarRayoSec(X, Y, AnguloPrin,Angulo):
	'''
	Objetivo: Funcion del hilo para lanzar y dibujar los pixeles en el momento que se retorne una lista con los tiempos de rebote
	Recibe: X posicion inicial, Y posicion inicial, Angulo del rayo principal, Angulo del rayo secundario
	Restricciones: No hay
	'''
	listaTiempos=Desplazarse(X, Y, Angulo, [], 0,3)
	contador=1
	try:
		if listaTiempos!=[]:
			for Tiempos in listaTiempos:
				XFinal=Tiempos*math.sin(AnguloPrin)+X
				YFinal=Tiempos*math.cos(AnguloPrin)+Y
				pixelesResultado[XFinal, YFinal]=CalcularColor((Tiempos/contador))
				contador+=1
	except (IndexError):
		pass

def LanzarRayo(X, Y, Angulo):
	'''
	Objetivo: Funcion del hilo para lanzar y dibujar los pixeles de los rayos principales en el momento que se retorne una lista con los tiempos de rebote
	Recibe: X posicion inicial, Y posicion inicial, Angulo del rayo principal
	Restricciones: No tiene
	'''
	listaTiempos=Desplazarse(X, Y, Angulo, [], 0,3)
	contador=1
	for i in range(5): #por cada rayo principal, se lanzan 5 rayos secundarios
		FabricAngulosSec(X,Y,Angulo)
	try:
		if listaTiempos!=[]:
			for Tiempos in listaTiempos:
				XFinal=Tiempos*math.sin(Angulo)+X
				YFinal=Tiempos*math.cos(Angulo)+Y
				pixelesResultado[XFinal, YFinal]=CalcularColor((Tiempos/contador)/5)
				contador+=1
	except (IndexError):
		pass

def CalcularColor(Tiempo):
	'''
	Objetivo: Calcula el color dependiendo del tiempo que dura en ejecucion el rayo
	Recibe: Tiempo en ejecucion
	Restricciones: No hay
	'''
	if (255-Tiempo*0.4)>0:
		return int(255-Tiempo*0.4)
	else:
		return 0

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



def rotarCono(x,y,dire):
	'''
	Objetivo: Rota el cono para poder lanzar rayos en todas las dirrecciones
	Recibe: X posicion inicial, Y posicion inicial, direccion en a que va (1 para arriba, 2 para abajo, 0 para no rotacion)
	Restricciones: No tiene
	'''
	global lim1, lim2
	
	lista=[]
	if dire==1:
		lim1=lim1+0.4
		lim2=lim2+0.4
	elif dire==2:
		lim1=lim1-0.4
		lim2=lim2-0.4
	else:
		lim1=lim1
		lim2=lim2
	
	xaux=x
	yaux=y

	imagenLocal=Image.open('imagen.png')
	imagenLocal=imagenLocal.convert("RGB")
	pixelesLocal=imagenLocal.load()
	pixelesLocal[x,y]=(0, 0, 255)

	for i in range(40):
		xaux+=1*math.sin(lim1)
		yaux+=1*math.cos(lim1)
		pixelesLocal[xaux,yaux]=(0, 0, 255)

	xaux=x
	yaux=y
	for i in range(40):
		xaux+=1*math.sin(lim2)
		yaux+=1*math.cos(lim2)
		pixelesLocal[xaux,yaux]=(0, 0, 255)



	imagenLocal.save("imagenCono.png")

#Inicio de la pantalla de pygame
pygame.init()

#Escala de colores que se va a utilizar en el programa
ColorNegro=(0, 0, 0)
ColorBlanco=(255, 255, 255)
ColorGris=(155,155,155)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

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

#ImagenCono contiene la imagen del cono y imagenResultado contiene la imagen que se va creando
imagenCono=Image.open('imagenCono.png')
imagenCono=imagenCono.convert("RGB")
imagenResultado=Image.open('nueva_imagen.png')
imagenResultado=imagenResultado.convert("L")

#Matrices de pixeles de ambas imagenes
pixelesCono=imagenCono.load()
pixelesResultado=imagenResultado.load()

#Posicion inicial del sonar
posicionX=50
posicionY=250

#Se llena la pantalla de color blaco
Screen.fill(ColorBlanco)

#Se borra todo lo que habia anteriormente en pantalla
Borrar()

#Se manda a dibujar el cono en la posicion inicial sin rotacion
rotarCono(50,250,0)

while not Close: #mientras no este cerrada la ventana
	for evento in pygame.event.get():  # El usuario hizo algo
		if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
			Close=True                 # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
		if evento.type == pygame.KEYUP:
			if evento.key == pygame.K_LEFT: #Si se pulso la tecla de izquierda el cono rota hacia arriba
				rotarCono(posicionX,posicionY,1) 
			if evento.key == pygame.K_RIGHT: #Si se pulso la tecla de derecha el cono rota hacia abajo
				rotarCono(posicionX,posicionY,2)
		if evento.type == pygame.MOUSEBUTTONDOWN: #Si se hizo click en alguna parte de la ventana, se re-posiciona el sonar
			x,y=evento.pos
			if(x>500):
				posicionX=x-500
				posicionY=y
				rotarCono(posicionX,posicionY,0) #Se dibuja el cono en la nueva posicion



	FabricAngulos(posicionX,posicionY) #Se crean infinita cantidad de rayos principales hasta que el programa finalice

	#Se actualizan las imagenes que se utilizan
	imagenResultado.save("nueva_imagen.png")
	imagenNueva = pygame.image.load("nueva_imagen.png")
	Screen.blit(imagenNueva,(0,0))

	imagenCono = pygame.image.load("imagenCono.png")
	Screen.blit(imagenCono,(501,0))

	# Avancemos y actualicemos la pantalla con lo que hemos dibujado.
	pygame.display.flip()

	# Limitamos a 60 fotogramas por segundo
	Clock.tick(60)

pygame.quit() #Se cierra pygame del todo, para rapido rendimiento