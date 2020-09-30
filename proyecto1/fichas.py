from random import randint
import pygame
from Casillas import *

class Fichas(Casillas):
    def __init__(self,c,col,form):
        Casillas.__init__(self,c,"imagenes/"+form+col+".png")
        self.color=col
        self.forma=form
        self.estado=1
        
    def getColor(self):
        return self.color

    def getForma(self):
        return self.forma

class fabricaDeFichas:
    def __init__(self):
        self.bolsa=[]
        self.crearBolsa()

    
    def color(self):
        num=randint(1,6)
        switch={
            1:"Rojo",
            2:"Azul",
            3:"Verde",
            4:"Amarillo",
            5:"Naranja",
            6:"Morado"
        }

        return switch[num]

    def forma(self):
        num=randint(1,6)
        switch={
            1:"estrella",
            2:"cuadro",
            3:"circulo",
            4:"rombo",
            5:"flor",
            6:"equis"
        }

        return switch[num]    

    def crearBolsa(self):
        for i in range (0,108):
            self.bolsa.append(Fichas([0,0],self.color(),self.forma()))

