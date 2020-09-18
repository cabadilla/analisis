import sys, pygame
from pygame.locals import *
from pygame import surface

pygame.init()

class Casillas(pygame.sprite.Sprite):
    def __init__(self,c,imagen):
        self.image=pygame.image.load(imagen)
        self.rect=self.image.get_rect(50,50,(c[0],c[1]))
        self.image=pygame.transform.scale(self.image,(50,50))
        self.coor=c
        
 
        