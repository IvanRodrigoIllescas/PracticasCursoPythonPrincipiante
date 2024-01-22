from tkinter import Tk, Button, Label, Entry
#crear ventana
ventana1= Tk()
ventana1.title("Sumar con cajas de texto")
ventana1.geometry("500x250+700+250")
ventana1.resizable(0, 0)
ventana1.config(cursor="heart", bd=25, relief="sunken")

#crear funciones

def Suma(event=""):
    n1 = caja1.get()
    n2 = caja2.get()

    resultado = float(n1) + float(n2)
    caja3.config(state="normal")
    caja3.delete(0, "end")
    caja3.insert(0, resultado)
    caja3.focus()
    Seleccionar3()
    #caja3.config(state="readonly")

def Seleccionar1(event=""):
    caja1.select_range(0, "end")

def Seleccionar2(event=""):
    caja2.select_range(0, "end")

def Seleccionar3(event=""):
    caja3.select_range(0, "end")

#crear etiquetas
etiqueta1 = Label(ventana1, text="Primer número", bg="yellow")
etiqueta1.place(x=10, y=10, width=100, height=30)

etiqueta2 = Label(ventana1, text="Segundo número", bg="yellow")
etiqueta2.place(x=10, y=50, width=100, height=30)

etiqueta3 = Label(ventana1, text="Resultado", bg="yellow")
etiqueta3.place(x=10, y=120, width=100, height=30)

#crear cajas de texto
caja1 = Entry(ventana1, bg="pink")
caja1.place(x=120, y=10, width=100, height=30)

caja2 = Entry(ventana1, bg="pink")
caja2.place(x=120, y=50, width=100, height=30)
    #caja de resultado
caja3 = Entry(ventana1, bg="pink", state="readonly")
caja3.place(x=120, y=120, width=100, height=30)

caja1.insert(0, 0)
caja2.insert(0, 0)
caja3.insert(0, 0)

#boton de sumar
boton1=Button(text="sumar", command=Suma)
boton1.place(x=230, y=50, width=80, height=30)

while True:

    caja1.bind("<FocusIn>", Seleccionar1)
    caja2.bind("<FocusIn>", Seleccionar2)
    caja3.bind("<FocusIn>", Seleccionar3)

    ventana1.bind_all("<Return>", Suma)
    
    ventana1.mainloop()

