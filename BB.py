timestr = '00:00'
import Tkinter as tk
from Tkinter import *
from time import time
bb = tk.Tk()


BALANCE = False

class Stopwatch:
    def __init__(self):

        self.paused = True


        # Graphical User Interface Code
        self.introduction = Label(bb,text="Welcome to balance board game. "
                                          "This code, along with a makey makey will help you record the time "
                                          "you can stay balanced on a balance board. Good luck.").pack()
        self.name = Label(bb,text="Name:").pack()
        name = StringVar()
        self.ugh = Entry(bb,textvariable = name,).pack()


        self.button = tk.Button(bb,text="Enter")
        self.button.pack()


        Label(bb,text="When you start balancing, time will count up").pack()

        self.display = tk.Label(bb, text='00:00', width=10)
        self.display.pack()


        self.Indent = Label(bb,text="",)
        self.Indent.pack()







        #END OF MAIN VISUAL#


        #BIND KEYS TO FUNCTIONS
        bb.bind("<KeyRelease-Left>",self.starttimer)#BINDS THE RELEASE OF LEFT ARROW
        bb.bind("<KeyRelease-Right>",self.starttimer)#BINDS THE RELEASE OF RIGHTARROW
        bb.bind("<Left>",self.stoptimer)
        bb.bind("<Right>",self.stoptimer)


        bb.mainloop()

    #Textfile part
    def text_file(self):


        Balancetxt = open("scoreBaBo.txt","a+")
        Balancetxt.write(str(timestr))
        Balancetxt.write("\n")




        Stopwatch()





    #RUNS THE TIMER
    def run_timer(self):
        global timestr
        if self.paused == False:

            delta = int(time() - self.oldtime)
            timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
            self.display.config(text=timestr)
            self.display.after(1000, self.run_timer)
        elif self.paused == True:
            if BALANCE == False:
                return




    #TOGGLE
    #false = game is going
    #true = game is not going
    def starttimer(self,filler):
        global BALANCE
        self.paused = False
        self.Indent.config(text='Balance')
        if timestr != '00:00':
            BALANCE = True

        self.button.config(text='Stop')
        if BALANCE == False:
            self.oldtime = time()
            self.run_timer()




    def stoptimer(self,filler):#BUTTON PRESSED
        self.paused = True
        if BALANCE == True:

            bb.unbind("<Right>")
            bb.unbind("Left")
            self.ending = Label(bb,text="Thank you for playing. Your score is has been recorded in the scoreBaBo.txt file. Thank you!").pack()



Stopwatch()
