from tkinter import *
import random
import tkinter.colorchooser  


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()



def rectangulo_aleatorio(ancho, alto, color_relleno):
    x1= random.randrange(ancho)
    y1= random.randrange(alto)
    x2= random.randrange(x1 + random.randrange(ancho))
    y2 = random.randrange(y1 + random.randrange(alto))
    canvas.create_rectangle(x1, y1, x2, y2, fill=color_relleno)

def btnF():

    c = tkinter.colorchooser.askcolor()
    
    rectangulo_aleatorio(400, 400, c[1])


btn = tkinter.Button(tk, text="Crear rectangulo de color", command=btnF)
btn.pack()
