def buscaSoluciones(Nodos, FichasMano, SolucionPrincipal, MejorSolucion, N, Matriz):
	'''
	Objetivo: Busca en forma de un algoritmo de Backtracking la mejor solucion que se pueda aplicar dentro del
	tablero de juego, esto para que el algoritmo pueda jugar contra el Jugador
	Recibe: Nodos (lista de nodos que se han puesto en el juegoo), FichasMano(Fichas que tenga el algoritmo disponibles), SolucionPrincipal (Solucion que se va a crear con cada corrida), MejorSolucion (Lista a retornar con la mejor jugada), N (Numero que incrementa con nodos)
	Retorna: La mejor Solucion que pueda realizar el algoritmo para llevar a cabo
	'''
	if N>len(Nodos)-1:
		return MejorSolucion #Si ya se recorrieron todos los nodos del Grafo, se retorna la mejor solucion que se encontro
	else:
		SolucionPrincipal=solucionesCasilla(Nodos[N], FichasMano, Matriz) #Saca la mejor solucion del nodo actual
		MejorSolucion=ComparaLongitudes(SolucionPrincipal, MejorSolucion)
		return [] + buscaSoluciones(Nodos, FichasMano, [], MejorSolucion, N+1, Matriz) #Si no es mejor, se cambia de nodo y se continua

def solucionesCasilla(NodoMatriz, FichasMano, Matriz):
	'''
	Objetivo: Busca la mejor solucion que tenga el nodo que esta siendo evaluado
	Recibe: NodoMatriz (El nodo de la matriz que esta siendo evaluado), FichasMano (Fichas que tenga el algoritmo disponibles), SolucionActual (La solucion que se cree con cada corrida), SolucionFinal (Solucion que se retornara)
	Retorna: Una lista con la mejor solucion que tenga este nodo
	'''
	SolucionFigura=[]
	SolucionColor=[]
	if BuscaJugada(NodoMatriz, FichasMano):
		CombiFigura=CombinacionesFigura(FichasMano, 0)
		CombiColor=CombinacionesColor(FichasMano, 0)
		SolucionFigura=BacktrackingFigura(NodoMatriz, CombiFigura, 0, [], Matriz, [], FichasMano)
		SolucionColor=BacktrackingColor(NodoMatriz, CombiColor, 0, [], Matriz, [], FichasMano)
	return ComparaLongitudes(SolucionFigura, SolucionColor)
def BacktrackingFigura(NodoMatriz, CombiFigura, N, Solucion, Matriz, SolucionFinal, FichasMano):
	'''
	Objetivo: En una forma de backtracking, creando un arbol con muchas soluciones, con cada corrida se 
	actualiza cual es la mejor solucion y esta es la que se retornara al final
	Recibe: Posicion (x,y de la forma fila, columna de la casilla donde se va a jugar), FichasMano(Fichas disponibles que hay para jugar), Direccion(Direccion en la que tiene que ir el algoritmo), Solucion(Solucion que se va a obtener), n(Numero para indexar las fichas)
	Retorna: La mejor solucion que haya creado para esa posicion
	'''
	if N>5:
		Lista=[]
		for FichaSolucion in SolucionFinal:
			Lista.append([FichasMano.index(FichaSolucion[0]), FichaSolucion[1]])
		return Lista
	else:
		if NodoMatriz.getIzquierda()==None:
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiFigura[N], 0, "Izquierda", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		if NodoMatriz.getDerecha()==None:
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiFigura[N], 0, "Derecha", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		if NodoMatriz.getArriba()==None:
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiFigura[N], 0, "Arriba", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		if NodoMatriz.getAbajo()==None:
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiFigura[N], 0, "Abajo", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		return [] + BacktrackingFigura(NodoMatriz, CombiFigura, N+1, [], Matriz, SolucionFinal, FichasMano)

