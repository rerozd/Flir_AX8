from PIL import Image
import os, sys

path = "/home/renvt/thermal_images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((640,480), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', 'PNG', quality=100)

resize()
