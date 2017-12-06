import Tkinter as tk
from Tkinter import *
from time import time
root = tk.Tk()
timestr = '00:00'

Bug = False

class Stopwatch:
    def __init__(self):

        self.paused = True


        #MAIN VISUAL (HEADINGS, BUTTON, LABELS)
        self.jesus = Label(root,text="WELCOME TO OUR BALANCING BOARD GAME!",font=("System",15,"bold"),fg="steelblue").pack()
        self.christ = Label(root,text="ENTER YOUR NAME:",font=("System",10,"bold"),fg="RoyalBlue4").pack(side=TOP)
        name = StringVar()
        self.ugh = Entry(root,textvariable = name, width = 50,bg = "white").pack(side=TOP)


        self.button = tk.Button(root,text="Done!")
        self.button.pack()


        Label(root,text="To play our game, just balance the board.\n Our timer will start immediately after \nboth ends of the board are off the ground.",font=("System",10,"bold"),fg="RoyalBlue4").pack(side=TOP)

        self.display = tk.Label(root, text='00:00', width=30)
        self.display.pack()


        self.change = Label(root,text="",font=("System",10,"bold"),fg="RoyalBlue4")
        self.change.pack()

        self.change1 = Label(root,text="",font=("System",10,"bold"),fg="RoyalBlue4")
        self.change1.pack()

        self.button2 = Button(root,text="")
        self.button2.pack()

        self.change3 = Label(root,text="",font=("System",10,"bold"),fg="RoyalBlue4")
        self.change3.pack()


        #END OF MAIN VISUAL#


        #BIND KEYS TO FUNCTIONS
        root.bind("<KeyRelease-Left>",self.gamestart)#BINDS THE RELEASE OF LEFT ARROW
        root.bind("<KeyRelease-Right>",self.gamestart)#BINDS THE RELEASE OF RIGHTARROW
        root.bind("<Left>",self.gamestop)
        root.bind("<Right>",self.gamestop)


        root.mainloop()

    #REPEAT ALL OVER AGAIN
    def all_again(self):

        self.change3.config(text="Here's the scoreboard:")
        f = open("score.txt","a+")
        f.write(str(timestr))
        f.write("\n")
        f = open("score.txt","r")

        if f.mode == 'r':#if scoreboard.txt is in 'read' mode
            contents =f.read()
            Label(root,text=contents).pack(side=TOP)#PRINTS SCOREBOARD

        Stopwatch()





    #RUNS THE TIMER
    def run_timer(self):
        global timestr
        if self.paused == False:

            delta = int(time() - self.oldtime)
            timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
            self.display.config(text=timestr)#CHANGES THE TIMER DISPLAY AFTER 1 SECOND
            self.display.after(1000, self.run_timer)#CHANGES THE TIMER DISPLAY AFTER 1 SECOND
        elif self.paused == True:
            if Bug == False:
                return




    #TOGGLE
    #false = game is going
    #true = game is not going
    def gamestart(self,filler):#BUTTON RELEASED
        global Bug
        self.paused = False
        self.change.config(text='Go go go!')#LINE 10
        if timestr != '00:00':
            Bug = True

        self.button.config(text='Stop')
        if Bug == False:#only makes it play when bug is not happening
            self.oldtime = time()
            self.run_timer()




    def gamestop(self,filler):#BUTTON PRESSED
        self.paused = True
        if Bug == True:
            root.unbind("<KeyRelease-Right>")#MAKES GAME UNABLE TO PLAY UNTIL PERSON AGREES TO PLAY AGAIN
            root.unbind("<Right>")#MAKES GAME UNABLE TO PLAY UNTIL PERSON AGREES TO PLAY AGAIN
        self.change.config(text="Woops. You can play again if you want. Your score is:")
        self.change1.config(text=timestr)#TIMESTR = SECONDS PERSON STAYED ALIVE
        self.button2.config(text="Play again")
        self.button2.config(command= self.all_again)
        self.button2.pack()


Stopwatch()
