import globals as g
from tkinter import *
from utils import *
import materials as mat

def createMenu():
   
    g.filebar = Menu(g.menubar)
    g.filebar.add_command(label="Exit", command=exit)

    g.menubar.add_cascade(label="File", menu=g.filebar)
    
    g.toolsbar = Menu(g.menubar)
    g.subdraw = Menu(g.toolsbar)
    g.toolsbar.add_cascade(label="Draw", menu=g.subdraw,underline=0)

    g.toolsbar.add_command(label="Erase", command=selectEraser)
    g.menubar.add_cascade(label="Tools", menu=g.toolsbar)


    g.exportbar = Menu(g.menubar)
    g.exportbar.add_command(label="Export .inp ", command=export)
    g.menubar.add_cascade(label="Export", menu=g.exportbar)


    g.subdraw.add_command(label="IPE240",command=mat.IPE240)
    g.subdraw.add_command(label="IPE500",command=mat.IPE500)


