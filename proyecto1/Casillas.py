import sys, pygame
from pygame.locals import *
from pygame import surface

pygame.init()

class Casillas(pygame.sprite.Sprite):
    def __init__(self,c):
        self.image=pygame.image.load("imagenes/cuadro.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.coor=c
        
 
        