import globals as g
from tkinter import *
from tkinter import filedialog as fd
import os


def load():
    #loader will load everything in IPE240 because I did a design mistake
    filetypes = (
        ('FE input', '*.inp'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)
    content=""
    with open(filename,"r") as f:
        content=f.read()
    content= content.split("*NODES")[1]
    content= content.split("*ENDNODES")
    nodestr= content[0]
    content=content[1]
    content=content.split("*BEAMS")[1]
    beamstr=content.split("*ENDBEAMS")[0]
    nodes=[]
    for b in beamstr.split("\n"):
        ct=b.strip().split(" ")
        nodes.append((float(ct[1]),float(ct[2])))
    for b in beamstr.split("\n"):
        ct=b.strip().split(" ")
        nodes=(float(ct[1]),float(ct[2]))
