from Algoritmo1 import *


def buscaSoluciones2(Nodos, FichasMano, N, Matriz, ListaSoluciones)
	Soluciones=buscaSoluciones(Nodos, FichasMano, [], [], 0, Matriz, [])
	ListaSoluciones=Quicksort(Soluciones[1])
	return Algoritmo2(Nodos, FichasMano, 0, Matriz, ListaSoluciones)



def Algoritmo2(Nodos, FichasMano, N, Matriz, ListaSoluciones):
	if N>len(ListaSoluciones)-1:
		return ListaSoluciones[0]
	FichasManoPodada=sacarFichas(FichasMano, ListaSoluciones[N])
	if buscaSoluciones(Nodos, FichasManoPodada, [], [], 0, Matriz, [])[0]==[]:
		Algoritmo2(Nodos, FichasMano, N+1, Matriz)
	else:
		return ListaSoluciones[N]

def sacarFichas(FichasMano, ListaSoluciones):
	Mano=FichasMano[:]
	for i in ListaSoluciones:
		if not isinstance(i, int):
			Mano.remove(i[0])
	return Mano

def quicksort():
	pass
