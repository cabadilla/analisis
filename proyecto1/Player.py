from Algoritmo1 import *
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
			return self.algoritmo2()

	def algoritmo1(self, Nodos, Matriz):
		Soluciones=buscaSoluciones(Nodos, self.getFichasDisponibles(), [], [], 0, Matriz)
		print(Soluciones)
		return
	
	def algoritmo2(self):
		print("fddg")

	def getFichasDisponibles(self):
		return self.fichasDisponibles

	def getAlgoritmo(self):
		return self.algoritmo