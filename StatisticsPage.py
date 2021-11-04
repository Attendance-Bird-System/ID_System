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
        massive_Font = font.Font(size=50, weight='bold')
        normalfont = font.Font(size=14)
        boldedfont = font.Font(size=18, weight='bold')
        Consolas = font.Font(family="Consolas", size=14, weight='bold')
        #   --------------------------------------------------------------------- Frames
        Leftsideframe = Frame(self, bg=background_color)
        upsideframe = Frame(self, bg=background_color)
        kpiFrame = VerticalScrolledFrame(self,
        relief=FLAT,
        background="#3F3F3F")

        GroupsGraphsFrame = VerticalScrolledFrame(self,
        relief=FLAT,
        background="white")

        GeneralGraphsFrame = VerticalScrolledFrame(self,
        relief=FLAT,
        background="white")

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
        #   ---------------------------------------------------------------------
        general_LBL = Label(GeneralGraphsFrame, text="General Attendance Graphs", font=myFont, bg='white',
                                 fg="#3F3F3F")
        general_LBL.pack(side=TOP, fill=X, anchor=CENTER, expand=1, padx=5)

        fig = Figure(figsize=(5, 5), dpi=80)
        x = [1, 2, 3, 4, 5, 6, 7]
        y = [30, 25, 13, 4, 44, 20, 17]

        a = fig.add_subplot(111)
        a.plot(x, y, marker="o", label="Total Persons")
        a.set_xlabel("Last 7 Days")
        # a.set_ylabel("Total attendance")
        a.set_title("EME HUB")
        a.legend()
        a.grid()

        canv = FigureCanvasTkAgg(fig, master=GeneralGraphsFrame)
        canv.draw()

        get_widz = canv.get_tk_widget()
        get_widz.pack(side=TOP, expand=1, fill=BOTH)

        lbl_other= Label(GeneralGraphsFrame, text="Other Values\r Here", font=massive_Font, bg="white", fg=green_color)
        lbl_other.pack(side=TOP, )
        #   ---------------------------------------------------------------------

        Group_attend_LBL = Label(GroupsGraphsFrame, text="Groups Attendance Graphs", font=myFont, bg='white', fg="#3F3F3F")
        Group_attend_LBL.pack(side=TOP, fill=X, anchor=CENTER, expand=1, padx=5)

        for i in range(5):
            fig = Figure(figsize=(5, 5), dpi=80)
            x = [1, 2, 3, 4, 5, 6, 7]
            y = [10, 8, 3, 11, 12, 8, 7]

            a = fig.add_subplot(111)
            a.plot(x, y, marker="o", label="Total Attendance")
            a.set_xlabel("Last 7 Days")
            #a.set_ylabel("Total attendance")
            a.set_title("IOT Group")
            a.legend()
            a.grid()

            canv = FigureCanvasTkAgg(fig, master=GroupsGraphsFrame)
            canv.draw()

            get_widz = canv.get_tk_widget()
            get_widz.pack(side=TOP, expand=1, fill=BOTH)

        #   --------------------------------------------------------------------- kpi widgets
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='white', background="#097FC3", lightcolor="#097FC3",
                    darkcolor="#097FC3", troughcolor='white')
        #   ---------------------------------------------------------------------

        KPI_LBL = Label(kpiFrame, text="KPI Values", font=myFont, bg="#3F3F3F", fg="white")
        KPI_LBL.pack(side=TOP, fill=X, anchor=CENTER, expand=1)

        for i in range(10):
            up_frame = Frame(kpiFrame, bg='white')
            down_frame = Frame(kpiFrame, bg='white')
            SizedBox = Frame(kpiFrame, bg="#3F3F3F", height=10)

            SizedBox.pack(fill=X, expand=1)
            lbl_text1 = Label(up_frame, text="Total Students", font=boldedfont, bg='white', fg="#3F3F3F")
            lbl_text1.pack(side=LEFT, pady=5)
            lbl_text3 = Label(up_frame, text="/200", font=normalfont, bg='white', fg=green_color)
            lbl_text3.pack(side=RIGHT)
            lbl_text2 = Label(up_frame, text="185", font=boldedfont, bg='white', fg='#097FC3')
            lbl_text2.pack(side=RIGHT)


            pb1 = ttk.Progressbar(down_frame, style="red.Horizontal.TProgressbar", orient="horizontal",
                            length=300, mode="determinate", maximum=100, value=85)
            pb1.pack(side=LEFT, fill=X, expand=1, padx=5)

            lbl_val1 = Label(down_frame, text="85%", font=boldedfont, bg='white', fg='#097FC3')
            lbl_val1.pack(side=RIGHT, padx=5)

            up_frame.pack(side=TOP, expand=1, fill=X,)
            down_frame.pack(side=TOP, expand=1, fill=X,)
            #   ---------------------------------------------------------------------
            kpiFrame.pack(side=RIGHT, fill=Y)
            GroupsGraphsFrame.pack(side=RIGHT, fill=BOTH, expand=1)
            GeneralGraphsFrame.pack(side=LEFT, fill=BOTH, expand=1)

        lbl_TotalProgress = Label(kpiFrame, text="Total Progress", font=State_Font, bg="#3F3F3F", fg=green_color)
        lbl_TotalProgress.pack(side=TOP, pady=20)
        lbl_TotalProgress = Label(kpiFrame, text="85%", font=massive_Font, bg="#3F3F3F", fg=green_color)
        lbl_TotalProgress.pack(side=TOP, )

