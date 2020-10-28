from random import *

Matriz=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        
MatrizPixeles=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	    	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		       [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
		       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def Norte(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return Norte((Coords[0]-1, Coords[1]), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Sur(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return Sur((Coords[0]+1, Coords[1]), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Este(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return Este((Coords[0], Coords[1]+1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def Oeste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return Oeste((Coords[0], Coords[1]-1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def NorEste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return NorEste((Coords[0]-1, Coords[1]+1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def SurEste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return SurEste((Coords[0]+1, Coords[1]+1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def SurOeste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return SurOeste((Coords[0]+1, Coords[1]-1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def NorOeste(Coords, Matriz, Tiempo):
	try:
		if Coords[1]>=0 and Coords[0]>=0:
			if Matriz[Coords[0]][Coords[1]]==1:
				return Tiempo
			else:
				return NorOeste((Coords[0]-1, Coords[1]-1), Matriz, Tiempo+1)
		else:
			return False
	except (IndexError):
		return False

def DNorte(fila, columna):
	tiempo=Norte((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila-tiempo][columna]=1


def DSur(fila, columna):
	tiempo=Sur((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila+tiempo][columna]=1

def DEste(fila, columna):
	tiempo=Este((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila][columna+tiempo]=1

def DOeste(fila, columna):
	tiempo=Oeste((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila-tiempo][columna-tiempo]=1

def DNorEste(fila, columna):
	tiempo=NorEste((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila-tiempo][columna+tiempo]=1

def DSurEste(fila, columna):
	tiempo=SurEste((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila+tiempo][columna+tiempo]=1

def DNorOeste(fila, columna):
	tiempo=NorOeste((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila-tiempo][columna-tiempo]=1

def DSurOeste(fila, columna):
	tiempo=SurOeste((fila, columna), Matriz, 0)
	if tiempo!=False:
		MatrizPixeles[fila+tiempo][columna-tiempo]=1

def Fabric(Matriz):
	num=randint(1, 8)
	switch={
		1:DNorte(5,1),
		2:DSur(5,1),
		3:DEste(5,1),
		4:DOeste(5,1),
		5:DNorEste(5,1),
		6:DSurEste(5,1),
		7:DSurOeste(5,1),
		8:DNorOeste(5,1)
	}
	return switch[num]

def Algoritmo(Matriz):
	for i in range(0, 10):
		Fabric(Matriz)
	for j in MatrizPixeles:
		print(j)






Algoritmo(Matriz)
