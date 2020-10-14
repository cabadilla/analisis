import sys, pygame
from pygame.locals import *
from pygame import surface

pygame.init()

class Casillas():
    def __init__(self,c,imagen):
        self.image=pygame.image.load(imagen)
        self.image=pygame.transform.scale(self.image,(34,34))
        self.coor=c
        self.cordenadasMatriz=(0,0)
        self.estado=0

    def cambiarEscala(self,x):
        self.image=pygame.transform.scale(self.image,x)
        
 
        