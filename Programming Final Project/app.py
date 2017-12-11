from tkinter import *  #import tkinter 

from pygame import mixer # import pygame and music and audio stuff
 
import meditation as med # from the meditation.py  and call it med




class MainWindow(Frame): # class is where all of the instances are kept
    def __init__(self, *args, **kwargs):  # self represents current object, 
# args and kwargs are used to used in functions definitions *args and **kwargs allow you
#to pass a variable number of arguments to a function. What variable means here is that you do not know beforehand how
#many arguments can be passed to your function by the user so in this case you use these two keywords.
        Frame.__init__(self, *args, **kwargs) # The __init__ method is roughly what represents a constructor in Python.
        #. the self variable represents the instance of the object itself. Most object-oriented languages pass this as a hidden parameter
        #to the methods defined on an object; Python does not. You have to declare it explicitly.
        
        title = Label(self, text = "Meditation I2P App.Created by Yuto Lam Sarthak Bajpai and Steven Choi", fg = "blue", font = ("Lucida Calligraphy", 44)) # the font and size of the text, color of text and the text it self
        title.pack()
# self represents current object, 
        title = Label(self, text = "In this app, you will have the chance to choose 6 different types of meditation. After you click on your choice, you will get some information on each type of meditation. Through this screen, you can also play and pause the music. Enjoy!", fg = "blue", font = ("Lucida Calligraphy", 10))
        title.pack()# the font and size of the text, color of text and the text it self
#label to show only text
        self.button1 = Button(self, text = "Beginner: Transcendental Meditation", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Transcendental )#button to show clickable
        self.button1.pack()# the font and size of the text, color of text and the text it self

# pack shows where to put the different buttons and texts
        self.button2 = Button(self, text = "Beginner: Heart Rhythm Meditation", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_HeartRhytm)#button to show clickable
        self.button2.pack()
# the font and size of the text, color of text and the text it self
        self.button3 = Button(self, text = "Beginner: Mindfulness", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Mindfulness)#button to show clickable
        self.button3.pack()# the font and size of the text, color of text and the text it self


        self.button4 = Button(self, text = "Intermediate: Guided Visualization", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_GuidedVisual)#button to show clickable
        self.button4.pack()# the font and size of the text, color of text and the text it self


        self.button5 = Button(self, text = "Intermediate: Zen", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Zen)#button to show clickable
        self.button5.pack()
# the font and size of the text, color of text and the text it self
        self.button6 = Button(self, text = "Advanced: Kundalini", font = ("Lucida Calligraphy", 20), width = 50, command = self.create_Kundalini)#button to show clickable
        self.button6.pack()# the font and size of the text, color of text and the text it self

        self.buttonend = Button(self, text = "END", font = ("Lucida Calligraphy", 20), width = 50, command = self.end)#button to show clickable
        self.buttonend.pack()# the font and size of the text, color of text and the text it self
    
    def create_Transcendental(self):
        trans = med.Transcendental()
        SubWindow(trans.title,trans.imageName,trans.about,trans.sound)

#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file

    def create_HeartRhytm(self):
        trans = med.HeartRhytm()
        SubWindow(trans.title,trans.imageName,trans.about,trans.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file

    def create_Mindfulness(self):
        trans = med.Mindfulness()
        SubWindow(trans.title,trans.imageName,trans.about,trans.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file

    def create_GuidedVisual(self):
        trans = med.GuidedVisual()
        SubWindow(trans.title,trans.imageName,trans.about,trans.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file

    def create_Zen(self):
        trans = med.Zen()
        SubWindow(trans.title,trans.imageName,trans.about,trans.sound)
#create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file

    def create_Kundalini(self):
        trans = med.Kundalini()
        SubWindow(trans.title,trans.imageName,trans.about,trans.sound)
            
        #create the tasncendental self vairables for oop which will then use the med to import the trsncendental information from the trasncendental definition in the meditation.py file
# the sub window shows the things that will be defined a give na value to in the meditation.py file
    def end(self):
        exit()
        # when end is pressed, then exit
       


class SubWindow():  # the class here is used to new type of objects and the instaces 
    
    def __init__(self,title,imageName,about,sound):    # The __init__ method is roughly what represents a constructor in Python. with the differnt thing from the meditation.py file
        

        self.sound = mixer.Sound(sound) # inforation about the different varibles 
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

      




mixer.init()

root = Tk()
main = MainWindow(root)
main.pack()
root.mainloop()

 





