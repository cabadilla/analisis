from clases import abejas,flores
import numpy
from random import randint

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

print(diccionarioDirecciones['000'])

direccionUno=diccionarioDirecciones['N']
direccionDos=diccionarioDirecciones['SO']
for i in range(3):
    num=randint(0,1)
    if num==0:
        cromosomaDireccion+=direccionUno[i]
    else:
        cromosomaDireccion+=direccionDos[i]


def llenar(binario,num):
    nuevoValor=binario[2:]
    while len(nuevoValor) != num:
        nuevoValor='0'+nuevoValor
    return nuevoValor
    
print(llenar(bin(45),10))

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

print(diccionarioDirecciones[3])

