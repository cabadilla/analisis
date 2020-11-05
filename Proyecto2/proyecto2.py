from random import *
import threading
import sys, pygame
from pygame.locals import *
from PIL import Image, ImageChops, ImageEnhance, ImageOps
from statistics import mode


pygame.init()

#definiendo colores
NEGRO=[0,0,0]
BLANCO=[255,255,255]

#se define la imagen


'''for i in range(500):
	for j in range(500):
		if(pixeles[i,j]!=(255)):
			pixeles[i,j]=(200)'''



'''for i in range(500):
	for j in range(500):
		Pixeles[i,j]=(255,255,255)

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

def Norte(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Pixeles[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return Norte((Coords[0]-1, Coords[1]), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def veinteGradosArriba(Coords,Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			#pixels[Coords[1],Coords[0]]=(0,46,255)
			if Pixeles[Coords[0],Coords[1]]==(0,0,0): 
				return Tiempo
			else:
				return veinteGradosArriba((Coords[0]+2,Coords[1]-1), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def veinteGradosAbajo(Coords,Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			#pixels[Coords[0],Coords[1]]=(0,46,255)
			if Pixeles[Coords[0],Coords[1]]==(0,0,0): 
				return Tiempo
			else:
				return veinteGradosAbajo((Coords[0]+2,Coords[1]+1), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Sur(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Pixeles[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return Sur((Coords[0]+1, Coords[1]), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Este(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			#pixels[Coords[0],Coords[1]]=(0,46,255)
			if Pixeles[Coords[0],Coords[1]]==(0,0,0): 
				return Tiempo
			else:
				return Este((Coords[0]+1,Coords[1]), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Oeste(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Pixeles[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return Oeste((Coords[0], Coords[1]-1), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def NorEste(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			#pixels[Coords[0],Coords[1]]=(32,54,6)
			if Pixeles[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return NorEste((Coords[0]+1, Coords[1]-1), Tiempo+1)
		else:
			return False
	except (IndexError):
		print("error")
		return False

def SurEste(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			#pixels[Coords[0],Coords[1]]=(32,54,6)
			if Pixeles[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return SurEste((Coords[0]+1, Coords[1]+1), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def SurOeste(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Pixeles[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return SurOeste((Coords[0]+1, Coords[1]-1), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def calcularColor(tiempo):
	return (0,255,0)
	

def NorOeste(Coords, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Pixeles[Coords[0],Coords[1]]==(0,0,0):
				return Tiempo
			else:
				return NorOeste((Coords[0]-1, Coords[1]-1), Tiempo+1)
		else:
			return False
	except (IndexError):
		return False


def DNorte(fila, columna):
	tiempo=Norte((fila, columna), 0)
	if tiempo!=False:
		pixels[fila-tiempo,columna]=calcularColor(tiempo)


def DveinteAbajo(fila,columna):
	tiempo=veinteGradosAbajo((fila,columna), 0)
	if tiempo!=False:
		pass
		pixels[columna+(tiempo-1),fila+2*tiempo-2]=calcularColor(tiempo)

def DveinteArriba(fila,columna):
	tiempo=veinteGradosArriba((fila,columna), 0)
	if tiempo!=False:
		pass
		pixels[columna-(tiempo-1),fila+2*tiempo-2]=calcularColor(tiempo)

def DSur(fila, columna):
	tiempo=Sur((fila, columna), 0)
	if tiempo!=False:
		pixels[fila+tiempo,columna]=calcularColor(tiempo)

def DEste(fila,columna):
	tiempo=Este((fila,columna), 0)
	#print(fila,columna)
	if tiempo!=False:
		pixels[columna,fila+tiempo]=calcularColor(tiempo)

def DOeste(fila, columna):
	tiempo=Oeste((fila, columna), 0)
	if tiempo!=False:
		pixels[fila-tiempo,columna-tiempo]=calcularColor(tiempo)

def DNorEste(fila, columna):
	tiempo=NorEste((fila, columna), 0)
	if tiempo!=False:
		pass
		pixels[columna+tiempo,fila-tiempo]=calcularColor(tiempo)
		#print("dibuje en"+str(fila)+"-"+str(columna))

def DSurEste(fila, columna):
	tiempo=SurEste((fila, columna), 0)
	if tiempo!=False:
		pixels[columna+tiempo,fila+tiempo]=calcularColor(tiempo)
		pass

def DNorOeste(fila, columna):
	tiempo=NorOeste((fila, columna), 0)
	if tiempo!=False:
		pixels[fila-tiempo,columna-tiempo]=calcularColor(tiempo)

def DSurOeste(fila, columna):
	tiempo=SurOeste((fila, columna), 0)
	if tiempo!=False:
		pixels[fila+tiempo,columna-tiempo]=calcularColor(tiempo)
		#print("dibuje en"+str(fila)+"-"+str(columna))

def Fabric(num,fil,col):
	switch={
		1:DNorte(fil,col),
		2:DSur(fil,col),
		3:DEste(fil,col),
		4:DveinteAbajo(fil,col),
		5:DveinteArriba(fil,col),
		6:DSurEste(fil,col),
		7:DSurOeste(fil,col),
		8:DNorOeste(fil,col)
	}
	return switch[num]



def creaCono(Coords, n, sonar):
	son=[]
	im = Image.open('imagen.png')
	im=im.convert("RGB")
	pix=im.load()
	son.append((Coords[0], Coords[1]))
	var=1
	fila=Coords[1]-1
	columna=Coords[0]+1
	for j in range(n):
		var+=2
		MemoriaFila=fila
		MemoriaColumna=columna
		for i in range(var):
			son.append((columna, fila))
			fila+=1
		fila=MemoriaFila-1
		columna=MemoriaColumna+1

	for i in son:
		pix[i[0],i[1]]=(254,252,0)
		if i[0]==n+Coords[0]:
			sonar.append(i)

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
		n=randint(1,5)
		listapeque=[]
		for i in range(n):
			dire=randint(1,5)
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
			elif i==3:
				hilo=threading.Thread(target=DSurEste(rayo[0], rayo[1]))
				hilo.start()
			elif i==4:
				hilo=threading.Thread(target=DveinteArriba(rayo[0], rayo[1]))
				hilo.start()
			else:
				hilo=threading.Thread(target=DveinteAbajo(rayo[0], rayo[1]))
				hilo.start()



listaRayos=[]
creaCono((50,250), 25, sonar)

global ima
global img

# img contiene la imagen del cono y ima contiene la imagen que se va creando
img = Image.open('imagenCono.png')
img=img.convert("RGB")

ima = Image.open('nueva_imagen.png')
ima=ima.convert("RGB")

global pixels
global Pixeles

#pixels tiene los pixeles  de ima y Pixeles  los de img
Pixeles=img.load()
pixels=ima.load()



crearRayos(sonar, listaRayos)
lanzarRayos(listaRayos)

clock = pygame.time.Clock()

def borrar():
	for i in range(500):
		for j in range(500):
			pixels[i,j]=(255,255,255)

	ima.save("nueva_imagen.png")

borrar()
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

	crearRayos(sonar, listaRayos)
	lanzarRayos(listaRayos)

	ima.save("nueva_imagen.png")

	imagen = pygame.image.load("nueva_imagen.png")
	screen.blit(imagen,(0,0))
	pygame.display.flip()
	
	clock.tick(30)