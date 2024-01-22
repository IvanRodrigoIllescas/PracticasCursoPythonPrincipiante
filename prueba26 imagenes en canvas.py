from tkinter import*
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

imagen = PhotoImage(file = "C:/Users/ivan/Desktop/foto1.png")

canvas.create_image(200, 200, anchor=NW, image = imagen)