def BacktrackingColor(NodoMatriz, CombiColor, N, Solucion, Matriz, SolucionFinal, FichasMano):
	'''
	Objetivo: En una forma de backtracking, creando un arbol con muchas soluciones, con cada corrida se 
	actualiza cual es la mejor solucion y esta es la que se retornara al final
	Recibe: Posicion (x,y de la forma fila, columna de la casilla donde se va a jugar), FichasMano(Fichas disponibles que hay para jugar), Direccion(Direccion en la que tiene que ir el algoritmo), Solucion(Solucion que se va a obtener), n(Numero para indexar las fichas)
	Retorna: La mejor solucion que haya creado para esa posicion
	'''
	if N>5:
		Lista=[]
		for FichaSolucion in SolucionFinal:
			Lista.append([FichasMano.index(FichaSolucion[0]), FichaSolucion[1]])
		return Lista
	else:
		if NodoMatriz.getIzquierda()==None: #Si se puede poner una ficha al a izquierda, busca las soluciones de ese movimiento
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiColor[N], 0, "Izquierda", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		if NodoMatriz.getDerecha()==None: #Si se puede poner una ficha al a derecha, busca las soluciones de ese movimiento
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiColor[N], 0, "Derecha", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		if NodoMatriz.getArriba()==None: #Si se puede poner una ficha arriba, busca las soluciones de ese movimiento
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiColor[N], 0, "Arriba", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		if NodoMatriz.getAbajo()==None: #Si se puede poner una ficha abajo, busca las soluciones de ese movimiento
			Solucion=CalculaMovimientos(NodoMatriz, Matriz, CombiColor[N], 0, "Abajo", [])
			SolucionFinal=ComparaLongitudes(Solucion, SolucionFinal)
		return [] + BacktrackingColor(NodoMatriz, CombiColor, N+1, [], Matriz, SolucionFinal, FichasMano)
	
def CalculaMovimientos(NodoMatriz, Matriz, Combinacion, N, Direccion, SolucionFinal):
	'''
	Objetivo: Realiza los 3 tipos de movimientos que estan permitidos
	Recibe: -
	Retorna: El movimiento de la mayor puntuacion
	'''
	if validaIgualdad(NodoMatriz, Combinacion[0]) and len(Combinacion)>1:
		rotate(Combinacion)
	if validaJugada(NodoMatriz, Combinacion[N]):
		if Direccion=="Izquierda":
			ListaSoluciones=sorted([Abajo(Matriz, NodoMatriz.getFila(), NodoMatriz.getColumna()-1, Combinacion, N), Izquierda(Matriz, NodoMatriz.getFila(), NodoMatriz.getColumna()-1, Combinacion, N), Derecha(Matriz, NodoMatriz.getFila(), NodoMatriz.getColumna()-1, Combinacion, N)], key=len, reverse=True) #Lista para las soluciones y buscar cual es la mejor de todas
			SolucionFinal=ListaSoluciones[0]
		elif Direccion=="Derecha":
			ListaSoluciones=sorted([Abajo(Matriz, NodoMatriz.getFila(), NodoMatriz.getColumna()+1, Combinacion, N), Derecha(Matriz, NodoMatriz.getFila(), NodoMatriz.getColumna()+1, Combinacion, N), Arriba(Matriz, NodoMatriz.getFila(), NodoMatriz.getColumna()+1, Combinacion, N)], key=len, reverse=True) #Lista para las soluciones y buscar cual es la mejor de todas
			SolucionFinal=ListaSoluciones[0]
		elif Direccion=="Arriba":
			ListaSoluciones=sorted([Izquierda(Matriz, NodoMatriz.getFila()-1, NodoMatriz.getColumna(), Combinacion, N), Arriba(Matriz, NodoMatriz.getFila()-1, NodoMatriz.getColumna(), Combinacion, N), Derecha(Matriz, NodoMatriz.getFila()-1, NodoMatriz.getColumna(), Combinacion, N)], key=len, reverse=True) #Lista para las soluciones y buscar cual es la mejor de todas
			SolucionFinal=ListaSoluciones[0]
		else:
			ListaSoluciones=sorted([Izquierda(Matriz, NodoMatriz.getFila()+1, NodoMatriz.getColumna(), Combinacion, N), Abajo(Matriz, NodoMatriz.getFila()+1, NodoMatriz.getColumna(), Combinacion, N), Derecha(Matriz, NodoMatriz.getFila()+1, NodoMatriz.getColumna(), Combinacion, N)], key=len, reverse=True) #Lista para las soluciones y buscar cual es la mejor de todas
			SolucionFinal=ListaSoluciones[0]
	return SolucionFinal

