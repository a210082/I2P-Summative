import Tkinter


#Load a window for GUI

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

def initialize(self):
    self.grid()
    self.entryVariable = Tkinter.StringVar()

# Adding a self entry box
    self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
    self.entry.grid(column=0,row=0,sticky='EW')
#returning when pressing enter
    self.entry.bind("<Return>", self.OnPressEnter)
#Setting the variable self entry box on start up to display this text
    self.entryVariable.set(u"Enter text here.")

#Adding a button
    button = Tkinter.Button(self,text=u"Enter",
# when button is clicked
    command=self.OnButtonClick)
    button.grid(column=1,row=0)

#Adding a label below the entry box and button - setting a self variable
    self.labelVariable = Tkinter.StringVar()
    label = Tkinter.Label(self,textvariable=self.labelVariable, text=u"Please enter your text above.", anchor="w",fg="white",bg="pink")
    label.grid(column=0,row=1,columnspan=2,sticky='EW')

#Set label to Hello on start up
    self.labelVariable.set(u"Hello.. How are you today?")

# Make the window resizable according to the text typed out by the user
    self.resizable(True,False)

    self.entry.focus_set()
    self.entry.selection_range(0, Tkinter.END)


# When the button/enter is pressed it will display it in the self variable label
    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get()+"..You clicked the button!" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get()+ "..You pressed enter !")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


    if __name__ == "__main__":
        app = simpleapp_tk(None)
        app.title('my application')
        app.mainloop()
