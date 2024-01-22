from tkinter import *

tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_polygon(10, 10, 10, 60, 50, 35)

def mover_triangulo_derecha(evento):
    canvas.move(1, 5, 0)
    
def mover_triangulo_izquierda(evento):
    canvas.move(1, -5, 0)
    
def mover_triangulo_arriba(evento):
    canvas.move(1, 0, -5)
    
def mover_triangulo_abajo(eventos):
    canvas.move(1, 0, 5)

canvas.bind_all("<KeyPress-Right>", mover_triangulo_derecha)
canvas.bind_all("<KeyPress-Left>", mover_triangulo_izquierda)
canvas.bind_all("<KeyPress-Up>", mover_triangulo_arriba)
canvas.bind_all("<KeyPress-Down>", mover_triangulo_abajo)
