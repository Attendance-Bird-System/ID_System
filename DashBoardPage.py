from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from urllib.request import urlopen
import io

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color = "#CCFFCC"



class DashBoardPage(Frame):

    def onselect(self, evt):
        w = evt.widget
        b = w.curselection()
        if len(b) > 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            print('You selected item %d: "%s"' % (index, value))
            self.controller.SetGroupName(value)
            self.controller.show_frame("GroupPage")

    def change(self):
        self.L2["text"] = "abdelmenam"
        self.L3["text"] = "999999999"
        self.L4["text"] = "+20120000000"

    def addGroup(self):
        self.controller.show_frame("addGroupPage")


    def logout(self):
        self.controller.show_frame("SignInPage")
        self.controller.MinimizeScreen()

    def gotostsatisticspage(self):
        self.controller.show_frame("StatisticsPage")

    def archivedGroup(self):
        self.controller.show_frame("archivedGroup")

    def wifiConfButton(self):

        self.controller.show_frame("WifiConf")

    def gotoWhatsApppage(self):
        self.controller.show_frame("Send_Whatsapp_page")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.Card_id = StringVar(value="18010103")
        self.Card_phone = StringVar(value="01288534459")
        self.Card_name = StringVar(value="Ahmed Khaled Ibrahem")
        self.PersonState = StringVar(value="Recorded")
        self.PersonGroup = StringVar(value="Internet of things")
        self.config(bg=white_color)
        #   ---------------------------------------------------------------------

        rightsideframe = Frame(self, bg=background_color)

        dashboardframe = Frame(self, bg=white_color)
        Headlineframe = Frame(dashboardframe, bg="#3F3F3F")
        leftsideframe = Frame(dashboardframe, bg=white_color)
        botomleftframe = Frame(leftsideframe, bg=white_color)
        idcardframe = Frame(leftsideframe, bg=white_color, width=600, height=300)

        #   ---------------------------------------------------------------------
        myFont = font.Font(size=30, weight='bold')
        State_Font = font.Font(size=23, weight='bold')
        normalfont = font.Font(size=14)
        boldedfont = font.Font(size=14, weight='bold')
        #   ---------------------------------------------------------------------
        Lbl = Label(idcardframe, text="Name", font=boldedfont, bg=white_color)
        Lbl.place(x=10, y=20)
        #x=20, y=100
        self.L2 = Label(idcardframe, text=f"{self.Card_name.get()}", font=normalfont, bg=white_color)
        self.L2.place(x=10, y=45)
        #   ---------------------------------------------------------------------
        Lbl = Label(idcardframe, text="ID", font=boldedfont, bg=white_color)
        Lbl.place(x=10, y=80)
        self.L3 = Label(idcardframe, text=f"{self.Card_id.get()}", font=normalfont, bg=white_color)
        self.L3.place(x=10, y=105)
        #   ---------------------------------------------------------------------
        Lbl = Label(idcardframe, text="Group", font=boldedfont, bg=white_color)
        Lbl.place(x=10, y=140)
        self.L4 = Label(idcardframe, text=f"{self.PersonGroup.get()}", font=normalfont, bg=white_color)
        self.L4.place(x=10, y=170)
        #   ---------------------------------------------------------------------
        self.L5 = Label(idcardframe, text=f"{self.PersonState.get()}", font=State_Font, bg=white_color, fg='#C3097F')
        self.L5.place(x=100, y=210)
        #   ---------------------------------------------------------------------
        #url = "https://st4.depositphotos.com/15648834/23779/v/600/depositphotos_237795814-stock-illustration-unknown-person-silhouette-glasses-profile.jpg"
        #global image
        #raw_data = urlopen(url).read()
        #im = Image.open(io.BytesIO(raw_data)).resize((150, 190), Image.ANTIALIAS)
        #image = ImageTk.PhotoImage(im)

        global img
        path = "images/pic.jpg"
        img = ImageTk.PhotoImage(Image.open(path).resize((180, 215), Image.ANTIALIAS))


        label = Label(idcardframe, image=img, bg=white_color)
        label.place(x=300, y=20)
        #   ---------------------------------------------------------------------

        LG = Label(rightsideframe, text="Groups", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)

        Lt = Label(Headlineframe, text="Dashboard", font=myFont, bg="#3F3F3F", fg=green_color)

        listbox = Listbox(rightsideframe,
                          width=17,
                          bg="#3F3F3F",
                          activestyle='dotbox',
                          font=myFont,
                          fg=com_color,
                          relief=FLAT,
                          xscrollcommand=1,
                          selectbackground='#2E945E',
                          highlightbackground="#3F3F3F"
                          )
        listbox.insert(1, " IOT Course (33)")
        listbox.insert(2, " Python Group (23)")
        listbox.insert(3, " PCB Lab (66)")
        listbox.insert(4, " MicroMouse (12)")
        listbox.insert(5, " Marketing (11)")
        listbox.insert(6, " Lab (22)")
        listbox.insert(7, " Visitors (34)")
        listbox.insert(8, " Workers (8)")
        listbox.insert(9, " Other (80)")
        listbox.insert(10, " Fabrication (72)")
        listbox.insert(11, " Lab Group (3)")

        addgroupbutton = Button(rightsideframe, text="Create Group +", relief=FLAT, font=State_Font, bg=green_color, fg="#3F3F3F",
                         command=lambda: self.addGroup(), activebackground="#3F3F3F", activeforeground=green_color)

        archived_Groups_button = Button(rightsideframe, text="Archived", relief=FLAT, font=State_Font, bg=green_color, fg="#3F3F3F",
                         command=lambda: self.archivedGroup(), activebackground="#3F3F3F", activeforeground=green_color)

        global logouticon
        path = "images/logout.png"
        logouticon = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        logoutbutton = Button(Headlineframe, relief=FLAT, bg="#3F3F3F", fg="#7A1481",
                            command=lambda: self.logout(), image=logouticon, activebackground="#3F3F3F")

        Headlineframe.pack(side=TOP, fill=X, ipady=10)
        logoutbutton.pack(side=LEFT)
        Lt.pack(anchor=CENTER, fill=Y, expand=1)
        listbox.pack(fill=Y, expand=1)

        archived_Groups_button.pack(side=BOTTOM, fill=X)
        addgroupbutton.pack(side=BOTTOM, fill=X)

        listbox.bind('<<ListboxSelect>>', self.onselect)
        rightsideframe.pack(side=RIGHT, fill=Y)

        #   ---------------------------------------------------------------------
        global stat_icon
        path = "images/stat_icon.png"
        stat_icon = ImageTk.PhotoImage(Image.open(path).resize((80, 80), Image.ANTIALIAS))
        stat_but = Button(botomleftframe, relief=FLAT, bg="white",
                                image = stat_icon,
                                command=lambda: self.gotostsatisticspage(), activebackground=green_color,)
        stat_but.pack(side=LEFT)

        #   ---------------------------------------------------------------------
        global whatsapp_icon
        path = "images/whatsapp-icon.png"
        whatsapp_icon = ImageTk.PhotoImage(Image.open(path).resize((80, 80), Image.ANTIALIAS))
        whatsapp_but = Button(botomleftframe, relief=FLAT, bg="white",
                          image=whatsapp_icon,
                          command=lambda: self.gotoWhatsApppage(), activebackground=green_color)
        whatsapp_but.pack(side=LEFT)
        #   ---------------------------------------------------------------------
        global wifi_icon
        path = "images/wifiRouterIcon.png"
        wifi_icon = ImageTk.PhotoImage(Image.open(path).resize((80, 80), Image.ANTIALIAS))
        whatsapp_but = Button(botomleftframe, relief=FLAT, bg="white",
                          image=wifi_icon,
                          command=lambda: self.wifiConfButton(), activebackground=green_color)
        whatsapp_but.pack(side=LEFT)
        #   ---------------------------------------------------------------------


        dashboardframe.pack(side=LEFT, fill=BOTH, expand=1)
        leftsideframe.pack(side=LEFT, fill=Y)
        idcardframe.pack(side=TOP)
        botomleftframe.pack(side=BOTTOM, fill=X)





        #   ---------------------------------------------------------------------





