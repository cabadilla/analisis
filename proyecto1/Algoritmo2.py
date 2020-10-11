from Algoritmo1 import *


def buscaSoluciones2(Nodos, FichasMano, N, Matriz, ListaSoluciones): #Metodo encargado de buscar las soluciones del segundo algoritmo
	'''
	Objetivo: Encontrar la mejor solucion para el segundo algoritmo
	Recibe: Nodos actuales en el grafo, Fichas que tiene en la mano el jugador 3, N para iterar, Copia de la matriz del grafo, Lista vacia para formar solucion
	Retorna: Una lista con la mejor solucion a futuro	
	'''
	Soluciones=buscaSoluciones(Nodos, FichasMano, [], [], 0, Matriz, []) #Utiliza el mismo algoritmo1 pero solamente para sacar todas las soluciones que se encontraron
	ListaSoluciones=sort(Soluciones[1]) #Se ordenan las soluciones de mayor a menor por puntos
	return Algoritmo2(Nodos, FichasMano, 0, Matriz, ListaSoluciones)



def Algoritmo2(Nodos, FichasMano, N, Matriz, ListaSoluciones):
	'''
	Objetivo: Por medio de backtracking, dadas las soluciones que se encontraron con la mano propia, busca entre sus propias fichas, combinaciones a futuro, escoge la mejor y retorna esta misma
	Recibe: Nodos actuales en el grafo, Fichas que tiene en la mmano, N para iterar, La copia de la matriz actual, Lista con las soluciones
	Retorna: La solucion con mejor jugada a futuro
	'''
	if N>len(ListaSoluciones)-1:
		return ListaSoluciones[0] #Si llego al final quiere decir que no hay fichas para una futura jugada por lo que retorna la de mejor puntuacion
	FichasManoPodada=sacarFichas(FichasMano, ListaSoluciones[N]) #Saca las fichas actuales de la Solucion para probar con las que quedan
	if buscaSoluciones(Nodos, FichasManoPodada, [], [], 0, Matriz, [])[0]==[]: #Se buscan soluciones con la mano podada en busca de jugadas a futuro
		Algoritmo2(Nodos, FichasMano, N+1, Matriz, ListaSoluciones) #Si no se encuentran para esta solucion, sigue con otra solucion
	else:
		return ListaSoluciones[N] #Si encuentra que hay jugada a futuro, retorna esta misma jugada

def sacarFichas(FichasMano, ListaSoluciones):
	'''
	Objetivo: Poda la mano actual de forma que solo queden las fichas que no estan en la solucion actual
	Recibe: La mano completa, La solucion actual de fichas
	Retorna: La mano podada
	'''
	Mano=[]
	find=False
	for i in range(0, len(FichasMano)):
		for j in ListaSoluciones:
			if not isinstance(j, int):
				if FichasMano[i]==j[0]:
					find=True
		if not find:
			Mano.append(FichasMano[i])
		find=False
	return Mano

def sort(lista):
	'''
	Objetivo: Ordena las soluciones por el puntaje obtenido
	Recibe: La lista de soluciones
	Retorna: La misma lista pero ordenada
	'''
	izquierda = []
	centro = []
	derecha = []

	if len(lista) > 1:
		pivote = lista[0][-1]
		for i in lista:
			if i[-1] > pivote:
				izquierda.append(i)
			elif i[-1] == pivote:
				centro.append(i)
			elif i[-1] < pivote:
				derecha.append(i)
		return sort(izquierda)+centro+sort(derecha)
	else:
		return lista
	
