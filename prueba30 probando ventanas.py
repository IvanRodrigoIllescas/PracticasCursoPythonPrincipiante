from tkinter import *

ventana1 = Tk()
ventana1.geometry("700x500+580+170")
ventana1.config(cursor="heart", relief="sunken", bd=25)

boton1 = Button(text="hola boton")
boton1.pack()
#boton1.place(relx=0.25, rely=0.1, relwidth=0.5, height=30)

txt1=Label(ventana1, text="holamundo")
txt1.pack(before=boton1)
  
