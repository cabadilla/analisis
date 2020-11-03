from random import *
import threading
import sys, pygame
from pygame.locals import *
from PIL import Image, ImageChops, ImageEnhance, ImageOps

pygame.init()

#definiendo colores
NEGRO=[0,0,0]
BLANCO=[255,255,255]

#se define la imagen
global img
img = Image.open('imagenCono.png')
img=img.convert("RGB")

global Pixeles
Pixeles=img.load()



'''for i in range(500):
    for j in range(500):
    	if(pixeles[i,j]!=(255)):
        	pixeles[i,j]=(200)



for i in range(500):
    for j in range(500):
    	if(pixeles[i,j]==(255)):
        	pixeles[i,j]=(0)

img.save("nueva_imagen.png")'''


#tamano ventana
size = (500,500)
global screen


screen=pygame.display.set_mode(size)
screen.fill(BLANCO)

sonar=[]
'''
0=(255,255,255)
2=(254,252,0)
1=(0,0,0)

'''

def Norte(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return Norte((Coords[0]-1, Coords[1]), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Sur(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return Sur((Coords[0]+1, Coords[1]), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Este(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return Este((Coords[0], Coords[1]+1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Oeste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return Oeste((Coords[0], Coords[1]-1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def NorEste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return NorEste((Coords[0]-1, Coords[1]+1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def SurEste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return SurEste((Coords[0]+1, Coords[1]+1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def SurOeste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return SurOeste((Coords[0]+1, Coords[1]-1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def calcularColor(tiempo):
    pass
    

def NorOeste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return NorOeste((Coords[0]-1, Coords[1]-1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def DNorte(fila, columna):
	tiempo=Norte((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila-tiempo,columna]=calcularColor(tiempo)


def DSur(fila, columna):
	tiempo=Sur((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila+tiempo,columna]=calcularColor(tiempo)

def DEste(fila, columna):
	tiempo=Este((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila,columna+tiempo]=calcularColor(tiempo)

def DOeste(fila, columna):
	tiempo=Oeste((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila-tiempo,columna-tiempo]=calcularColor(tiempo)

def DNorEste(fila, columna):
	tiempo=NorEste((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila-tiempo,columna+tiempo]=calcularColor(tiempo)

def DSurEste(fila, columna):
	tiempo=SurEste((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila+tiempo,columna+tiempo]=calcularColor(tiempo)

def DNorOeste(fila, columna):
	tiempo=NorOeste((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila-tiempo,columna-tiempo]=calcularColor(tiempo)

def DSurOeste(fila, columna):
	tiempo=SurOeste((fila, columna), Pixeles, 0)
	if tiempo!=False:
		Pixeles[fila+tiempo,columna-tiempo]=calcularColor(tiempo)

def Fabric(num,fil,col):
	switch={
		1:DNorte(fil,col),
		2:DSur(fil,col),
		3:DEste(fil,col),
		4:DOeste(fil,col),
		5:DNorEste(fil,col),
		6:DSurEste(fil,col),
		7:DSurOeste(fil,col),
		8:DNorOeste(fil,col)
	}
	img.save("nueva_imagen.png")
	return switch[num]



def creaCono(Coords, n, sonar):
	im = Image.open('imagen.png')
	im=img.convert("RGB")
	pix=im.load()

	sonar.append((Coords[0], Coords[1]))
	var=1
	fila=Coords[0]-1
	columna=Coords[1]+1
	for i in range(n):
		var+=2
		MemoriaFila=fila
		MemoriaColumna=columna
		for j in range(var):
			pix[fila,columna]=(254,252,0)
			sonar.append((fila, columna))
			fila+=1
		fila=MemoriaFila-1
		columna=MemoriaColumna+1

	im.save("imagenCono.png")

def crearRayos(sonar, listaRayos):
	cant=randint(1, len(sonar))
	for i in range(cant):
		punto=randint(0, len(sonar)-1)
		if sonar[punto] not in listaRayos:
			listaRayos.append(sonar[punto])
		else:
			i-=1

def lanzarRayos(listaRayos):
	for rayo in listaRayos:
		n=randint(1,3)
		listapeque=[]
		for i in range(n):
			dire=randint(1,3)
			if dire not in listapeque:
				listapeque.append(dire)
			else:
				i-=1
		for i in listapeque:
			if i==1:
				hilo=threading.Thread(target=DNorEste(rayo[0], rayo[1]))
				hilo.start()
			elif i==2:
				hilo=threading.Thread(target=DEste(rayo[0], rayo[1]))
				hilo.start()
			else:
				hilo=threading.Thread(target=DSurEste(rayo[0], rayo[1]))
				hilo.start()


listaRayos=[]
creaCono((50,250), 25, sonar)
crearRayos(sonar, listaRayos)
lanzarRayos(listaRayos)



while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

	imagen = pygame.image.load("nueva_imagen.png")
	screen.blit(imagen,(0,0))
	pygame.display.flip()