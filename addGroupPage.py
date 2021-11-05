from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from scrollframe import *

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color = "#CCFFCC"



class addGroupPage(Frame):

    def addGroup(self):
        self.controller.show_frame("DashBoardPage")

    def addProp(self):
        addedentry = Entry(self.groupdataframe, relief=FLAT, font=self.exteralfont, fg="#7A1481",
                           textvariable=StringVar(),
                         highlightbackground=green_color, highlightthickness=1, width=50)
        addedentry.pack(side=TOP, anchor=CENTER, padx=20, pady=10)

    def CreateGroup(self):
        self.controller.show_frame("DashBoardPage")

    def back(self):
        self.controller.show_frame("DashBoardPage")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.GroupName_text = StringVar()
        self.name_text = StringVar(value="Name")
        self.ID_text = StringVar(value="ID")
        self.config(bg="#3F3F3F")

        #   --------------------------------------------------------------------- Fonts
        myFont = font.Font(size=30, weight='bold')
        State_Font = font.Font(size=23, weight='bold')
        huge_Font = font.Font(size=30, weight='bold')
        normalfont = font.Font(size=14)
        boldedfont = font.Font(size=14, weight='bold')
        self.exteralfont = font.Font(size=14, weight='bold')
        Consolas = font.Font(family="Consolas", size=14, weight='bold')
        #   --------------------------------------------------------------------- Frames
        nameframe = Frame(self, bg='white')
        tempcenterframe = Frame(nameframe, bg='white')
        upsideframe = Frame(self, bg=background_color)
        Centerframe = Frame(self, bg='white')
        self.groupdataframe = VerticalScrolledFrame(Centerframe,
        relief=FLAT,
        background="white", width=600,)
        #persondataframe = Frame(self, bg="#5A5C6A")
        tabledataframe = Frame(self, bg="#5A5C6A", relief=FLAT)
        rightPropframe = Frame(self, bg="#3F3F3F", relief=FLAT)

        global backphoto
        path = "images/backicon.png"
        backphoto = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(upsideframe,  relief=FLAT,  bg=green_color, fg="#7A1481",
                            command=lambda: self.back(), image=backphoto, activebackground="#3F3F3F")
        buttonback.pack(side=LEFT, fill=Y)

        LG = Label(upsideframe, text="Create New Group", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)

        #   ---------------------------------------------------------------------

        L1 = Label(tempcenterframe, text="Group Name", font=boldedfont, bg="white", fg=green_color)
        L1.pack(side=LEFT,)
        E1 = Entry(tempcenterframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.GroupName_text,
                   highlightbackground=green_color, highlightthickness=1, width=40)
        E1.pack(side=LEFT,)
        createquikbutton = Button(tempcenterframe, text="Create Quick Group", font=boldedfont, relief=FLAT, bg='white',
                                 fg=background_color, command=lambda: self.addGroup(), activebackground="#3F3F3F",
                                 activeforeground=green_color)
        createquikbutton.pack(side=LEFT, anchor=CENTER)

        #   ---------------------------------------------------------------------
        createGroupbutton = Button(Centerframe, text="Create New Group", font=boldedfont, relief=FLAT, bg='white',
                                  fg=background_color, command=lambda: self.CreateGroup(), activebackground="#3F3F3F",
                                  activeforeground=green_color)
        createGroupbutton.pack(side=BOTTOM, fill=X)
        #   ---------------------------------------------------------------------
        lblColumns = Label(Centerframe, text="Inside Columns", font=boldedfont, bg="white", fg=green_color)
        lblColumns.pack(side=TOP, anchor=CENTER, padx=10)
        #   ---------------------------------------------------------------------
        entry_name = Entry(self.groupdataframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.name_text,
                             highlightbackground=green_color, highlightthickness=1, width=50, state=DISABLED)
        entry_name.pack(side=TOP, anchor=CENTER, padx=20, pady=10)
        #   ---------------------------------------------------------------------
        entry_ID = Entry(self.groupdataframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.ID_text,
                           highlightbackground=green_color, highlightthickness=1, width=50, state=DISABLED)
        entry_ID.pack(side=TOP, anchor=CENTER, padx=20, pady=10)
        #   ---------------------------------------------------------------------
        addPROPbutton = Button(Centerframe, text="+", font=huge_Font, relief=FLAT, bg='white',
                                   fg=background_color, command=lambda: self.addProp(), activebackground="#3F3F3F",
                                   activeforeground=green_color, width=22)

        #   ---------------------------------------------------------------------
        upsideframe.pack(side=TOP, fill=X)
        tempcenterframe.pack(side=TOP, anchor=CENTER)
        nameframe.pack(side=TOP, fill=X,)
        Centerframe.pack(side=TOP, fill=BOTH, expand=1)
        self.groupdataframe.pack(side=TOP, fill=Y, expand=1)
        addPROPbutton.pack(side=TOP)













