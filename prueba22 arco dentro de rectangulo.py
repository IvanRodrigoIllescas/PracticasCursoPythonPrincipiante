from tkinter import*
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

canvas.create_arc(100, 10, 200, 80, extent=180, style=PIESLICE, fill="red" , outline="Blue")


canvas.create_arc(300, 200, 100, 150, extent=156, style=PIESLICE)
