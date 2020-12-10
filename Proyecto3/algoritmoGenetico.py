from clases import abejas,flores
import numpy
from random import randint

def funcionAdaptabilidadAbejas(abejas):
    mayorCantidadFlores=0
    mejorAbeja=0
    mejoresAbejas=[]
    for i in range(6):
        mayorCantidadFlores=0
        for abeja in range(len(abejas)):
            if len(abejas[abeja].polen)>mayorCantidadFlores:
                mayorCantidadFlores=len(abejas[abeja].polen)
                mejorAbeja=abeja
        mejoresAbejas.append(abejas.pop(mejorAbeja))
    return mejoresAbejas



def funcionAdaptabilidadFlores(flores):
    mejoresFlores=[]
    mejorFlor=0
    for i in range(10):
        for flor in range(len(flores)):
            if len(flores[i].abejas)>mejorFlor:
                mejorFlor=flor
        mejoresFlores.append(abejas.pop(mejorFlor))

    return mejoresFlores

def llenar(binario,num):
    nuevoValor=binario[2:]
    while len(nuevoValor) != num:
        nuevoValor='0'+nuevoValor
    return nuevoValor
    
    
def cruceAbeja(abejaUno,abejaDos):
    cromosomaDireccion=''
    cromosomaColor=['','','']

   
    diccionarioDirecciones={
        'N':'000',
        'S':'001',
        'E':'010',
        'O':'011',
        'NE':'100',
        'NO':'101',
        'SE':'110',
        'SO':'111',
        '000':'N',
        '001':'S',
        '010':'E',
        '011':'O',
        '100':'NE',
        '101':'NO',
        '110':'SE',
        '111':'SO'
    }


    direccionUno=diccionarioDirecciones[abejaUno.direccionFavorita]
    direccionDos=diccionarioDirecciones[abejaDos.direccionFavorita]
    for i in range(3):
        num=randint(0,1)
        if num==0:
            cromosomaDireccion+=direccionUno[i]
        else:
            cromosomaDireccion+=direccionDos[i]

    colorUno=(llenar(bin(abejaUno.colorFavorito[0])),llenar(bin(abejaUno.colorFavorito[1])),llenar(bin(abejaUno.colorFavorito[2])),8)
    colorDos=(llenar(bin(abejaDos.colorFavorito[0])),llenar(bin(abejaDos.colorFavorito[1])),llenar(bin(abejaDos.colorFavorito[2])),8)

    for i in range (3):
        for j in range (8):
            num=randint(0,1)
            if num==0:
                cromosomaColor[i]+=colorUno[i][j]
            else:
                cromosomaColor[i]+=colorDos[i][j]
        
    nuevaAbeja=abejas(diccionarioDirecciones[cromosomaDireccion],(int(cromosomaColor[0],2),int(cromosomaColor[1],2),int(cromosomaColor[2],2)),(0,0))
    return nuevaAbeja

def cruceAbejas(abejas):
    mejoresAbejas=funcionAdaptabilidadAbejas(abejas)
    nuevasAbejas=[]
    abejaUno=0
    abejaDos=0
    for i in range(12):
        abejaUno=randint(0,len(mejoresAbejas))
        abejaDos=randint(0,len(mejoresAbejas))

        nuevasAbejas.append(cruceAbeja(mejoresAbejas[abejaUno],mejoresAbejas[abejaDos]))

    return nuevasAbejas


def cruceFlor(florUno,florDos):
    cromosomasPosicion=('','')
    cromosomasColor=('','','')

    cordsUno=(llenar(bin(florUno.posicion[0]),6),llenar(bin(florUno.posicion[1]),7))
    cordsDos=(llenar(bin(florDos.posicion[0]),6),llenar(bin(florDos.posicion[1]),7))

    for i in range (2):
        for j in range (7):
            num=randint(0,1)
            if num==0:
                cromosomasPosicion[i]+=cordsUno[i][j]
            else:
                cromosomasPosicion[i]+=cordsDos[i][j]


    colorUno=(llenar(bin(florUno.colorFavorito[0])),llenar(bin(florUno.colorFavorito[1])),llenar(bin(florUno.colorFavorito[2])),8)
    colorDos=(llenar(bin(florDos.colorFavorito[0])),llenar(bin(florDos.colorFavorito[1])),llenar(bin(florDos.colorFavorito[2])),8)

    for i in range (3):
        for j in range (8):
            num=randint(0,1)
            if num==0:
                cromosomasColor[i]+=colorUno[i][j]
            else:
                cromosomasColor[i]+=colorDos[i][j]

    nuevaFlor=flores((int(cromosomasPosicion[0],2),int(cromosomasPosicion[1],2)),(int(cromosomasColor[0],2),int(cromosomasColor[1],2),int(cromosomasColor[2],2)))
    


def cruceFlores(flores):
    mejoresFlores=funcionAdaptabilidadAbejas(flores)
    nuevasFlores=[]
    florUno=0
    florDos=0
    for i in range(20):
        florUno=randint(0,len(mejoresFlores))
        florDos=randint(0,len(mejoresFlores))

        nuevasAbejas.append(cruceFlor(mejoresFlores[florUno],mejoresFlores[florDos]))

    return nuevasFlores

def devolverColor():
    colores={
        1:(255,51,51),
        2:(255,242,51),
        3:(120,255,51),
        4:(51,255,220),
        5:(121,255,219),
        6:(163,51,255),
        7:(255,171,51),
        8:(254,7,160)
    }
    return colores[randint(1,9)]

def devolverDireccion():
    diccionarioDirecciones={
        1:('N','000'),
        2:('S','001'),
        3:('E','010'),
        4:('O','011'),
        5:('NE','100'),
        6:('NO','101'),
        7:('SE','110'),
        8:('SO','111')
       
    }
    return diccionarioDirecciones[randint(1,9)]


def generarPoblacionInicialDeAbejas(cantidad, panal):
    poblacion=[]
    for i in range (cantidad):
        poblacion.append(abejas(devolverDireccion(),devolverColor(),panal,1))
    return poblacion

def generarPoblacionInicialDeFlores(cantidad):
    poblacion=[]

    x=randint(0,101)
    y=randint(0,101)

    for i in range(cantidad):
        poblacion.append(flores((x,y),devolverColor(),1))

    return poblacion
