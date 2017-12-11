#importing things
from tkinter import *
#import tkinter and like
from pygame import mixer
#import pygame and sound
import meditation as med
#import meditation from meditation.py

#defining, instacnes and class

class MainWindow(Frame):  # class is where all of the instances are kept
    def __init__(self, *args, **kwargs):  # self represents current object, 
# args and kwargs are used to used in functions definitions *args and **kwargs allow you
#to pass a variable number of arguments to a function. What variable means here is that you do not know beforehand how
#many arguments can be passed to your function by the user so in this case you use these two keywords.
        Frame.__init__(self, *args, **kwargs)
        # The __init__ method is roughly what represents a constructor in Python.
        #. the self variable represents the instance of the object itself. Most object-oriented languages pass this as a hidden parameter
        #to the methods defined on an object; Python does not. You have to declare it explicitly.

 #main GUI       
        title = Label(self, text = "Meditation", fg = "blue", font = ("Lucida Calligraphy", 44))
        title.pack()
# the font and size of the text, color of text and the text it self
# self represents current object, 

        self.button1 = Button(self, text = "Beginner: Transcendental Meditation", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Transcendental )
        self.button1.pack()
# the font and size of the text, color of text and the text it self
# self represents current object,

        self.button2 = Button(self, text = "Beginner: Heart Rhythm Meditation", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_HeartRhytm)
        self.button2.pack()
# the font and size of the text, color of text and the text it self
# self represents current object,
        self.button3 = Button(self, text = "Beginner: Mindfulness", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Mindfulness)
        self.button3.pack()
# the font and size of the text, color of text and the text it self
# self represents current object,

        self.button4 = Button(self, text = "Intermediate: Guided Visualization", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_GuidedVisual)
        self.button4.pack()
# the font and size of the text, color of text and the text it self
# self represents current object,

        self.button5 = Button(self, text = "Intermediate: Zen", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Zen)
        self.button5.pack()
# the font and size of the text, color of text and the text it self
# self represents current object,
        self.button6 = Button(self, text = "Advanced: Kundalini", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Kundalini)
        self.button6.pack()
# the font and size of the text, color of text and the text it self
# self represents current object,
        self.buttonend = Button(self, text = "END", font = ("Lucida Calligraphy", 20), width = 50, command = self.end)
        self.buttonend.pack()
    # the font and size of the text, color of text and the text it self
# self represents current object,
    def create_Transcendental(self):
        trans = med.Transcendental()
        SubWindow(trans.title,trans.imageName,trans.about,trans.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file


    def create_HeartRhytm(self):
        heart = med.HeartRhytm()
        SubWindow(heart.title,heart.imageName,heart.about,heart.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file


    def create_Mindfulness(self):
        mind = med.Mindfulness()
        SubWindow(mind.title,mind.imageName,mind.about,mind.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file


    def create_GuidedVisual(self):
        guided = med.GuidedVisual()
        SubWindow(guided.title,guided.imageName,guided.about,guided.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file


    def create_Zen(self):
        zen = med.Zen()
        SubWindow(zen.title,zen.imageName,zen.about, zen.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file


    def create_Kundalini(self):
        Kund = med.Kundalini()
        SubWindow(Kund.title,Kund.imageName,Kund.about,Kund.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file

            
        
    def end(self):
        exit()
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file

       


class SubWindow():
# the class here is used to new type of objects and the instaces 
    
    def __init__(self,title,imageName,about,sound):
 # The __init__ method is roughly what represents a constructor in Python. with the differnt thing from the meditation.py file        

        self.sound = mixer.Sound(sound)# inforation about the different varibles , where to place, values 
        self.tl = Toplevel()
        self.tl.grab_set()        

        self.tl.wm_title(title)
        img = PhotoImage(file = imageName )
        self.label = Label(self.tl, image = img)
        self.label.image = img
        self.label.pack()
        
        
        self.title = Label(self.tl, text = about, fg = "blue", font = ("Arial", 10))
        self.title.pack()
# the font and size of the text, color of text and the text it self

        self.button1 = Button(self.tl, text = "Start Music", font = ("Lucida Calligraphy", 20), width = 50, command = self.play)
        self.button1.pack()
# the font and size of the text, color of text and the text it self

        self.button2 = Button(self.tl, text = "Pause Music", font = ("Lucida Calligraphy", 20), width = 50, command = self.pause)
        self.button2.pack()
# the font and size of the text, color of text and the text it self

        self.button3 = Button(self.tl, text = "Unpause Music", font = ("Lucida Calligraphy", 20), width = 50, command = self.unpause)
        self.button3.pack()
# the font and size of the text, color of text and the text it self

        self.button4 = Button(self.tl, text = "Stop Music", font = ("Lucida Calligraphy", 20), width = 50, command = self.stop)
        self.button4.pack()
# the font and size of the text, color of text and the text it self
# plus button commands
    def play(self):
        self.sound.play()
                        #self defined fuctions in self variables represents the instances

    def pause(self):
        mixer.pause()
                #self defined fuctions in self variables represents the instances
        
    def stop(self):
        mixer.stop()
                #self defined fuctions in self variables represents the instances
        
    def unpause(self):
        mixer.unpause()
                #self defined fuctions in self variables represents the instances
        
      




mixer.init() # everything inside tkinter so can run through tkinter and mixer, pygme, need to close off the import statets at top

root = Tk()
main = MainWindow(root)
main.pack()
root.mainloop()

 





