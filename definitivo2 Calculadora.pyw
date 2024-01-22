from tkinter import Tk, Button, Label, Entry
import math

global x
x=False
global estado
estado=''
global num1
num1=0

       
        
def crear_botones():

        btn1 = Boton(1, 'red',1, 0)
        btn2 = Boton(2, 'red',1, 1)
        btn3 = Boton(3, 'red',1, 2)
        btn4 = Boton(4, 'red',2, 0)
        btn5 = Boton(5, 'red',2, 1)
        btn6 = Boton(6, 'red',2, 2)
        btn7 = Boton(7, 'red',3, 0)
        btn8 = Boton(8, 'red',3, 1)
        btn9 = Boton(9, 'red',3, 2)

        btn0 = Boton(0, 'orange',4,0, 2)

        btnPunto= Boton('.','pink',4,2)

        

        

       

        

class Boton:

        def __init__(self, num, color, fila, columna, expandir=1):
                self = Button(text=num, background = color, font=('arial',17), command =lambda: escribir(num))
                self.grid(row=fila, column=columna,  columnspan=expandir, sticky='NSEW')

def botones_Func():
        
        btnDiv= Button(text='/', background = 'blue', font=('arial',17), command = dividir)
        btnDiv.grid(row=1, column=3,  columnspan=1, sticky='NSEW')

        btnRes= Button(text='-', background = 'blue', font=('arial',17), command = restar)
        btnRes.grid(row=2, column=3,  columnspan=1, sticky='NSEW')

        btnSuma = Button(text='+', background = 'blue', font=('arial',17), command = sumar)
        btnSuma.grid(row=3, column=3,  columnspan=1, sticky='NSEW')


        btnIgual = Button(text='=', background = 'green', font=('arial',17), command = igual)
        btnIgual.grid(row=4, column=3,  columnspan=1, sticky='NSEW')


def dividir():
        print('dividir',)
        global estado
        estado="dividir"
        
        global num1
        num1=caja1.get()
        
        print(estado, num1)
        caja1.config(state='normal')
        caja1.delete(0, 'end')
        caja1.config(state='readonly')
def restar():
        print('restar',)
        global estado
        estado="restar"
        
        global num1
        num1=caja1.get()
        
        print(estado, num1)
        caja1.config(state='normal')
        caja1.delete(0, 'end')
        caja1.config(state='readonly')
        
def sumar():
        print('sumar',)
        global estado
        estado="sumar"
        
        global num1
        num1=caja1.get()
        
        print(estado, num1)
        caja1.config(state='normal')
        caja1.delete(0, 'end')
        caja1.config(state='readonly')

def igual():
        print('igual', estado)
        
        global num2

        if caja1.get()=='':

                num2=0
        else:
                num2=caja1.get()


        if estado=='sumar':
                
                resultado= float(num1) + float(num2)

        elif estado == 'restar':
        
                resultado= float(num1) - float(num2)

        elif estado == 'dividir':
        
                resultado= float(num1) / float(num2)

        else:
                resultado = 0



        
        print(resultado)
        caja1.config(state='normal')
        caja1.delete(0, 'end')
        caja1.config(state='readonly')

        dec, ent = math.modf(resultado)

        if dec == 0:
                resultado = int (resultado)
                caja1.config(state='normal')
                caja1.insert('end', resultado)
                caja1.config(state='readonly')
        else:
                caja1.config(state='normal')
                caja1.insert('end', '{:,.2f}'.format(resultado))
                caja1.config(state='readonly')

        print('igual', resultado)

        global x

        x=True

        
def escribir(num):
        global x
        if x:
                caja1.delete(0, 'end')
                x=False

        caja1.config(state='normal')
        caja1.insert("end", num)
        caja1.config(state='readonly')
        print(num)
    



        

#crear ventana
ventana1 = Tk()
ventana1.title("MiCalculadora")
ventana1.geometry("320x501+700+250")

ventana1.columnconfigure(0, weight=1)
ventana1.columnconfigure(1, weight=1)
ventana1.columnconfigure(2, weight=1)
ventana1.columnconfigure(3, weight=1)

ventana1.rowconfigure(0, weight=1)
ventana1.rowconfigure(1, weight=1)
ventana1.rowconfigure(2, weight=1)
ventana1.rowconfigure(3, weight=1)
ventana1.rowconfigure(4, weight=1)

#self.resizable(0, 0)

crear_botones()
botones_Func()

caja1 = Entry(font=("arial", 40, "bold"), width=5,justify="right", state='readonly')
caja1.grid(row=0, column=0, columnspan=4, sticky='NSEW')


while True:

        ventana1.bind_all(0, lambda event: escribir(event.char))
        ventana1.bind_all(1, lambda event: escribir(event.char))
        ventana1.bind_all(2, lambda event: escribir(event.char))
        ventana1.bind_all(3, lambda event: escribir(event.char))
        ventana1.bind_all(4, lambda event: escribir(event.char))
        ventana1.bind_all(5, lambda event: escribir(event.char))
        ventana1.bind_all(6, lambda event: escribir(event.char))
        ventana1.bind_all(7, lambda event: escribir(event.char))
        ventana1.bind_all(8, lambda event: escribir(event.char))
        ventana1.bind_all(9, lambda event: escribir(event.char))
        ventana1.bind_all('/', lambda event: dividir())
        ventana1.bind_all('-', lambda event: restar())
        ventana1.bind_all('+', lambda event: sumar())
        ventana1.bind_all('<Return>', lambda event: igual())
        

        
        
    
        ventana1.mainloop()
