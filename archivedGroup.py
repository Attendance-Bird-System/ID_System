# send data to google sheet


from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from scrollframe import *
from prettytable import PrettyTable
from tkinter import messagebox

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color ="#CCFFCC"


class archivedGroup(Frame):


    def onselectGroup(self, evt):
        w = evt.widget
        b = w.curselection()
        if len(b) > 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            print('You selected item %d: "%s"' % (index, value))
            #self.controller.SetGroupName(value)
            #self.controller.show_frame("GroupPage")

    def back(self):
        self.controller.show_frame("DashBoardPage")

    def RemoveGroup(self):
         if messagebox.askokcancel("Remove Group", "Do you want to Remove this Group?"):
            pass

    def CreateCSV(self):
        if messagebox.askokcancel("CSV file", "Do you want to Create CSV file?"):
            pass

    def ChangePersonData(self, name):
        self.nameValue["text"] = name.split(')')[1].strip()

    def onselect(self, evt):
        w = evt.widget
        b = w.curselection()
        if len(b) > 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            self.ChangePersonData(value)
            print('You selected item %d: "%s"' % (index, value))

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.personName = StringVar(value=".....")

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
        rightGroupsframe = Frame(self, bg="#3F3F3F", relief=FLAT)

        #   --------------------------------------------------------------------
        LG = Label(rightGroupsframe, text="Groups", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)

        listboxGroups = Listbox(rightGroupsframe,
                          width=17,
                          bg="#3F3F3F",
                          activestyle='dotbox',
                          font=myFont,
                          fg=com_color,
                          relief=FLAT,
                          xscrollcommand=1,
                          selectbackground='#2E945E',
                          highlightbackground=green_color,
                                borderwidth=8, highlightcolor=green_color, highlightthickness=7)

        listboxGroups.insert(1, " IOT Course (33)")
        listboxGroups.insert(2, " Python Group (23)")
        listboxGroups.insert(3, " PCB Lab (66)")
        listboxGroups.insert(4, " MicroMouse (12)")
        listboxGroups.insert(5, " Marketing (11)")
        listboxGroups.insert(6, " Lab (22)")
        listboxGroups.insert(7, " Visitors (34)")
        listboxGroups.insert(8, " Workers (8)")
        listboxGroups.insert(9, " Other (80)")
        listboxGroups.insert(10, " Fabrication (72)")
        listboxGroups.insert(11, " Lab Group (3)")
        listboxGroups.pack(fill=Y, expand=1)
        listboxGroups.bind('<<ListboxSelect>>', self.onselectGroup)
        #   --------------------------------------------------------------------
        lblDateandState = Label(tabledataframe, text="Date and State",
                                           font=normalfont, bg="#3F3F3F", fg=green_color)
        lblDateandState.pack(side=TOP, fill=X, padx=5, pady=4)

        lbltotalnumberofattendance = Label(tabledataframe,
        text="Total Number Of Attendance = 14\r Total Days = 24\r absence percentage = 41.6%",
                                           font=normalfont, bg=green_color, fg="#3F3F3F")
        lbltotalnumberofattendance.pack(side=BOTTOM, fill=X, ipady=5, ipadx=5)
        #   --------------------------------------------------------------------

        t = Text(tabledataframe, width=25, font=Consolas, bg="#5A5C6A", fg="white", bd=0, exportselection=0,
                 selectbackground="green")
        x = PrettyTable()
        x.field_names = ["Date", "State"]

        x.add_row(["Friday-25/6", "Attend"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Friday-25/6", "Attend"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Friday-25/6", "Attend"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Sunday-28/6", "Attend"])
        x.add_row(["Friday-25/6", "Attend"])
        x.add_row(["Sunday-28/6", "X"])
        x.add_row(["Sunday-28/6", "Attend"])


        t.insert(INSERT, x)  # Inserting table in text widget
        t.pack(fill=Y, expand=1)
        t.config(state=DISABLED)

        #   --------------------------------------------------------------------
        lblpersondata = Label(persondataframe, text="Person Data",
                                font=normalfont, bg="#3F3F3F", fg=green_color)
        lblpersondata.pack(side=TOP, fill=X)

        global backphoto
        path = "images/backicon.png"
        backphoto = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(upsideframe,  relief=FLAT,  bg=green_color, fg="#7A1481",
                            command=lambda: self.back(), image=backphoto, activebackground="#3F3F3F")
        buttonback.pack(side=LEFT, fill=Y)
        #   --------------------------------------------------------------------
        self.LG = Label(upsideframe, text="Archived Groups", font=myFont, bg=green_color, fg="#3F3F3F")
        self.LG.pack(side=LEFT, fill=BOTH, expand=1)
        #   --------------------------------------------------------------------
        global csv_icon
        path = "images/csv_icon.png"
        csv_icon = ImageTk.PhotoImage(Image.open(path).resize((80, 80), Image.ANTIALIAS))
        csv_but = Button(upsideframe, relief=FLAT, bg=green_color,
                         image=csv_icon,
                         command=lambda: self.CreateCSV(), activebackground=green_color, )
        #   --------------------------------------------------------------------

        global remove_icon
        path = "images/remove.png"
        remove_icon = ImageTk.PhotoImage(Image.open(path).resize((80, 80), Image.ANTIALIAS))
        remove_but = Button(upsideframe, relief=FLAT, bg=green_color,
                            image=remove_icon,
                            command=lambda: self.RemoveGroup(), activebackground=green_color, )
        csv_but.pack(side=LEFT,)
        remove_but.pack(side=LEFT)

        LblNames = Label(Leftsideframe, text="Names", font=myFont, bg="#3F3F3F", fg=green_color)
        #   --------------------------------------------------------------------- listbox
        listbox = Listbox(Leftsideframe,
                          width=30,
                          bg="#3F3F3F",
                          activestyle='dotbox',
                          font=normalfont,
                          fg=com_color,
                          relief=FLAT,
                          xscrollcommand=1,
                          selectbackground='#2E945E',
                          cursor="target",
                          highlightbackground="#3F3F3F"
                          )
        listbox.insert(1, " 1) ahmed Khaled Ibrahem")
        listbox.insert(2, " 2) Abdelmenam tarek")
        listbox.insert(3, " 3) Essam Eldin")
        listbox.insert(4, " 4) Saleh ahmed")
        listbox.insert(5, " 5) Alber Atia ")
        listbox.insert(6, " 6) ahmed Khaled Ibrahem")
        listbox.insert(7, " 7) Abdelmenam tarek")
        listbox.insert(8, " 8) Essam Eldin")
        listbox.bind('<<ListboxSelect>>', self.onselect)

        #   -------------------------------------------------------------------- person data
        global personimage
        path = "images/pic.jpg"
        personimage = ImageTk.PhotoImage(Image.open(path).resize((170, 200), Image.ANTIALIAS))
        panel = Label(persondataframe, image=personimage, width=250, height=250, bg="#5A5C6A",)
        panel.pack()

        namelbl = Label(persondataframe, text="Name", font=boldedfont, bg="#5A5C6A", fg=green_color)
        namelbl.pack(anchor="w", ipadx=10)
        self.nameValue = Label(persondataframe, text=self.personName.get(), font=boldedfont, bg="#5A5C6A", fg="#2EF577")
        self.nameValue.pack(anchor="w", ipadx=10)

        idlbl = Label(persondataframe, text="ID", font=boldedfont, bg="#5A5C6A", fg=green_color)
        idlbl.pack(anchor="w", ipadx=10)
        idValue = Label(persondataframe, text="18010103", font=boldedfont, bg="#5A5C6A", fg="#2EF577")
        idValue.pack(anchor="w", ipadx=10)

        phonelbl = Label(persondataframe, text="Phone", font=boldedfont, bg="#5A5C6A", fg=green_color)
        phonelbl.pack(anchor="w", ipadx=10)
        phoneValue = Label(persondataframe, text="01288534459", font=boldedfont, bg="#5A5C6A", fg="#2EF577")
        phoneValue.pack(anchor="w", ipadx=10)

        emaillbl = Label(persondataframe, text="Email", font=boldedfont, bg="#5A5C6A", fg=green_color)
        emaillbl.pack(anchor="w", ipadx=10)
        emailValue = Label(persondataframe, text="ahmedkhaledibrahem@gmail.com", font=boldedfont, bg="#5A5C6A",
                           fg="#2EF577")
        emailValue.pack(anchor="w", ipadx=10)

        #   --------------------------------------------------------------------- pack() frames

        upsideframe.pack(side=TOP, fill=X,)
        LblNames.pack(side=TOP, fill=X)
        listbox.pack(fill=Y, expand=1)
        rightGroupsframe.pack(side=LEFT, fill=Y)
        Leftsideframe.pack(side=LEFT, fill=Y)
        persondataframe.pack(side=LEFT, fill=Y,)
        tabledataframe.pack(side=LEFT, fill=Y)
        rightPropframe.pack(side=RIGHT,)




