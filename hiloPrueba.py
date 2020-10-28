import threading
def im1():
    i=0
    while i<10:
        print('hola1')
        i+=1

def im2():
    i=0
    while i<10:
        print('hola2')
        i+=1
    
t=threading.Thread(target=im1)
t.start()

t=threading.Thread(target=im2)
t.start()

print('ya estoy aqui')