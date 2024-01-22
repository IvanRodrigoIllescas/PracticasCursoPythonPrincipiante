from tkinter import *
import random
import time

class Pelota:
    def __init__(self, lienzo, color):
        self.lienzo=lienzo
        self.id = self.lienzo.create_oval(10, 10, 25, 25, fill = color)
        self.lienzo.coords(self.id, 245,100, 260, 115)
        self.x=-2
        self.y=0.5
        self.pos = self.lienzo.coords(self.id)
    def mover(self):
        self.lienzo.move(self.id, self.x, self.y)
        self.pos = self.lienzo.coords(self.id)
        
        if self.pos[1] <=0:
            self.y = self.y * -1

        if self.pos[3] >= 400:
            self.y = self.y * -1

        if self.pos[2] <= 0:
            
            self.tocar_fondo = False
            raqueta1.empezado = False
            print("pierde 1")
            self.ganador = "Azul"
            raqueta2.puntos = raqueta2.puntos + 1
            self.x = -2
            
        if self.pos[0] >= 499:
            
            self.tocar_fondo = False
            raqueta1.empezado = False
            print("pierde 2")
            self.ganador = "Blanco"
            raqueta1.puntos = raqueta1.puntos + 1
            self.x = 2
            

    def rebotar(self):
        if self.pos[1] >= raqueta1.posicion[1] and self.pos[3] <= raqueta1.posicion[3] and self.pos[0] <= raqueta1.posicion[2]:
            if self.x <= 0:
                self.x = self.x * -1 +0.1
                self.cambiar_rebote()

        if self.pos[1] >= raqueta2.posicion[1] and self.pos[3] <= raqueta2.posicion[3] and self.pos[2] >= raqueta2.posicion[0]:
            if self.x >= 0:
                self.x = self.x * -1 -0.1
                self.cambiar_rebote()
            
    def cambiar_rebote(self):
        self.y = random.randrange(-3, 4)
        
        print("angulo", self.y)
        print("velocidad", self.x)
        
        
class Raqueta:
    def __init__(self, lienzo, x1, y1, x2, y2, color):
        self.lienzo = lienzo
        self.id = self.lienzo.create_rectangle(x1, y1, x2, y2, fill = color)
        self.y=0
        self.puntos = 0
        
        
        self.posicion = self.lienzo.coords(self.id)
    def mover_arriba(self, x):
        self.y = -2
                                
    def mover_abajo(self, x):
        self.y = 2
                
    def mover(self):
        
        self.posicion = self.lienzo.coords(self.id)

        if self.posicion[1] <= 0:
            self.y = 2
            self.lienzo.move(self.id, 0, self.y)
            self.y = 0
        elif self.posicion[3] >= 400:
            self.y = -2
            self.lienzo.move(self.id, 0, self.y)
            self.y = 0

        self.lienzo.move(self.id, 0, self.y)
        
    def quieto(self, x):
        self.y = 0

    def empezar(self, event):
        pelota1.lienzo.coords(pelota1.id, 245,100, 260, 115)
        
        lienzo1.itemconfig(texto_ganador, state="hidden")
        self.empezado= True
        pelota1.tocar_fondo = True





        
#creo la ventana con los detalles
ventana1 = Tk()
ventana1.title("MiPong")
ventana1.resizable(0, 0)
ventana1.wm_attributes("-topmost", 1)
lienzo1 = Canvas(ventana1, width=500, height=400, bd=0, highlightthickness=0)
lienzo1.pack()
lienzo1.update()

#creo los objetos
pelota1 = Pelota(lienzo1, "red")
raqueta1 = Raqueta(lienzo1, 10, 185, 20, 215, "white")
raqueta2 = Raqueta(lienzo1, 480, 185, 490, 215, "blue")

raqueta1.empezado = False
pelota1.tocar_fondo = True
ganador = ""
texto_ganador = lienzo1.create_text(250, 250, font=("Barbieri-Book", 34), text=("Gana",ganador), state= "hidden") 
texto_Puntos1 = lienzo1.create_text(100, 200, font=("Barbieri-Book", 34), text=(raqueta1.puntos), state= "normal")
texto_Puntos2 = lienzo1.create_text(400, 200, font=("Barbieri-Book", 34), text=(raqueta2.puntos), state= "normal")

while 1:
    
    #los objetos se mueven siempre
    raqueta1.lienzo.bind_all("<KeyPress-d>", raqueta1.empezar)
    raqueta1.lienzo.bind_all("<KeyPress-D>", raqueta1.empezar)
    if pelota1.tocar_fondo ==True and raqueta1.empezado == True:
        pelota1.mover() 
        raqueta1.mover()
        raqueta2.mover()
    if pelota1.tocar_fondo==False:
        time.sleep(0.3)
        lienzo1.itemconfig(texto_ganador, state="normal", text=("Gana",pelota1.ganador))
        lienzo1.itemconfig(texto_Puntos1, state="normal", text=(raqueta1.puntos))
        lienzo1.itemconfig(texto_Puntos2, state="normal", text=(raqueta2.puntos))
        
    #controles de la raqueta1
    raqueta1.lienzo.bind_all("<KeyPress-w>", raqueta1.mover_arriba)
    raqueta1.lienzo.bind_all("<KeyPress-s>", raqueta1.mover_abajo)

    raqueta1.lienzo.bind_all("<KeyRelease-w>", raqueta1.quieto)
    raqueta1.lienzo.bind_all("<KeyRelease-s>", raqueta1.quieto)    

    #controles de la raqueta2
    raqueta2.lienzo.bind_all("5", raqueta2.mover_arriba)
    raqueta2.lienzo.bind_all("2", raqueta2.mover_abajo)

    raqueta2.lienzo.bind_all("<KeyRelease-5>", raqueta2.quieto)
    raqueta2.lienzo.bind_all("<KeyRelease-2>", raqueta2.quieto)

    #rebotar en la raqueta1
    pelota1.rebotar()

    #actualizo el lienzo para que se vean los cambios   
    lienzo1.update_idletasks()
    lienzo1.update()
    time.sleep(0.01)
    
    
