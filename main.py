import globals
from tkinter import *
from utils import *
from config import *



globals.app=Tk()
globals.app.geometry("1200x1000")
globals.app.title("Inp_generator")
globals.menubar=Menu(globals.app)
globals.app.config(menu=globals.menubar)

#menubar configuration
createMenu()



#create canvas
globals.canvas=Canvas(globals.app, bg='white')
globals.canvas.pack(anchor='nw', fill='both', expand=1)
globals.canvas.bind('<Motion>', onMotion)
globals.canvas.bind('<Configure>',configuration)
globals.canvas.bind('<Button-1>', art)


globals.app.mainloop()
