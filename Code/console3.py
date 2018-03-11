from Tkinter import *
import random 
import time; 
import datetime 


root=Tk()
root.geometry("1350x750+0+0")
root.title("Fast Food Restaurant")

Tops = Frame(root, width = 1350, height =100, bd = 12, relief= "raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial',50,'bold'), text="Fast Food Restaurant")
lblTitle.grid(row=0, column=0)

BottomMainFrame = Frame(root, width = 1350, height=650, bd=12, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width = 450, height= 650, bd= 12, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(BottomMainFrame, width = 450, height= 650, bd = 12, relief="raise")
f2.pack(side=LEFT)

f2TOP = FRAME (f2, width = 450, height= 350, bd = 12, relief="raise")
f2TOP.psvk
f3 = Frame(BottomMainFrame, width = 450, height= 650, bd= 12, relief="raise")
BottomMainFrame.pack(side=RIGHT)

var1=IntVar()inverse kinematiin

root.mainloop()