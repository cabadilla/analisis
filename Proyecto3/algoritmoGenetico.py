from clases import abejas,flores,panal
import numpy
from random import randint

def funcionAdaptabilidadAbejas(abejas):
    '''
    Objetivo: Funcion de adaptabilidad de las abejas, se sacan la mitad de abejas que peor rendimiento dieron y se reproducen solo la mejor mitad
    Recibe: Un array de abejas que es el enjambre del panal
    Retorna: Retorna un array con las mejores abejas que hay en el enjambre actualmetne
    '''
    mayorCantidadFlores=0
    mejorAbeja=0
    mejoresAbejas=[]
    for i in range(6):
        mayorCantidadFlores=0
        for abeja in range(len(abejas)):
            if len(abejas[abeja].polem)>mayorCantidadFlores:
                mayorCantidadFlores=len(abejas[abeja].polem)
                mejorAbeja=abeja
        if(mejorAbeja<len(abejas)):
            mejoresAbejas.append(abejas.pop(mejorAbeja))
    return mejoresAbejas



def funcionAdaptabilidadFlores(flo):
    '''
    Objetivo: Funcion de adaptabilidad de las flores, se sacan la mitad de flores que por rendimiento dieron o que nunca se visitaron y comienzan a morir
    Recibe: Un array de las flores que hay en todo el campo actualmente
    Retorna: Las flores que tuvieron el mejor rendimiento para que estas mismas empiecen a reproducirse
    '''
    mejoresFlores=[]
    mejorFlor=0
    for i in range(50):
        for flor in range(len(flo)-1):
            if len(flo[flor].abejas)>mejorFlor:
                mejorFlor=flor
        if(len(flo[mejorFlor].abejas)!=0) and (len(flo[mejorFlor].abejas)-1<mejorFlor):
            mejoresFlores.append(flo.pop(mejorFlor))
        else:
            mejoresFlores.append(flores((randint(0,49),randint(0,49)),devolverColor()))

    return mejoresFlores

def llenar(binario,num):
    '''
    Objetivo: Funcion que se dedica a rellenar con 0's a la izquierda para mantener los 8 bits
    Recibe: Recibe un numero en binario y un numero de longitud
    Retorna: El numero binario en 8 bits
    '''
    nuevoValor=binario[2:]
    while len(nuevoValor) != num:
        nuevoValor='0'+nuevoValor
    return nuevoValor
    
    
def cruceAbeja(abejaUno,abejaDos):
    '''
    Objetivo: Tiene como objetivo el realizar el cruce de abejas para mezclar los genes entre las mejores abejas
    Recibe: Una abeja padre y una abeja madre
    Retorna: Una abeja con los cromosomas nuevos
    '''
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


    direccionUno=diccionarioDirecciones[abejaUno.direccionFavorita[0]]
    direccionDos=diccionarioDirecciones[abejaDos.direccionFavorita[0]]
    '''for i in range(3):
        num=randint(0,1)
        if num==0:
            cromosomaDireccion+=direccionUno[i]
        else:
            cromosomaDireccion+=direccionDos[i]'''
    cromosomaDireccion+=direccionUno[0]
    muta=randint(0,1)
    cromosomaDireccion+=str(muta)
    cromosomaDireccion+=direccionDos[2]

    colorUno=(llenar(bin(abejaUno.colorFavorito[0]),8),llenar(bin(abejaUno.colorFavorito[1]),8),llenar(bin(abejaUno.colorFavorito[2]),8))
    colorDos=(llenar(bin(abejaDos.colorFavorito[0]),8),llenar(bin(abejaDos.colorFavorito[1]),8),llenar(bin(abejaDos.colorFavorito[2]),8))

    '''for i in range (3):
        for j in range (8):
            num=randint(0,1)
            if num==0:
                cromosomaColor[i]+=colorUno[i][j]
            else:
                cromosomaColor[i]+=colorDos[i][j]'''
    cromosomaColor[0]+=colorUno[0]
    cromosomaColor[2]+=colorDos[2]
    for i in range(4):
        cromosomaColor[1]+=colorUno[1][i]
    for i in [4,5,6,7]:
        cromosomaColor[1]+=colorDos[1][i]
    mutaCromosoma=randint(0,7)
    muta=randint(0,1)
    cromosomaMutado=''
    for i in range(8):
        if(i!=mutaCromosoma):
            cromosomaMutado+=cromosomaColor[1][i]
        else:
            cromosomaMutado+=str(muta)
    cromosomaColor[1]=cromosomaMutado

        
    nuevaAbeja=abejas(diccionarioDirecciones[cromosomaDireccion],(int(cromosomaColor[0],2),int(cromosomaColor[1],2),int(cromosomaColor[2],2)),(0,0))
    return nuevaAbeja

