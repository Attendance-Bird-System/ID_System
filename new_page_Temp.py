# Finished File


from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from scrollframe import *

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color ="#CCFFCC"


class newpage(Frame):

    def back(self):
        self.controller.show_frame("DashBoardPage")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        #   --------------------------------------------------------------------- Fonts
        myFont = font.Font(size=30, weight='bold')
        State_Font = font.Font(size=23, weight='bold')
        normalfont = font.Font(size=14)
        boldedfont = font.Font(size=14, weight='bold')
        Consolas = font.Font(family="Consolas", size=14, weight='bold')
        #   --------------------------------------------------------------------- Frames
        Leftsideframe = Frame(self, bg=background_color)
        upsideframe = Frame(self, bg=background_color)
        persondataframe =VerticalScrolledFrame(self,
        relief=FLAT,
        background="#5A5C6A")
        #persondataframe = Frame(self, bg="#5A5C6A")
        tabledataframe = Frame(self, bg="#5A5C6A", relief=FLAT)
        rightPropframe = Frame(self, bg="#3F3F3F", relief=FLAT)

        global backphoto
        path = "images/backicon.png"
        backphoto = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(upsideframe,  relief=FLAT,  bg=green_color, fg="#7A1481",
                            command=lambda: self.back(), image=backphoto, activebackground="#3F3F3F")
        buttonback.pack(side=LEFT, fill=Y)

        LG = Label(upsideframe, text="head line here", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)

        upsideframe.pack(side=TOP, fill=X)