def Izquierda(Matriz, fila, columna, Combinacion, N):
	'''
	Objetivo: Coloca todas las fichas en direccion de izquierda para calcular el puntaje al hacer esto
	Recibe: Matriz para realizar las pruebas, fila donde se va a insertar, columna donde se va a insertar, Combinacion actual, N para indexar
	Retorna: Puntuacion que genera este movimiento
	'''
	Solucion=[]
	for i in range(N, len(Combinacion)):
		if valido(Matriz, Combinacion[i], fila, columna):
			Solucion.append((Combinacion[i], (fila, columna)))
		else:
			break
		columna-=1
	return Solucion

def Derecha(Matriz, fila, columna, Combinacion, N):
	'''
	Objetivo: Coloca todas las fichas en direccion de derecha para calcular el puntaje al hacer esto
	Recibe: Matriz para realizar las pruebas, fila donde se va a insertar, columna donde se va a insertar, Combinacion actual, N para indexar
	Retorna: Puntuacion que genera este movimiento
	'''
	Solucion=[]
	for i in range(N, len(Combinacion)):
		if valido(Matriz, Combinacion[i], fila, columna):
			Solucion.append((Combinacion[i], (fila, columna)))
		else:
			break
		columna+=1
	return Solucion

def Arriba(Matriz, fila, columna, Combinacion, N):
	'''
	Objetivo: Coloca todas las fichas en direccion arriba para calcular el puntaje al hacer esto
	Recibe: Matriz para realizar las pruebas, fila donde se va a insertar, columna donde se va a insertar, Combinacion actual, N para indexar
	Retorna: Puntuacion que genera este movimiento
	'''
	Solucion=[]
	for i in range(N, len(Combinacion)):
		if valido(Matriz, Combinacion[i], fila, columna):
			Solucion.append((Combinacion[i], (fila, columna)))
		else:
			break
		fila-=1
	return Solucion

def Abajo(Matriz, fila, columna, Combinacion, N):
	'''
	Objetivo: Coloca todas las fichas en direccion abajo para calcular el puntaje al hacer esto
	Recibe: Matriz para realizar las pruebas, fila donde se va a insertar, columna donde se va a insertar, Combinacion actual, N para indexar
	Retorna: Puntuacion que genera este movimiento
	'''
	Solucion=[]
	for i in range(N, len(Combinacion)):
		if valido(Matriz, Combinacion[i], fila, columna):
			Solucion.append((Combinacion[i], (fila, columna)))
		else:
			break
		fila+=1
	return Solucion

def rotate(Combinacion):
	'''
	Objetivo: Rotar el primer elemento de la lista
	Recibe: Una lista
	Retorna: La lista rotada
	'''
	Primero = Combinacion[0];
	for i in range(0, len(Combinacion)-1):
		Combinacion[i] = Combinacion[i+1]
	Combinacion[i]= Primero
	return Combinacion

def valido(Matriz, Ficha, fila, columna):
	'''
	Objetivo: Valida y verifica que la ficha que en este momento se vaya a colocar se pueda colocar
	y en caso de que se pueda colocar retorna True
	Recibe: Matriz(prueba para simular los movimientos), Posicion(donde se van a ir colocando las fichas), Ficha(Ficha que se va a colocar), Direccion(Direccion en la que solo se pueden colocar fichas)
	Retorna: True si la jugada se puede y False si es invalida
	'''
	try: #Revisa en las 4 direcciones que no haya una ficha que invalide el movimiento
		if Matriz[fila][columna+1]!=None:
			c=columna
			while Matriz[fila][c+1]!=None:
				if not validaJugada(Ficha, Matriz[fila][c+1]): #Si hay un nodo o alguna ficha, valida que se pueda poner
					return False
				c+=1
		if Matriz[fila][columna-1]!=None:
			c=columna
			while (Matriz[fila][c-1]!=None):
				if not validaJugada(Ficha, Matriz[fila][c-1]): #Si hay un nodo o alguna ficha, valida que se pueda poner
					return False
				c-=1
		if Matriz[fila-1][columna]!=None:
			f=fila
			while (Matriz[f-1][columna]!=None):
				if not validaJugada(Ficha, Matriz[f-1][columna]): #Si hay un nodo o alguna ficha, valida que se pueda poner
					return False
				f-=1
		if Matriz[fila+1][columna]!=None:
			f=fila
			while (Matriz[f+1][columna]!=None):
				if not validaJugada(Ficha, Matriz[f+1][columna]): #Si hay un nodo o alguna ficha, valida que se pueda poner
					return False
				f+=1
		return True
	except (IndexError):
		pass #En caso de un error de index por espacio de la matriz, se omite porque la matriz puede crecer
	
