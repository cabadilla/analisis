from Algoritmo1 import *
from Algoritmo2 import *
from time import time
#Creacion de la clase principal para los personajes o jugadores

class Player:
	def __init__(self, name, col,r, algoritmo): #constructor de la clase player, tiene nombre, puntuacion iniciada en 0 y un color
		self.nombre=name
		self.puntuacion=0
		self.fichasDisponibles=[]
		self.color=col
		self.rectFichas=r
		self.algoritmo=algoritmo

	def aumentaPuntuacion(self, points): #metodo aumentaPuntuacion, ya que el juego se basa por puntos cada player tiene que tener su propia puntuacion
		self.puntuacion+=points
	
	def jugarSolo(self, Nodos, Matriz):
		if self.getAlgoritmo()==1:
			return self.algoritmo1(Nodos, Matriz)
		else:
			return self.algoritmo2(Nodos, Matriz)

	def algoritmo1(self, Nodos, Matriz):
		CopiaMatriz=Matriz[:]
		#tiempo_inicial=time()
		Soluciones=buscaSoluciones(Nodos, self.getFichasDisponibles(), [], [], 0, CopiaMatriz, [])
		#tiempoFinal=time()
		#tiempoEjecucion = time() - tiempo_inicial
		#print("Algoritmo 1 tiempo: "+str(tiempoEjecucion))
		return Soluciones[0]
	
	def algoritmo2(self, Nodos, Matriz):
		CopiaMatriz=Matriz[:]
		#tiempo_inicial=time()
		Soluciones=buscaSoluciones2(Nodos, self.getFichasDisponibles(), 0, CopiaMatriz, [])
		#tiempoEjecucion = time() - tiempo_inicial
		#print("Algoritmo 2 tiempo: "+str(tiempoEjecucion))
		return Soluciones
		

	def getFichasDisponibles(self):
		return self.fichasDisponibles

	def getAlgoritmo(self):
		return self.algoritmo