def cruceAbejas(abejas):
    '''
    Objetivo: Funcion que se dedica a escoger la abeja padre y madre para la reproduccion de ellas
    Recibe: El enjambre completo
    Retorna: El nuevo enjambre de esta generacion
    '''
    mejoresAbejas=funcionAdaptabilidadAbejas(abejas)
    nuevasAbejas=[]
    abejaUno=0
    abejaDos=0
    for i in range(12):
        abejaUno=randint(0,len(mejoresAbejas)-1)
        abejaDos=randint(0,len(mejoresAbejas)-1)

        nuevasAbejas.append(cruceAbeja(mejoresAbejas[abejaUno],mejoresAbejas[abejaDos]))

    return nuevasAbejas


def cruceFlor(florUno,florDos):
    '''
    Objetivo: Tiene como objetivo el realizar el cruce de las flores
    Recibe: Una flor madre y una flor padre
    Retorna: La nueva flor que se forma del cruce
    '''
    cromosomasColor=['','','']

    cordsUno=(llenar(bin(florUno.posicion[0]),6),llenar(bin(florUno.posicion[1]),6))
    cordsDos=(llenar(bin(florDos.posicion[0]),6),llenar(bin(florDos.posicion[1]),6))

    posicion1=''
    posicion2=''
    for i in range(3):
        posicion1+=cordsUno[0][i]
    for i in [3,4,5]:
        posicion1+=cordsDos[0][i]

    for i in range(3):
        posicion2+=cordsUno[1][i]
    for i in [3,4,5]:
        posicion2+=cordsDos[1][i]

    if(int(posicion1,2)>49):
        posicion1='110001'
    if(int(posicion2,2)>49):
        posicion2='110001'
    cromosomasPosicion=(posicion1,posicion2)

    colorUno=(llenar(bin(florUno.colorDeFlor[0]),8),llenar(bin(florUno.colorDeFlor[1]),8),llenar(bin(florUno.colorDeFlor[2]),8))
    colorDos=(llenar(bin(florDos.colorDeFlor[0]),8),llenar(bin(florDos.colorDeFlor[1]),8),llenar(bin(florDos.colorDeFlor[2]),8))

    for i in range (3):
        for j in range (8):
            num=randint(0,1)
            if num==0:
                cromosomasColor[i]+=colorUno[i][j]
            else:
                cromosomasColor[i]+=colorDos[i][j]

    nuevaFlor=flores((int(cromosomasPosicion[0],2),int(cromosomasPosicion[1],2)),(int(cromosomasColor[0],2),int(cromosomasColor[1],2),int(cromosomasColor[2],2)))
    return nuevaFlor


def cruceFlores(flores):
    '''
    Objetivo: Controla el cruce de todas las flores y consigo escoge las flores padre
    Recibe: El arreglo de las flores que hay en la generacion actual
    Retorna: Las nuevas flores que van a haber en la generacion
    '''
    mejoresFlores=funcionAdaptabilidadFlores(flores)
    nuevasFlores=[]
    florUno=0
    florDos=0
    for i in range(50):
        florUno=randint(0,len(mejoresFlores)-1)
        florDos=randint(0,len(mejoresFlores)-1)
        nuevasFlores.append(cruceFlor(mejoresFlores[florUno],mejoresFlores[florDos]))

    return nuevasFlores

def devolverColor():
    '''
    Objetivo: Retorna el color favorito para las flores o para las abejas
    Recibe: No recibe
    Retorna: Retorna un random entre los 8 colores que hay
    '''
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
    return colores[randint(1,8)]

def devolverDireccion():
    '''
    Objetivo: Retorna una direccion favorita para las abejas
    Recibe: No recibe
    Retorna: Retorna una direccion random para la direccion favorita
    '''
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
    return diccionarioDirecciones[randint(1,8)]


def generarPoblacionInicialDeAbejas(cantidad, panal):
    '''
    Objetivo: Genera la poblacion inicial de abejas 
    Recibe: La cantidad de abejas a generar y el panal donde se van a almacenar
    Retorna: Un arreglo con la poblacion de abejas
    '''
    poblacion=[]
    for i in range (cantidad):
        poblacion.append(abejas(devolverDireccion(),devolverColor(),panal))
    return poblacion

def generarPoblacionInicialDeFlores(cantidad,n):
    '''
    Objetivo: Genera la poblacion inicial de flores
    Recibe: La cantidad de flores a generar, un n de coordenada
    Retorna: Un arreglo con la poblacion de flores
    '''
    poblacion=[]
    for i in range(cantidad):
        x=randint(0,n-1)
        y=randint(0,n-1)
        poblacion.append(flores((x,y),devolverColor()))
       

    return poblacion
