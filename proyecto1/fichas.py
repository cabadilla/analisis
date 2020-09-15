from Tablero import *

class Fichas:
    def __init__(self,imagen,col,form):
        self.color=col
        self.forma=form
        self.imagen=pygame.image.load(imagen)



class fabricaDeFichas:
    def __init__(self):
        