import time
from tkinter import *

tk=Tk()
canvas=Canvas(width=400, height=400)
canvas.pack()

canvas.create_polygon(10, 10, 10, 60, 50, 35)

def mover_triangulo_derecha():
    canvas.move(1, 5, 0)
    
def mover_triangulo_izquierda():
    canvas.move(1, -5, 0)
    
def mover_triangulo_arriba():
    canvas.move(1, 0, -5)
    
def mover_triangulo_abajo():
    canvas.move(1, 0, 5)

btnDerecha = Button(tk, text="derecha", command= mover_triangulo_derecha)
btnDerecha.pack()

btnIzquierda = Button(tk, text="Izquierda", command= mover_triangulo_izquierda)
btnIzquierda.pack()

btnArriba = Button(tk, text="Arriba", command= mover_triangulo_arriba)
btnArriba.pack()

btnAbajo = Button(tk, text="Abajo", command= mover_triangulo_abajo)
btnAbajo.pack()
