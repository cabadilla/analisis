import sys, pygame
from pygame.locals import *
from pygame import surface

class abejas:
    def __init__(self,dire,color,coor,gene):
        self.polen=[]
        self.direccionFavorita=dire
        self.colorFavorito=color
        self.coordenadas=coor
        self.distanciaRecorrida=0
        self.generacion=gene

class flores:
    def __init__(self,posi,color,gene):
        self.posicion=posi
        self.colorFavorito=color
        self.coordenadas=posi
        self.abejas=[]
        self.generacion=gene

class panal:
    def __init__(self,coord,abejas):
        self.coordenadas=coord
        self.enjambre=abejas
        self.imagen=pygame.image.load("imagenes/PanalAbejas.png")
        self.imagen=pygame.transform.scale(self.imagen,(50,50))