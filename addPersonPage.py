# send data to google sheet


from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from scrollframe import *

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color = "#CCFFCC"


class AddPersonPage(Frame):

    def onselect(self, evt):
        w = evt.widget
        b = w.curselection()
        if len(b) > 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            self.ChangePersonData(value)
            print('You selected item %d: "%s"' % (index, value))

    def back(self):
        self.controller.show_frame("GroupPage")

    def ChangePersonData(self, data):
        pass

    def SearchFUN(self):
        pass

    def addPerson(self):
        self.controller.show_frame("GroupPage")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.Name_text = StringVar()
        self.ID_text = StringVar()
        self.Email_text = StringVar()
        self.Phone_text = StringVar()
        self.Gender_text = StringVar()
        self.Search_text = StringVar()
        self.link_text = StringVar()

        #   --------------------------------------------------------------------- Fonts
        myFont = font.Font(size=30, weight='bold')
        State_Font = font.Font(size=23, weight='bold')
        normalfont = font.Font(size=14)
        boldedfont = font.Font(size=14, weight='bold')
        Consolas = font.Font(family="Consolas", size=14, weight='bold')
        #   --------------------------------------------------------------------- Frames
        Leftsideframe = Frame(self, bg=background_color)
        upsideframe = Frame(self, bg=background_color)
        persondataframe =VerticalScrolledFrame(Leftsideframe,
        relief=FLAT,
        background=background_color, width=460)
        #persondataframe = Frame(self, bg="#5A5C6A")
        tabledataframe = Frame(self, bg="#5A5C6A", relief=FLAT)
        rightPropframe = Frame(self, bg="#3F3F3F", relief=FLAT)

        global backphoto
        path = "images/backicon.png"
        backphoto = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(upsideframe,  relief=FLAT,  bg=green_color, fg="#7A1481",
                            command=lambda: self.back(), image=backphoto, activebackground="#3F3F3F")
        buttonback.pack(side=LEFT, fill=Y)

        LG = Label(upsideframe, text="Add New Person", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)

        upsideframe.pack(side=TOP, fill=X)
        #   ---------------------------------------------------------------------
        lblSearch = Label(rightPropframe, text="Search in Responses", font=boldedfont, bg="#3F3F3F", fg="white")
        lblSearch.pack(side=TOP, fill=X)
        lblName = Label(rightPropframe, text="Name or Phone", font=boldedfont, bg="#3F3F3F", fg='white')
        lblName.pack(side=TOP, anchor="w", padx=20)
        #   ---------------------------------------------------------------------
        entry_search = Entry(rightPropframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.Search_text,
                   highlightbackground='white', highlightthickness=1, width=40)
        entry_search.pack(side=TOP, anchor=CENTER, padx=20)
        #   ---------------------------------------------------------------------
        addColumnbutton = Button(rightPropframe, text="Search", font=boldedfont, relief=FLAT, bg=green_color,
                                 fg="#3F3F3F", command=lambda: self.SearchFUN(), activebackground="#3F3F3F",
                                 activeforeground=green_color)
        addColumnbutton.pack(side=TOP, fill=X, padx=20, pady=10)
        #   ---------------------------------------------------------------------
        lblResults = Label(rightPropframe, text="Results", font=boldedfont, bg="#3F3F3F", fg='white')
        lblResults.pack(side=TOP, anchor="w", padx=20, pady=20)
        #   ---------------------------------------------------------------------
        resultslistbox = Listbox(rightPropframe, width=30, bg="#3F3F3F",
                                 activestyle='dotbox',
                                 font=normalfont,
                                 fg=com_color,
                                 relief=FLAT,
                                 xscrollcommand=1,
                                 selectbackground='#2E945E',
                                 highlightbackground="#3F3F3F")
        resultslistbox.insert(1, " 1) ahmed Khaled Ibrahem")
        resultslistbox.insert(2, " 2) Abdelmenam tarek")
        resultslistbox.insert(3, " 3) Essam Eldin")
        resultslistbox.insert(4, " 4) Saleh ahmed")
        resultslistbox.insert(5, " 5) Alber Atia ")
        resultslistbox.insert(6, " 6) ahmed Khaled Ibrahem")
        resultslistbox.insert(7, " 7) Abdelmenam tarek")
        resultslistbox.insert(8, " 8) Essam Eldin")
        resultslistbox.bind('<<ListboxSelect>>', self.onselect)
        resultslistbox.pack()

        #   ---------------------------------------------------------------------
        lblresponselink = Label(rightPropframe, text="Response Link", font=boldedfont, bg="#3F3F3F", fg='white')
        lblresponselink.pack(side=TOP, anchor="w", padx=20, pady=20)

        entry_response = Entry(rightPropframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.link_text,
                               highlightbackground='white', highlightthickness=1, width=40)
        entry_response.pack(side=TOP, anchor=CENTER, padx=20)

        self.lblnote = Label(rightPropframe, text="Response Sheet Should be Public", font=boldedfont, bg="#3F3F3F",
                        fg=green_color)
        self.lblnote.pack(side=TOP, anchor="w", padx=20, pady=5)
        #   ---------------------------------------------------------------------
        L1 = Label(Leftsideframe, text="Person Data", font=myFont, bg=background_color, fg="white")
        L1.pack(side=TOP, fill=X)

        #   ---------------------------------------------------------------------
        L2 = Label(persondataframe, text="Name", font=boldedfont, bg=background_color, fg='white')
        L2.pack(side=TOP, anchor="w")
        E2 = Entry(persondataframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.Name_text,
                   highlightbackground='white', highlightthickness=1, width=40)
        E2.pack(side=TOP, anchor=CENTER)
        #   ---------------------------------------------------------------------

        L3 = Label(persondataframe, text="ID", font=boldedfont, bg=background_color, fg='white')
        L3.pack(side=TOP, anchor="w")

        E3 = Entry(persondataframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.ID_text,
                   highlightbackground='white', highlightthickness=1, width=40)
        E3.pack(side=TOP, anchor=CENTER)
        self.L0 = Label(persondataframe, text="Pass The ID Card To Read it", font=boldedfont, bg=background_color,
                   fg=green_color)
        self.L0.pack(side=TOP, anchor="w")
        #   ---------------------------------------------------------------------
        L4 = Label(persondataframe, text="Email", font=boldedfont, bg=background_color, fg='white')
        L4.pack(side=TOP, anchor="w")
        E4 = Entry(persondataframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.Email_text,
                   highlightbackground='white', highlightthickness=1, width=40)
        E4.pack(side=TOP, anchor=CENTER)
        #   ---------------------------------------------------------------------
        L5 = Label(persondataframe, text="Phone", font=boldedfont, bg=background_color, fg='white')
        L5.pack(side=TOP, anchor="w")
        E5 = Entry(persondataframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.Phone_text,
                   highlightbackground='white', highlightthickness=1, width=40)
        E5.pack(side=TOP, anchor=CENTER)
        #   ---------------------------------------------------------------------
        L6 = Label(persondataframe, text="Gender", font=boldedfont, bg=background_color, fg='white')
        L6.pack(side=TOP, anchor="w")
        E6 = Entry(persondataframe, relief=FLAT, font=boldedfont, fg="#7A1481", textvariable=self.Gender_text,
                   highlightbackground='white', highlightthickness=1, width=40)
        E6.pack(side=TOP, anchor=CENTER)
        #   ---------------------------------------------------------------------
        addColumnbutton = Button(Leftsideframe, text="add Person + ", font=boldedfont, relief=FLAT, bg=green_color,
                               fg="#3F3F3F", command=lambda: self.addPerson(), activebackground="#3F3F3F",
                               activeforeground=green_color)
        addColumnbutton.pack(side=BOTTOM, fill=X)

        #   ---------------------------------------------------------------------
        Leftsideframe.pack(side=LEFT, fill=Y, expand=1)
        persondataframe.pack(side=LEFT, fill=Y, expand=1, padx=10)
        rightPropframe.pack(side=RIGHT, fill=Y, expand=1, padx=10)


