'''
Nodo.forma
Nodo.color
Nodo.fila
Nodo.columna
Ficha.forma
Ficha.color
'''

def buscaSoluciones(Nodos, FichasMano, SolucionPrincipal, MejorSolucion, N):
	'''
	Objetivo: Busca en forma de un algoritmo de Backtracking la mejor solucion que se pueda aplicar dentro del
	tablero de juego, esto para que el algoritmo pueda jugar contra el Jugador
	Recibe: Nodos (lista de nodos que se han puesto en el juegoo), FichasMano(Fichas que tenga el algoritmo disponibles), SolucionPrincipal (Solucion que se va a crear con cada corrida), MejorSolucion (Lista a retornar con la mejor jugada), N (Numero que incrementa con nodos)
	Retorna: La mejor Solucion que pueda realizar el algoritmo para llevar a cabo
	'''
	if N>len(Nodos)-1:
		return MejorSolucion #Si ya se recorrieron todos los nodos del Grafo, se retorna la mejor solucion que se encontro
	else:
		SolucionPrincipal=solucionesCasilla(Nodo[N], FichasMano, []) #Saca la mejor solucion del nodo actual
		if len(SolucionPrincipal)>len(MejorSolucion): #Si la solucion actual es mejor que la que ahorita esta, se cambia la solucion Final
			MejorSolucion=SolucionPrincipal
		buscaSoluciones(Nodos, FichasMano, [], MejorSolucion, N+1) #Si no es mejor, se cambia de nodo y se continua

def solucionesCasilla(NodoMatriz, FichasMano, SolucionActual, SolucionFinal):
	'''
	Objetivo: Busca la mejor solucion que tenga el nodo que esta siendo evaluado
	Recibe: NodoMatriz (El nodo de la matriz que esta siendo evaluado), FichasMano (Fichas que tenga el algoritmo disponibles), SolucionActual (La solucion que se cree con cada corrida), SolucionFinal (Solucion que se retornara)
	Retorna: Una lista con la mejor solucion que tenga este nodo
	'''
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
	'''
	Objetivo: En una forma de backtracking, creando un arbol con muchas soluciones, con cada corrida se 
	actualiza cual es la mejor solucion y esta es la que se retornara al final
	Recibe: Posicion (x,y de la forma fila, columna de la casilla donde se va a jugar), FichasMano(Fichas disponibles que hay para jugar), Direccion(Direccion en la que tiene que ir el algoritmo), Solucion(Solucion que se va a obtener), n(Numero para indexar las fichas)
	Retorna: La mejor solucion que haya creado para esa posicion
	'''
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

def valido(Matriz, Posicion, Ficha, Direccion):
	'''
	Objetivo: Valida y verifica que la ficha que en este momento se vaya a colocar se pueda colocar
	y en caso de que se pueda colocar retorna True
	Recibe: Matriz(prueba para simular los movimientos), Posicion(donde se van a ir colocando las fichas), Ficha(Ficha que se va a colocar), Direccion(Direccion en la que solo se pueden colocar fichas)
	Retorna: True si la jugada se puede y False si es invalida
	'''
	fila=Posicion[0] #fila donde se esta posicionando el puntero para poner la ficha
	columna=Posicion[1] #columna donde se esta posicionando el puntero para poner la ficha
	if Direccion=="Izquierda" or Direccion=="Derecha": #ya que si es se va a poner hacia la izquierda o hacia la derecha solo se puede en esa posicion, siempre se tienen que fijar en las fichas que estan hacia la izquierda y hacia la derecha
		for i in range(columna, len(matriz(fila))): #desde la columna actual hasta el fin del tamagno de la matriz
			if Matriz[fila][i]==None: #Si encuentra un None quiere decir que ya no hay mas nodos para recorrer
				break
			if Matriz[fila][i].color==Ficha.color and Matriz[fila][i].forma==Ficha.forma: #por cada nodo que recorra tiene que verificar si la ficha que vamos a colocar ya se encuentra
				return False
		for i in range(columna, 0, -1): #desde la columna actual hasta el inicio del tamagno de la matriz
			if Matriz[fila][i]==None:
				break
			if Matriz[fila][i].color==Ficha.color and Matriz[fila][i].forma==Ficha.forma: #por cada nodo que se recorra tiene que verificar si la ficha que vamos a colocar ya se encuentra
				return False
		return (validaFigura(Matriz[fila][columna+1], Ficha) or validaColor(Matriz[fila][columna+1], Ficha)) if (Direccion=="Izquierda") else (validaFigura(Matriz[fila][columna-1], Ficha) or validaColor(Matriz[fila][columna-1], Ficha)) #si la ficha no se encuentra, vamos a retornar la validez del movimiento(si el color== and figura!= or color!= and figura==)
	else: #si la direccion no era izquierda o derecha, se deduce que es arriba o abajo
		for i in range(fila, len(Matriz)): #desde la fila actual hasta el final del tamagno de la matriz
			if Matriz[i][columna]==None:
				break
			if Matriz[i][columna].color==Ficha.color and Matriz[i][columna].fomra==Ficha.forma: #por cada nodo que se recorra tiene que verificar si la ficha que vamos a colocar ya se encuentra
				return False
		for i in range(fila, 0, -1): #desde la fila actual hasta el inicio del tamagno de la matriz
			if Matriz[i][columna]==None: #si encuentra un None quiere decir que ya no hay mas nodos para recorrer
				break
			if Matriz[i][columna].color==Ficha.color and Matriz[i][columna].fomra==Ficha.forma: #por cada nodo que recorra tiene que verificar si la ficha que vamos a colocar ya se encuentra
				return False
		return (validaFigura(Matriz[fila+1][columna], Ficha) or validaColor(Matriz[fila+1][columna], Ficha)) if (Direccion=="Arriba") else (validaFigura(Matriz[fila-1][columna], Ficha) or validaColor(Matriz[fila-1][columna], Ficha))#si la ficha no se encuentra, vamos a retornar la validez del movimiento(si el color== and figura!= or color!= and figura==)

def Jugada(Nodo, FichasMano):
	'''
	Objetivo: Verifica si existe alguna jugada dentro de las fichas que tenemos, esto para podar que si no existe
	no se tenga que gastar tiempo de ejecucion
	Recibe: Nodo actual y FichasMano
	Retorna: True si existe alguna jugada en este nodo, False de lo contrario
	'''
	for Ficha in FichasMano: #por cada ficha en la mano
		if validaFigura(Nodo, Ficha): #si la figura es la misma y el color es diferente es valido
			return True
		if validaColor(Nodo, Ficha): #si el color es el mismo y la figura diferente es valido
			return True
	return False #si ambas funciones fueron falsas para todas las fichas, no hay jugada en este nodo

def validaFigura(Nodo, Ficha):
	'''
	Objetivo: Verifica que la figura sea la misma y que a la vez el color sea diferente
	Recibe: Nodo actual, ficha actual
	Retorna: True si se cumple, False si no
	'''
	return Nodo.forma==Ficha.forma and Nodo.color!=Ficha.color

def validaColor(Nodo, Ficha):
	'''
	Objetivo: Verifica que el color sea el mismo y que a la vez la figura sea diferente
	Recibe: Nodo actual, ficha actual
	Retorna: True si se cumple, False si no
	'''
	return Nodo.color==Ficha.color and Nodo.forma!=Ficha.forma

