class Node():
	def __init__(self, fila, columna):
		self.izquierda=None                  #rama que va a apuntar siempre a los nodos ubicados a la izquierda
		self.derecha=None                    #rama que va a apuntar siempre a los nodos ubicados a la derecha
		self.arriba=None                     #rama que va a apuntar siempre a los nodos ubicados abajo
		self.abajo=None                      #rama que va a apuntar siempre a los nodos ubicados arriba
		self.color=None                      #atributo color que simboliza el color de la ficha puesta
		self.forma=None                      #atributo forma que simboliza la forma de la ficha puesta
		self.fila=fila                       #atributo fila que simboliza la fila de la casilla donde fue puesta
		self.columna=columna                 #atributo columna que simboliza la columna de la casilla donde fue puesta

	def setIzquierda(self, Nodo):
		self.izquierda=Nodo                  #setea el puntero de la izquierda para que apunte al nodo que se encuentra a la izquierda

	def setDerecha(self, Nodo):
		self.derecha=Nodo                    #setea el puntero de la derecha para que apunte al nodo que se encuentra a la derecha

	def setArriba(self, Nodo):
		self.arriba=Nodo                     #setea el puntero de arriba para que apunte al nodo que se encuentra arriba

	def setAbajo(self, Nodo):
		self.abajo=Nodo                      #setea el puntero de abajo para que apunte al nodo que se encuentra a la izquierda

	def getIzquierda(self):
		return self.izquierda                #retorna el objeto que tenga a la izquierda, None si no existe

	def getDerecha(self):
		return self.derecha                  #retorna el objeto que tenga a la derecha, None si no existe

	def getArriba(self):
		return self.arriba                   #retorna el objeto que tenga arriba, None si no existe

	def getAbajo(self):
		return self.abajo                    #retorna el objeto que tenga abajo, None si no existe