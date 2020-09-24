from Grafo import Grafo

matriz=[]

def llenaMatriz(filas, columnas):
	for i in range(filas):
		matriz.append([])
		for j in range(columnas):
			matriz[i].append(None)

def printMatriz():
	for i in range(len(matriz)):
		print(matriz[i])


llenaMatriz(10, 11)
root=Grafo()
matriz=root.insertar(5, 5, matriz) #nodo central
matriz=root.insertar(5, 6, matriz) #nodo derecho
matriz=root.insertar(5, 4, matriz) #nodo izquierdo
matriz=root.insertar(4, 5, matriz) #nodo arriba
matriz=root.insertar(6, 5, matriz) #nodo abajo
matriz=root.getMatriz()
printMatriz()
print(root.getNodos())
print(matriz[5][4].getArriba())
print(matriz[5][4].getAbajo())
print(matriz[5][4].getIzquierda())
print(matriz[5][4].getDerecha())