#------------------------------------------------------------Funciones auxiliares-------------------------------------------------------------
def CombinacionesFigura(ListaFichas, N):
	'''
	Objetivo: Funcion que saca las cominaciones de fichas que tenga dependiendo de la figura
	Recibe: Fichas que tenga en la mano y un numero para poder iterar
	Retorna: La lista de las combinaciones
	'''
	if N>5:
		return []
	else:
		Lista=[]
		Lista.append(ListaFichas[N])
		for i in range(N+1, 6):
			if validaFigura(Lista[0], ListaFichas[i]):
				Lista.append(ListaFichas[i])
		return [Lista]+CombinacionesFigura(ListaFichas, N+1) #Por medio de recursion de pila realiza todas las posibles combinaciones dentro de las fichas, esto con el fin de realizar las jugadas con la mayor cantidad de fichas

def CombinacionesColor(ListaFichas, N):
	'''
	Objetivo: Funcion que saca las cominaciones de fichas que tenga dependiendo del color
	Recibe: Fichas que tenga en la mano y un numero para poder iterar
	Retorna: La lista de las combinaciones
	'''
	if N>5:
		return []
	else:
		Lista=[]
		Lista.append(ListaFichas[N])
		for i in range(N+1, 6):
			if validaColor(Lista[0], ListaFichas[i]):
				Lista.append(ListaFichas[i])
		return [Lista]+CombinacionesColor(ListaFichas, N+1)  #Por medio de recursion de pila realiza todas las posibles combinaciones dentro de las fichas, esto con el fin de realizar las jugadas con la mayor cantidad de fichas

def BuscaJugada(Nodo, FichasMano):
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

def ComparaLongitudes(Lista1, Lista2):
	'''
	Objetivo: Retorna la lista que tenga una mayor longitud
	Recibe: Dos listas
	Retorna: La lista de mayor tamagno
	'''
	return Lista1 if (len(Lista1)>=len(Lista2)) else Lista2

#------------------------------------------------------------Funciones de Validacion-------------------------------------------------------------
def validaFigura(Nodo, Ficha):
	'''
	Objetivo: Verifica que la figura sea la misma y que a la vez el color sea diferente
	Recibe: Nodo actual, ficha actual
	Retorna: True si se cumple, False si no
	'''
	return Nodo.getForma()==Ficha.getForma() and Nodo.getColor()!=Ficha.getColor()

def validaColor(Nodo, Ficha):
	'''
	Objetivo: Verifica que el color sea el mismo y que a la vez la figura sea diferente
	Recibe: Nodo actual, ficha actual
	Retorna: True si se cumple, False si no
	'''
	return Nodo.getColor()==Ficha.getColor() and Nodo.getForma()!=Ficha.getForma()

def validaIgualdad(Nodo, Ficha):
	'''
	Objetivo: Verifica que ambas fichas sean diferentes
	Recibe: Nodo actual, ficha actual
	Retorna: True si se cumple, False si no
	'''
	return Nodo.getForma()==Ficha.getForma() and Nodo.getColor()==Ficha.getColor()

def validaJugada(Nodo, Ficha):
	'''
	Objetivo: Valida que una ficha pueda ser colocada junto al nodo
	Recibe: Nodo actual, ficha actual
	Retorna: True si al menos una se cumple, False si ninguna
	'''
	return validaFigura(Nodo, Ficha) or validaColor(Nodo, Ficha)