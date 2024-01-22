from tkinter import *
tk = Tk()
canvas = Canvas(width=2400, height=400)
canvas.pack()

tx = canvas.create_text(50, 50, fill="red", text="hola que tal", activefill="blue", font="helvetica")

tx = canvas.create_text(650, 200, fill="yellow", text="hola que tal esta usted", activefill="green", font=("courier", 30))
