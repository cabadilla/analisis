def buscaSoluciones(Nodos, FichasMano, SolucionPrincipal, MejorSolucion, N):
	if N>len(Nodos)-1:
		return MejorSolucion #Si ya se recorrieron todos los nodos del Grafo, se retorna la mejor solucion que se encontro
	else:
		SolucionPrincipal=solucionesCasilla(Nodo[N], FichasMano, []) #Saca la mejor solucion del nodo actual
		if len(SolucionPrincipal)>len(MejorSolucion): #Si la solucion actual es mejor que la que ahorita esta, se cambia la solucion Final
			MejorSolucion=SolucionPrincipal
		buscaSoluciones(Nodos, FichasMano, [], MejorSolucion, N+1) #Si no es mejor, se cambia de nodo y se continua

def solucionesCasilla(NodoMatriz, FichasMano, SolucionActual, SolucionFinal):
	if Jugada(NodoMatriz, FichasMano): #Si existe alguna posibilidad con las fichas que se tienen en la mano, sigue
		if NodoMatriz.getIzquierda()==None: #Verifica todas las jugadas hacia la izquierda de ese nodo
			SolucionActual=Backtracking((NodoMatriz.fila, NodoMatriz.columna-1), FichasMano, "Izquierda", 0) #Busca la mejor solucion hacia la izquierda
			if len(SolucionActual)>len(SolucionFinal):
				SolucionFinal=SolucionActual
		if NodoMatriz.getDerecha()==None: #Verifica todas las jugadas hacia la derecha de ese nodo
			SolucionActual=Backtracking((NodoMatriz.fila, NodoMatriz.columna+1), FichasMano, "Derecha", 0) #Busca la mejor solucion hacia la derecha
			if len(SolucionActual)>len(SolucionFinal):
				SolucionFinal=SolucionActual
		if NodoMatriz.getArriba()==None: #Verifica todas las jugadas abajo de ese nodo
			SolucionActual=Backtracking((NodoMatriz.fila-1, NodoMatriz.columna), FichasMano, "Arriba", 0) #Busca la mejor solucion hacia arriba
			if len(SolucionActual)>len(SolucionFinal):
				SolucionFinal=SolucionActual
		if NodoMatriz.getAbajo()==None: #Verifica todas las jugadas hacia abajo de ese nodo
			SolucionActual=Backtracking((NodoMatriz.fila+1, NodoMatriz.columna), FichasMano, "Abajo", 0) #Busca la mejor solucion hacia abajo
			if len(SolucionActual)>len(SolucionFinal):
				SolucionFinal=SolucionActual
	return SolucionFinal #Cuando encuentre la mejor solucion de ese nodo la retorna

def Backtracking(Posicion, FichasMano, Direccion, Solucion, n):
	if Direccion=="Izquierda": #Si la direccion es hacia la izquierda prueba todas las fichas que tiene hacia la izquierda 
		if valido(): #Si se puede poner la ficha en esa direccion sigue
			Solucion.append((n, Posicion)) #Se coloca la ficha en la solucion y se continua
			Matriz[Posicion[0]][Posicion[1]]=FichasMano[n] #Se coloca la ficha en la matriz para poder simular la jugada completa
			Backtracking((Posicion[0], Posicion[1]-1), FichasMano, Direccion, Solucion, n+1) #Se repite con otra ficha
		elif n<len(FichasMano): #Si no se pudo poner la ficha y n sigue siendo menor que la cantidad de fichas, se prueba con otra ficha
			Backtracking(Posicion, FichasMano, Direccion, Solucion, n+1)
	elif Direccion=="Derecha":
		if valido():
			Solucion.append(FichasMano[n])
			Matriz[Posicion[0]][Posicion[1]]=FichasMano[n]
			Backtracking((Posicion[0], Posicion[1]+1), FichasMano, Direccion, Solucion, n+1)
		elif n<len(FichasMano):
			Backtracking(Posicion, FichasMano, Direccion, Solucion, n+1)
	elif Direccion=="Arriba":
		if valido():
			Solucion.append(FichasMano[n])
			Matriz[Posicion[0]][Posicion[1]]=FichasMano[n]
			Backtracking((Posicion[0]-1, Posicion[1]), FichasMano, Direccion, Solucion, n+1)
		elif n<len(FichasMano):
			Backtracking(Posicion, FichasMano, Direccion, Solucion, n+1)
	else:
		if valido():
			Solucion.append(FichasMano[n])
			Matriz[Posicion[0]][Posicion[1]]=FichasMano[n]
			Backtracking((Posicion[0]+1, Posicion[1]), FichasMano, Direccion, Solucion, n+1)
		elif n<len(FichasMano):
			Backtracking(Posicion, FichasMano, Direccion, Solucion, n+1)
	return Solucion	#Si se acabaron las pruebas se retorna la solucion

def valido():
	pass