# send data using whatsap 


from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from scrollframe import *
from tkinter import messagebox
import pywhatkit as kit
import time
import pyautogui as pg



white_color = "#FFFFFF"
background_color = "#4F4171"
green_color = "#09C54E"
com_color ="#CCFFCC"


class Send_Whatsapp_page(Frame):

    def onselect(self, evt):
        w = evt.widget
        b = w.curselection()
        if len(b) > 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            values = [self.listbox.get(idx) for idx in self.listbox.curselection()]
            all = ', '.join(values)
            self.L6["text"] = all

    def back(self):
        self.controller.show_frame("DashBoardPage")

    def changeHugeNumber(self):
        pass

    def checkbuttonchanged(self, v):
        for widgets in self.changableframe.winfo_children():
            widgets.destroy()
        if v == 1:
            L1 = Label(self.changableframe, text="All Members Will Receive Message", font=self.addedFont, bg='white',
                       fg="#7A1481")
            L1.pack(side=BOTTOM, anchor=CENTER, fill=Y, pady=20)
        elif v == 2:
            L1 = Label(self.changableframe, text="Person that attend Last ", font=self.addedFont, bg='white', fg="#7A1481")

            E1 = Entry(self.changableframe, relief=FLAT, font=self.addedFont, fg="#7A1481", textvariable=self.choice,
                       highlightbackground=green_color, highlightthickness=1, width=4)
            L2 = Label(self.changableframe, text=" Times", font=self.addedFont, bg='white', fg="#7A1481")
            L1.pack(side=LEFT, pady=20)
            E1.pack(side=LEFT, pady=20)
            L2.pack(side=LEFT, pady=20)

        elif v == 3:
            L1 = Label(self.changableframe, text="Person that attend Totally ", font=self.addedFont, bg='white',
                       fg="#7A1481")

            E1 = Entry(self.changableframe, relief=FLAT, font=self.addedFont, fg="#7A1481", textvariable=self.choice,
                       highlightbackground=green_color, highlightthickness=1, width=4)
            L2 = Label(self.changableframe, text=" Times", font=self.addedFont, bg='white', fg="#7A1481")
            L1.pack(side=LEFT, pady=20)
            E1.pack(side=LEFT, pady=20)
            L2.pack(side=LEFT, pady=20)
        else:
            L1 = Label(self.changableframe, text="Please Select any  filter", font=self.addedFont, bg='white',
                       fg="#7A1481")
            L1.pack(side=BOTTOM, anchor=CENTER, fill=Y, pady=20)


    def SendMessage(self):
        print(self.Message.get())

        messagebox.showinfo("Whatsapp Sender", "Don't Touch PC While Sending Messages\r "
                                               "This Process Will Take some Time\r"
                                               "Make Sure you whatsapp web is active")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='white')
        self.Message = StringVar()
        self.choice = StringVar()
        self.RB_var = IntVar()

        #   --------------------------------------------------------------------- Fonts
        myFont = font.Font(size=30, weight='bold')
        self.addedFont = font.Font(size=25, weight='bold')
        hugeFont = font.Font(size=70, weight='bold')
        State_Font = font.Font(size=23, weight='bold')
        normalfont = font.Font(size=14)
        boldedfont = font.Font(size=14, weight='bold')
        Consolas = font.Font(family="Consolas", size=14, weight='bold')
        #   --------------------------------------------------------------------- Frames

        upsideframe = Frame(self, bg=background_color)
        Messageframe = Frame(self, bg='white')
        down_frame = Frame(self, bg='white')
        Leftsideframe = Frame(down_frame, bg='white')
        rightsideframe = Frame(down_frame, bg='white')
        centerPROPframe = Frame(down_frame, bg='white')

        filterframe = VerticalScrolledFrame(centerPROPframe,
        relief=FLAT,
        background='white')
        self.changableframe = Frame(filterframe, bg='white')

        #   ---------------------------------------------------------------------

        global backphoto
        path = "images/backicon.png"
        backphoto = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(upsideframe,  relief=FLAT,  bg=green_color, fg="#7A1481",
                            command=lambda: self.back(), image=backphoto, activebackground="#3F3F3F")
        buttonback.pack(side=LEFT, fill=Y)

        LG = Label(upsideframe, text="Send Messages", font=myFont, bg=green_color, fg="#3F3F3F")
        LG.pack(fill=X, ipady=10)
        #   ---------------------------------------------------------------------

        L1 = Label(Messageframe, text="Message Content", font=State_Font, bg='white', fg=green_color)
        L1.pack(side=TOP, anchor="w", expand=1, pady=12)

        E1 = Text(Messageframe, relief=FLAT, font=normalfont, fg="#7A1481",
                   highlightbackground=green_color, highlightthickness=1, width=80, height=10)
        E1.pack(side=TOP, anchor="e")
        #   ---------------------------------------------------------------------

        L2 = Label(rightsideframe, text="23", font=hugeFont, bg='white', fg=green_color)
        L2.pack(side=TOP,  expand=1)

        L3 = Label(rightsideframe, text="Person \n Will \n Receive \n Message", font=myFont, bg='white', fg=background_color)
        L3.pack(side=TOP, expand=1)

        SendCMessagebutton = Button(rightsideframe, text="Send", relief=FLAT, bg="#3F3F3F", font=myFont,
                                command=lambda: self.SendMessage(), activebackground=green_color, fg=green_color)
        SendCMessagebutton.pack(side=BOTTOM, fill=BOTH, expand=1)

        #   ---------------------------------------------------------------------
        L4 = Label(Leftsideframe, text="All Groups", font=State_Font, bg='white',
                   fg=background_color)
        L4.pack(side=TOP, pady=15)
        #   ---------------------------------------------------------------------
        L5 = Label(centerPROPframe, text="Filter", font=State_Font, bg='white',
                   fg=background_color)
        L5.pack(side=TOP, pady=15)
        #   ---------------------------------------------------------------------
        self.listbox = Listbox(Leftsideframe,
                          width=30,
                          bg="#3F3F3F",
                          activestyle='dotbox',
                          font=boldedfont,
                          fg=com_color,
                          relief=FLAT,
                          selectmode=MULTIPLE,
                          xscrollcommand=1,
                          selectbackground='#2E945E',
                          highlightbackground="#3F3F3F"
                          )
        self.listbox.insert(1, " 1) Group 1")
        self.listbox.insert(2, " 2) Group 2")
        self.listbox.insert(3, " 3) Group 3")
        self.listbox.insert(4, " 4) Group 4")
        self.listbox.insert(5, " 5) Group 5")
        self.listbox.insert(6, " 6) Group 6")
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        self.listbox.pack(fill=Y, expand=1)
        #   --------------------------------------------------------------------
        RB_all = Radiobutton(filterframe, command=lambda: self.checkbuttonchanged(1), font=normalfont, fg='#0A6889',
                             text="Send To All Members", bg='white', variable=self.RB_var, value=1,
                             relief=FLAT, )
        RB_all.pack(side=TOP, anchor="w")
        #   --------------------------------------------------------------------
        RB_all = Radiobutton(filterframe, command=lambda: self.checkbuttonchanged(2), font=normalfont, fg='#0A6889',
                             text="last number of attend", bg='white', variable=self.RB_var, value=2,)
        RB_all.pack(side=TOP, anchor="w")

        #   --------------------------------------------------------------------
        RB_all = Radiobutton(filterframe, command=lambda: self.checkbuttonchanged(3), font=normalfont, fg='#0A6889',
                             text="Total attends", bg='white', variable=self.RB_var, value=3, )
        RB_all.pack(side=TOP, anchor="w")

        #   --------------------------------------------------------------------- frame pack

        upsideframe.pack(side=TOP, fill=X)
        Messageframe.pack(side=TOP)
        down_frame.pack(side=TOP, expand=1, fill=BOTH)
        Leftsideframe.pack(side=LEFT, fill=Y)
        rightsideframe.pack(side=RIGHT, fill=Y)
        centerPROPframe.pack(anchor=CENTER, fill=BOTH, expand=1)
        filterframe.pack(anchor=CENTER, fill=BOTH, expand=1)
        self.changableframe.pack(fill=BOTH, expand=1)
        self.checkbuttonchanged(0)
        #   --------------------------------------------------------------------
        L7 = Label(filterframe, text="Selected Groups", font=State_Font, bg='white',
                   fg=background_color)
        L7.pack(side=TOP, pady=15, anchor="w")

        self.L6 = Label(filterframe, text="NO Groups Selected", font=boldedfont, bg='white',
                   fg=background_color)
        self.L6.pack(side=TOP, pady=15, anchor="w")
        #   --------------------------------------------------------------------



# kit.sendwhatmsg_instantly(phone_no="+201229473873", message= "welcome2 from python" , wait_time=20 )


# # import winsound
# # frequency = 2500  # Set Frequency To 2500 Hertz
# # duration = 1000  # Set Duration To 1000 ms == 1 second
# # winsound.Beep(frequency, duration)