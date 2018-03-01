from Tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Servo Control")
       
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()


        self.serv_btn1 = Button(master, text="Servo 1", command=self.servo1)
        self.serv_btn1.grid(row=0, column=1)
        self.serv_btn1.pack()

        self.serv_btn2 = Button(master, text="Servo 2", command=self.servo2)
        self.serv_btn2.pack()

        self.serv_btn3 = Button(master, text="Servo 3", command=self.servo3)
        self.serv_btn3.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def servo1(self):
        print("Running Servo 1")
    def servo2(self):
        print("Running Servo 2")
    def servo3(self):
        print("Running Servo 3")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()