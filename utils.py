import globals as g
from tkinter import *
from tkinter.filedialog import asksaveasfile
import math

def getMouse(event):
    g.mousex = event.x
    g.mousey = event.y
    return (event.x,event.y)

def create_grid(event=None):
    w = g.canvas.winfo_width() # Get current width of canvas
    h = g.canvas.winfo_height() # Get current height of canvas
    g.canvas.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, g.grid_size):
        g.canvas.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, g.grid_size):
        g.canvas.create_line([(0, i), (w, i)], tag='grid_line')

def selected_node(coord):

    #cerca il nodo piu vicino e dammi le coordinate

    x=coord[0]-coord[0]%g.grid_size
    if(coord[0]%g.grid_size>g.grid_size/2):
        x+=g.grid_size

    y=coord[1]-coord[1]%g.grid_size
    if(coord[1]%g.grid_size>g.grid_size/2):
        y+=g.grid_size

    if g.debug:
        print (x,y)
    return (x,y)

def generatePointer(event=None):
    try:
        g.canvas.delete("pointer")
    except:
        pass
    x,y=selected_node((event.x,event.y))
    g.canvas.create_oval(x, y, x, y, width = 10, fill = 'red',tag="pointer")

def createEarth(event=None):
    g.canvas.create_oval(g.x0, g.y0, g.x0, g.y0, width = 20, fill = 'black',tag="zero")

def configuration(event=None):
    create_grid(event)
    createEarth(event)

def relative(coord):
    return (coord[0]-g.x0,-(coord[1]-g.y0))

def absolute(coord):
    return (coord[0]+g.x0,coord[1]+g.y0)

def onMotion(event):
    getMouse(event)
    generatePointer(event)
    try:
        g.canvas.delete("len")
    except:
        pass
    
    if g.selected:
        g.coord1=selected_node(getMouse(event))
        x1,y1=g.coord0
        x2,y2=g.coord1
        l=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
        l=str(round(l/(g.grid_size*2),2))
        g.canvas.create_text(x1+g.grid_size,y1+g.grid_size,text=l,fill="black",font=("Helvetica 12 bold"),tag="len")

def draw(event=None):
    if not g.selected:
        g.coord0=selected_node(getMouse(event))
        x,y=g.coord0
        g.canvas.create_oval(x, y, x, y, width = 15, fill = 'yellow',tag="first")
        g.selected=1
    else:
        g.canvas.delete("first")
        try:
            g.canvas.delete("len")
        except:
            pass
    
        g.coord1=selected_node(getMouse(event))
        x1,y1=g.coord0
        x2,y2=g.coord1
        
        if not (x1==x2 and y1==y2):
            line=g.canvas.create_line(x1,y1,x2,y2,width=4,fill=g.mat[0])
            g.canvas.create_oval(x2, y2, x2, y2, width = 15, fill = 'yellow',tag="{}{}".format(x2,y2))

            g.beams.append((g.coord0,g.coord1,line,g.mat))
        g.selected=0

def delete(event=None):
    coord=selected_node(getMouse(event))
    for i,beam in enumerate(g.beams):
        if beam is not None:
            if (beam[0][0]==coord[0] and beam[0][1]==coord[1]) or (beam[1][0]==coord[0] and beam[1][1]==coord[1]):
                g.canvas.delete(beam[2])
                g.canvas.delete("{}{}".format(beam[0][0],beam[0][1]))
                g.canvas.delete("{}{}".format(beam[1][0],beam[1][1]))
                g.beams[i]=None

def art(event=None):
    g.canvas.delete("temp")

    if g.tool>=1:
        draw(event)
    elif g.tool==0:
        delete(event)

def selectPencil(event=None):
    g.tool=1

def selectEraser(event=None):
    g.tool=0


def genNodes():
    nodes=[]
    for i,beam in enumerate(g.beams):
        if beam is not None:
            flag1=1
            flag2=1
            for node in nodes:
                if (beam[0][0]==node[0] and beam[0][1]==node[1]):
                    flag1=0
                if (beam[1][0]==node[0] and beam[1][1]==node[1]):
                    flag2=0
            if flag1:
                nodes.append((beam[0][0],beam[0][1]))
            if flag2:
                nodes.append((beam[1][0],beam[1][1]))
    return nodes

def lenBeam(beam):
    xsq=(beam[0][0]-beam[1][0])/(g.grid_size*2)
    ysq=(beam[0][1]-beam[1][1])/(g.grid_size*2)
    l=math.sqrt(pow(xsq,2)+pow(ysq,2))
    return l

    

def genInternNodes():
    nodes=[]
    for i,beam in enumerate(g.beams):
        if beam is not None:
            #vediamo se è piu lunga della lunghezza massima
            #sennò dividiamo
            if lenBeam(beam)>beam[3][5]:
                n=math.ceil(lenBeam(beam)/beam[3][5])
                xlen=beam[0][0]-beam[1][0]
                ylen=beam[0][1]-beam[1][1]
                for k in range(1,n):
                    xpos=beam[0][0]-(xlen/n)*(k)
                    ypos=beam[0][1]-(ylen/n)*(k)
                    nodes.append((xpos,ypos))
                g.canvas.delete(beam[2])
                mat=beam[3]
                g.beams[i]=None
                for k in range(n):
                    x1=beam[0][0]-(xlen/n)*(k)
                    y1=beam[0][1]-(ylen/n)*(k)
                    x2=beam[0][0]-(xlen/n)*(k+1)
                    y2=beam[0][1]-(ylen/n)*(k+1)
                    line=g.canvas.create_line(x1,y1,x2,y2,width=4,fill=mat[0])
                    g.beams.append(((x1,y1),(x2,y2),line,mat))
                
    return nodes
                    


def export(event=None):
    internodes=genInternNodes()
    nodes=genNodes()
    for node in nodes:
        x,y=node
        
        g.canvas.create_oval(x, y, x, y, width = 15, fill = 'yellow',tag="temp")
        

    
    nodestr=""
    for i,node in enumerate(nodes):
        nds=relative(node)
        newx=nds[0]/(g.grid_size*2)
        newy=nds[1]/(g.grid_size*2)
        nodestr+="{}    0 0 0    {} {}\n".format(i,newx,newy) 

    beamstr=""
    for i,beam in enumerate(g.beams):
        if beam is not None:
            n1=0
            n2=0
            for j,node in enumerate(nodes):
            
                if (beam[0][0]==node[0] and beam[0][1]==node[1]):
                    n1=j
                if (beam[1][0]==node[0] and beam[1][1]==node[1]):
                    n2=j
            if(n1==0 and n2==0):
                raise EnvironmentError
            phi=beam[3][1]
            E=beam[3][2]
            A=beam[3][3]
            I=beam[3][4]
            m=phi*A
            EA=E*A
            EI=E*I
            beamstr+="{}    {} {}   {} {} {}\n".format(i,n1,n2,m,EA,EI)

    cont= "*NODES\n"+ nodestr +"*ENDNODES\n\n"+"*BEAMS\n"+beamstr+"*ENDBEAMS\n"+"*DAMPING\n0.2  8.0e-5\n"

    f = asksaveasfile(initialfile = 'Untitled.inp',
defaultextension=".inp",filetypes=[("All Files","*.*"),("Inp files","*.inp")])
    f.write(cont)
    f.close()
