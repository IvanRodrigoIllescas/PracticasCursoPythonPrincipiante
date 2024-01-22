from tkinter import *
from random import*

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

def rectangulo_aleatorio():
    x1 = randrange(500)
    x2 = randrange(500)
    y1 = randrange(500)
    y2 = randrange(500)

    canvas.create_rectangle(x1, x2, y1, y2)

btn = Button(tk, text="Rectangulo aleatorio", command = rectangulo_aleatorio)
btn.pack()
