import pygame
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
    def __init__(self, DireccionFav, ColorFav, Coordenadas, GeneracionActual):
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
        self.generacion=GeneracionActual  #generacion actual

#--------------------------------------Clase de las flores-----------------------------------------------------
class flores:
    '''
    Clase flores, esta clase engloba toda la especie
    de las flores, con sus caracteristicas definidias
    ademas de las acciones que van a realizar dentro del
    programa
    '''
    def __init__(self, posicionMapa, colorFlor, GeneracionActual):
        '''
        Objetivo: Constructor de la clase, tiene el objetivo de crear una instancia del tipo flores
        Recibe: Una posicion en la que se va a encontrar la flor, un color de flor y una generacion de individuo
        Retorna: Un objeto flor unico con caracteristicas propias
        '''
        self.posicion=posicionMapa #posicion donde se encuentra
        self.colorDeFlor=colorFlor #color de la flor
        self.generacion=GeneracionActual #generacion actual 
        self.abejas=[] #abejas que han visitado esta flor
        

#--------------------------------------Clase del panal de abejas-----------------------------------------------------
class panal:
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