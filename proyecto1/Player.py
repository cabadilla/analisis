
#Creacion de la clase principal para los personajes o jugadores

class Player:
	def __init__(self, name, col,r): #constructor de la clase player, tiene nombre, puntuacion iniciada en 0 y un color
		self.nombre=name
		self.puntuacion=0
		self.fichasDisponibles=[]
		self.color=col
		self.rectFichas=r
		self.algoritmo=1

	def aumentaPuntuacion(self, points): #metodo aumentaPuntuacion, ya que el juego se basa por puntos cada player tiene que tener su propia puntuacion
		self.puntuacion+=points

	
	def jugarSolo(self):
		print("dd")

	def algoritmo1(self):
		print("fd")
	
	def algoritmo2(self):
		print("fddg")