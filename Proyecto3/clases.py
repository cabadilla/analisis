import pygame
import os
"""
Archivo .py dedicado especialmente para las clases que son utilizadas 
dentro del proyecto, esto con el fin de llevar un mejor orden de en 
donde se encuentra cada cosa y poder exportar un solo archivo y se 
puedan utilizar todas las clases cuando se requieran 
"""

#--------------------------------------Clase de las abejas-----------------------------------------------------
class abejas:
    '''
    Clase abejas, esta clase engloba toda la especie
    de las abejas, con sus caracteristicas definidas
    y sus acciones dentro del programa
    '''
    def __init__(self, DireccionFav, ColorFav, Coordenadas):
        '''
        Objetivo: Constructor de la clase, tiene el objetivo de crear una instancia del tipo abejas
        Recibe: una direccion favorita, un color favorito, unas coordenadas y una generacion de individuo
        Retorna: Un objeto abeja unico con caracteristicas propias
        '''
        self.polem=[] #polem recolectado en una corrida
        self.direccionFavorita=DireccionFav #direccion favorita
        self.colorFavorito=ColorFav #color favorito
        self.coordenadasActuales=Coordenadas #coordenadas donde se encuentra
        self.distanciaRecorrida=0 #distancia que ha recorrido

#--------------------------------------Clase de las flores-----------------------------------------------------
class flores:
    '''
    Clase flores, esta clase engloba toda la especie
    de las flores, con sus caracteristicas definidias
    ademas de las acciones que van a realizar dentro del
    programa
    '''
    def __init__(self, posicionMapa, colorFlor):
        '''
        Objetivo: Constructor de la clase, tiene el objetivo de crear una instancia del tipo flores
        Recibe: Una posicion en la que se va a encontrar la flor, un color de flor y una generacion de individuo
        Retorna: Un objeto flor unico con caracteristicas propias
        '''
        self.posicion=posicionMapa #posicion donde se encuentra
        self.colorDeFlor=colorFlor #color de la flor 
        self.abejas=[] #abejas que han visitado esta flor
        
#--------------------------------------Clase del panal de abejas-----------------------------------------------------
class panal:
    '''
    Clase panal, este objeto es el que va a almacenar
    todas las abejas y dentro de el van a suceder todos los 
    procesos de reproduccion y genetica
    '''
    def __init__(self, ubicacionMapa, abejas):
        '''
        Objetivo: Constructor de la clase, tiene el objetivo de crear una instancia del tipo panal
        Recibe: Una coordenada que es en donde se ubica el panal y un arreglo de abejas que va a definir el enjambre actual
        Retorna: Un objeto panal donde las abejas coexisten
        '''
        self.ubicacionPanal=ubicacionMapa #coordenadas donde se encuentra el panal
        self.enjambre=abejas #enjambre de abejas
        self.imagen=pygame.image.load("imagenes/PanalAbejas.png") #imagen para el despliegue grafico
        self.imagen=pygame.transform.scale(self.imagen,(50,50))

#--------------------------------------Clase para el manejo de archivos-----------------------------------------------------
class controladorTXT:
    '''
    Clase controladorTXT, esta clase esta dedicada para hacer el manejo del
    registro de todas las generaciones para poder ver el algoritmo
    funcionando conforme pasan generaciones 
    '''
    def __init__(self):
        '''
        Objetivo: Tiene como objetivo el abrir un archivo nuevo en blanco con el nombre de ResgistroSimulacion
        Recibe: No recibe nada
        Retorna: El archivo creado en el directorio del proyecto
        '''
        file=open("RegistroSimulacion.txt", "w") #txt que almacena todas las generaciones que han sucedido durante la corrida del programa
        file.close()
        file=open("GeneracionAnterior.txt", "w") #txt que almacena la generacion que se va a ir desplegando conforme se pase de generacion
        file.close()

    def leerTXT(self):
        '''
        Objetivo Tiene como objetivo el leer el archivo txt, e imprimir todas las abejas con los detalles necesarios
        Recibe: No recibe nada
        Retorna: En consola imprime los detalles de las abejas
        '''
        file=open("GeneracionAnterior.txt", "r") #se lee la generacion anterior para desplegarse en el programa
        for lines in file:
            print(file.readline())
        file.close()

    def escribirTXT(self, enjambre, generacion):
        '''
        Objetivo: Tiene el objetivo de escribir toda la generacion actual dentro del txt para manejar su uso
        Recibe: Recibe el enjambre de abejas y la generacion actual
        Retorna: No retorna nada 
        '''
        file=open("RegistroSimulacion.txt", "a") #le hace un append al archivo de los registros simulacion
        file.write("--------------Generacion "+str(generacion)+"--------------"+os.linesep)
        for abeja in enjambre:
            file.write(str(abeja.polem)+os.linesep)
        file.close()

        file=open("GeneracionAnterior.txt", "w") #le hace update a la relacion anterior
        file.write("--------------Generacion "+str(generacion)+"--------------"+os.linesep)
        for abeja in enjambre:
            file.write(str(abeja.polem)+os.linesep)
        file.close()