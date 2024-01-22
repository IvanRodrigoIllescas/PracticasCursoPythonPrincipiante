from tkinter import*

def hola():
    print("hola a todos")

tk = Tk()
btn = Button(tk, text="pulsame", command=hola)
btn.pack()
