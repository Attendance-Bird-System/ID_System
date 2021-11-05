from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from tkinter import messagebox

white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color ="#CCFFCC"



class WifiConf(Frame):

    def back(self):
        self.controller.show_frame("DashBoardPage")

    def SendWifiConf(self):
        messagebox.showinfo("Wifi Configuration", "Connecting")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.WifiSsidText = StringVar()
        self.WifiPassText = StringVar()
        self.config(bg='white')
        #   --------------------------------------------------------------------- Fonts
        myFont = font.Font(size=30, weight='bold')
        State_Font = font.Font(size=23, weight='bold')
        normalfont = font.Font(size=14)
        boldedfont = font.Font(size=14, weight='bold')
        Consolas = font.Font(family="Consolas", size=14, weight='bold')
        #   --------------------------------------------------------------------- Frames
        Leftsideframe = Frame(self, bg=background_color)
        upsideframe = Frame(self, bg=background_color)
        Centerframe = Frame(self, bg='white')
        #persondataframe = Frame(self, bg="#5A5C6A")
        tabledataframe = Frame(self, bg="#5A5C6A", relief=FLAT)
        rightframe = Frame(self, bg="white", relief=FLAT)

        global backphoto
        path = "images/backicon.png"
        backphoto = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(upsideframe,  relief=FLAT,  bg=green_color, fg="#7A1481",
                            command=lambda: self.back(), image=backphoto, activebackground="#3F3F3F")
        buttonback.pack(side=LEFT, fill=Y)

        LG = Label(upsideframe, text="WIFI Configuration", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)

        #   --------------------------------------------------------------------
        L1 = Label(Centerframe, text="WIFI Name", font=State_Font, bg='white', fg=green_color)
        L1.pack(side=TOP, anchor="w", expand=1)

        E1 = Entry(Centerframe, relief=FLAT, font=State_Font, fg="#7A1481", textvariable=self.WifiSsidText,
                   highlightbackground=green_color, highlightthickness=1, width=30)
        E1.pack(side=TOP, anchor="e")
        #   --------------------------------------------------------------------

        L2 = Label(Centerframe, text="WIFI Password", font=State_Font, bg='white', fg=green_color)
        L2.pack(side=TOP, anchor="w", expand=1)

        E2 = Entry(Centerframe, relief=FLAT, font=State_Font, fg="#7A1481", textvariable=self.WifiPassText,
                   highlightbackground=green_color, highlightthickness=1, width=30, show="*")
        E2.pack(side=TOP, anchor="e")
        #   --------------------------------------------------------------------

        SendConfButton = Button(Centerframe, text="Connect", relief=FLAT, bg="#3F3F3F", font=normalfont,
                         command=lambda: self.SendWifiConf(), activebackground=green_color, fg=green_color)
        SendConfButton.pack(side=TOP, anchor=CENTER, pady=20, fill=X)
        #   --------------------------------------------------------------------

        L4 = Label(rightframe, text="Note", font=State_Font, bg='white', fg=green_color)
        L4.pack(side=TOP,  anchor="w", pady=20)

        #   --------------------------------------------------------------------

        t = Text(rightframe, width=45, font=Consolas, bg='white', fg=background_color, bd=0, exportselection=0,
                 selectbackground="green")
        x = "Steps : \n" \
            "1) Connect to Esp WIFI With Password: 8888888\n" \
            "2) Insert your network name and password\n" \
            "3) Press Connect Button\n" \
            "# after that Esp Should Connect To network\n" \
            " and back automatically..\n\n" \
            "If this The First Use for Device :\n" \
            "You Should Set Account ID"
        t.insert(INSERT, x)  # Inserting table in text widget
        t.pack(padx=20)
        t.config(state=DISABLED)

        #   --------------------------------------------------------------------
        SetuserButton = Button(Centerframe, text="Set Account ID", relief=FLAT, bg="#3F3F3F", font=normalfont,
                               command=lambda: self.SendWifiConf(), activebackground=green_color, fg=green_color)
        SetuserButton.pack(side=TOP,  pady=20, fill=X)
        #   --------------------------------------------------------------------

        upsideframe.pack(side=TOP, fill=X)
        Centerframe.pack(side=LEFT, anchor=CENTER, expand=1)
        rightframe.pack(side=RIGHT, anchor="e", fill=Y,)









