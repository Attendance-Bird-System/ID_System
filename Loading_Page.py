from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from scrollframe import *
from itertools import count, cycle

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color ="#CCFFCC"


class Loading_page(Frame):

    def back(self):
        self.controller.show_frame("DashBoardPage")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")

        upsideframe = Frame(self, bg="#EBFFEE", bd=15, relief=FLAT)

        self.lbl = ImageLabel(upsideframe)
        self.lbl.pack(anchor=CENTER)

        self.lbl.load("images/loading.gif")
        upsideframe.pack(expand=1, anchor=CENTER,)


class ImageLabel(Label):

    def load(self, im):

        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()




    def unload(self):
        global image_stop
        path = "images/birdlogo.png"
        image_stop = ImageTk.PhotoImage(Image.open(path).resize((400, 400), Image.ANTIALIAS))
        self.config(image=image_stop)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)






