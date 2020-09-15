import sys, pygame


pygame.init()

#definiendo colores
NEGRO=[0,0,0]
BLANCO=[255,255,255]

size = (1500,1000)

global screen
screen=pygame.display.set_mode(size)

def dibujarTablero():
    for x in range (0,4):
        for y in range (0,4):
            pygame.draw.rect(screen, NEGRO,(x*200,y*200,100,100,))


#loop del juego
while True:
  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #imprime en la consola el botón presionado y su posición en ese momento
            print(u'botón {} presionado en la posición {}'.format(event.button, event.pos))

    
    
    
    screen.fill(BLANCO)

    for x in range (0,8):
        for y in range (0,8):
            pygame.draw.rect(screen, NEGRO,[(x*100,y*100),(100,100,)],1)

   

    #se actualiza
    pygame.display.flip()
    