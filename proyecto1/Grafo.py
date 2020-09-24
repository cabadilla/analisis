from Node import *

class Grafo():
	def __init__(self):
		self.nodos=[]                                                          #nodos dentro del grafo
		self.matriz=[]														   #matriz que va a tener el grafo
	
	def insertar(self, fila, columna, matriz):										   #funcion que se encarga de ingresar dentro del grafo
		self.setMatriz(matriz)
		if self.casilla_Vacia(fila, columna):
			Nodo=Node(fila, columna)										   #se crea el nodo a ingresar
			if not self.casilla_Vacia(fila, columna+1):                        #revisa si dentro de la matriz (donde se va a insertar un nodo), hay otro nodo a la derecha
				self.matriz[fila][columna+1].setIzquierda(Nodo)                #coloca el puntero izquierdo del Nodo para que apunte al nuevo nodo
				Nodo.setDerecha(self.matriz[fila][columna+1])                  #coloca el puntero del nuevo nodo al nodo del lado derecho
			if not self.casilla_Vacia(fila, columna-1):
				self.matriz[fila][columna-1].setDerecha(Nodo)                  #coloca el puntero derecho del Nodo para que apunte al nuevo nodo
				Nodo.setIzquierda(self.matriz[fila][columna-1])                #coloca el puntero del nuevo nodo al nodo del lado izquierdo
			if not self.casilla_Vacia(fila-1, columna):
				self.matriz[fila-1][columna].setAbajo(Nodo)                    #coloca el puntero de abajo del Nodo para que apunte al nuevo nodo
				Nodo.setArriba(self.matriz[fila-11][columna])                  #coloca el puntero del nuevo nodo al nodo del lado arriba
			if not self.casilla_Vacia(fila+1, columna):
				self.matriz[fila+1][columna].setArriba(Nodo)                   #coloca el puntero de arriba del Nodo para que apunte al nuevo nodo
				Nodo.setAbajo(self.matriz[fila+1][columna])                    #coloca el puntero del nuevo nodo al nodo del lado abajo
			self.nodos.append(Nodo)
			self.matriz[fila][columna]=Nodo
			return self.matriz
		else:
			return "Ya existe una pieza en esa casilla"

	def casilla_Vacia(self, fila, columna):                                   #funcion que verifica que la celda donde se va a insertar un nuevo nodo sea vacia
		return self.matriz[fila][columna]==None

	def setMatriz(self, matriz):                                              #setea una nueva matriz
		self.matriz=matriz

	def getNodos(self):                                                       #retorna la lista de nodos
		return self.nodos

	def getMatriz(self):                                                      #retorna la matriz que tiene al grafo
		return self.matriz

