from Algoritmo1 import *


def buscaSoluciones2(Nodos, FichasMano, N, Matriz, ListaSoluciones):
	Soluciones=buscaSoluciones(Nodos, FichasMano, [], [], 0, Matriz, [])
	print(Soluciones)
	ListaSoluciones=sort(Soluciones[1])
	return Algoritmo2(Nodos, FichasMano, 0, Matriz, ListaSoluciones)



def Algoritmo2(Nodos, FichasMano, N, Matriz, ListaSoluciones):
	if N>len(ListaSoluciones)-1:
		return ListaSoluciones[0]
	FichasManoPodada=sacarFichas(FichasMano, ListaSoluciones[N])
	if buscaSoluciones(Nodos, FichasManoPodada, [], [], 0, Matriz, [])[0]==[]:
		Algoritmo2(Nodos, FichasMano, N+1, Matriz, ListaSoluciones)
	else:
		return ListaSoluciones[N]

def sacarFichas(FichasMano, ListaSoluciones):
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
	
