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

def Norte(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		elif Coords[0]>=0:
			return Norte((Coords[0]-1, Coords[1]), Matriz)
		else:
			return False
	except (IndexError):
		return False 

def Sur(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		else:
			return Sur((Coords[0]+1, Coords[1]), Matriz)
	except (IndexError):
		return False

def Este(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		else:
			return Este((Coords[0], Coords[1]+1), Matriz)
	except (IndexError):
		return False

def Oeste(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		elif Coords[1]>=0 and Coords[0]>=0:
			return Oeste((Coords[0], Coords[1]-1), Matriz)
		else:
			return False
	except (IndexError):
		return False

def NorEste(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		else:
			return NorEste((Coords[0]-1, Coords[1]+1), Matriz)
	except (IndexError):
		return False

def SurEste(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		else:
			return SurEste((Coords[0]+1, Coords[1]+1), Matriz)
	except (IndexError):
		return False

def SurOeste(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		else:
			return SurOeste((Coords[0]+1, Coords[1]-1), Matriz)
	except (IndexError):
		return False

def NorOeste(Coords, Matriz):
	try:
		if Matriz[Coords[0]][Coords[1]]==1:
			return True
		elif Coords[0]>=0 and Coords[1]>=0:
			return NorOeste((Coords[0]-1, Coords[1]-1), Matriz)
		else:
			return False
	except (IndexError):
		return False

def Fabric(Matriz):
	num=randint(1, 8)
	switch={
		1:Norte((5, 1), Matriz),
		2:Sur((5, 1), Matriz),
		3:Este((5, 1), Matriz),
		4:Oeste((5, 1), Matriz),
		5:NorEste((5, 1), Matriz),
		6:SurEste((5, 1), Matriz),
		7:SurOeste((5, 1), Matriz),
		8:NorOeste((5, 1), Matriz)
	}
	print(num)
	return switch[num]

def Algoritmo(Matriz):
	for i in range(0, 10):
		print(Fabric(Matriz))



Algoritmo(Matriz)