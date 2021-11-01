from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from scrollframe import *
import io
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color ="#CCFFCC"


class StatisticsPage(Frame):

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

        LG = Label(upsideframe, text="Statistics", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)

        upsideframe.pack(side=TOP, fill=X)


        fig = Figure(figsize=(5, 5), dpi=100)
        x = [1, 2, 3, 4, 5]
        y = ["Debdut", "Sayoni", "Aishwarya", "Ankit", "Brata"]

        a = fig.add_subplot(122)
        a.plot(x, y, marker="o", label="October")
        a.set_xlabel("Marks")
        a.set_ylabel("Students")
        a.set_title("Graph_Tk")
        a.legend()
        a.grid()

        canv = FigureCanvasTkAgg(fig, master=self)
        canv.draw()

        get_widz = canv.get_tk_widget()
        get_widz.pack()



