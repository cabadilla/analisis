from Node import *
from Casillas import Casillas

class Grafo():
	def __init__(self):
		self.nodos=[]                                                          #nodos dentro del grafo
		self.matriz=[]														   #matriz que va a tener el grafo
	
	def insertar(self, fila, columna, ficha):						           #funcion que se encarga de ingresar dentro del grafo
		if self.casilla_Vacia(fila, columna):
			Nodo=Node(fila, columna, ficha)									   #se crea el nodo a ingresar
			try:
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
			except (IndexError):
				pass
			self.nodos.append(Nodo)
			self.matriz[fila][columna]=Nodo #coloca el nodo en la posicion donde debe ir


	def setMatriz(self, matriz):                                              #setea una nueva matriz
		self.matriz=matriz

	def getNodos(self):                                                       #retorna la lista de nodos
		return self.nodos

	def getMatriz(self):                                                      #retorna la matriz que tiene al grafo
		return self.matriz

	def casilla_Vacia(self, fila, columna):                                   #funcion que verifica que la celda donde se va a insertar un nuevo nodo sea vacia
		return self.matriz[fila][columna]==None

	def mueveNodos(self, fichasPuestas, filas, columnas):                     #funcion que se dedica a hacer el corrimiento de la matriz dentro del grafo
		newMatriz=[] #se crea una nueva matriz vacia
		for fila in range(0,filas):
			newMatriz.append([]) #se agregan la misma cantidad de filas que hay en el tablero
			for columna in range(0,columnas):
				newMatriz[fila].append(None) #se agregan la misma cantidad de columnas que hay en el tablero
		for i in range(0, len(fichasPuestas)):
			self.nodos[i].setFila(fichasPuestas[i].cordenadasMatriz[0]) #cambio la fila de los nodos, comparadas a las del tablero			
			self.nodos[i].setColumna(fichasPuestas[i].cordenadasMatriz[1]) #cambio la columna de los nodos, comparadas a las del tablero
			

		for nodo in self.nodos:
			newMatriz[nodo.fila][nodo.columna]=nodo #vuelve a colocar los nodos dentro de la nueva matriz

		self.setMatriz(newMatriz) #vuelve a setear la nueva matriz