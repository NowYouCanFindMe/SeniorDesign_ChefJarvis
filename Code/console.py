#from Tkinter import* 
from tkinter import*
import random 
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Chef Jarvis Console")

Tops = Frame(root, width = 8000, height = 700, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1= Frame(root, width = 800, height = 700, bg="powder blue", relief =SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height = 700, bg= "powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)
#============================= Time          =================================
localtime=time.asctime(time.localtime(time.time()))
#============================= Battery Label =================================
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text ="Power Supply", fg="Steel Blue", bd=10, anchor="w")

lblInfo.grid(row=0, column= 3)




#============================= Def Functions ==================================
def btnClick(servoId):
    switcher = {
            0 : "Servo 1",
            1 : "Servo 2",
            2 : "Servo 3",
            3 : "Servo 4",
            4 : "Servo 5",
            5 : "Servo 6",
            
    }
    return switcher.get(argument,"Selected")
## Servo 1
btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", text="OK", command=btnClick(0))
btn1.grid(row=0, column=1)
## Servo 2
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", text="OK", command=btnClick(0))
btn1.grid(row=0, column=1)
## Servo 3
## Servo 4
## Servo 5
## Servo 6


#Console Widget 


root.mainloop()
