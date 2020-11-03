from PIL import Image, ImageChops, ImageEnhance, ImageOps
 



img = Image.open('b.png')
img=img.convert("RGBA")

pixeles=img.load()

for i in range(500):
    for j in range(500):
        if(pixeles[i,j]==(0, 0, 204, 255)):
            pixeles[i,j]=(255,255,255,255)

#pixeles[0,0] = (33,150,243)
 
img.save("nueva_imagen.png")