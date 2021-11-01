from tkinter import *
from tkinter import ttk
from SigninPage import *
from DashBoardPage import *
from StatisticsPage import *
from ForgetPasswordPage import *
from create_new_user_page import *
from SendMessagePage import *
from GroupPage import *
from wifiConfiguration import *
from addPersonPage import *
from addGroupPage import *


class Main(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.Groupname = "Group name"
        self.frames = {}
        for F in (DashBoardPage, SignInPage, StatisticsPage, ForgetPasswordPage, CreateNewUserPage,
                  Send_Whatsapp_page, GroupPage, WifiConf, AddPersonPage, addGroupPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SignInPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def out(self):
        ws.quit()
        ws.destroy()

    def changesize(self):
        self.resizable(1, 1)
        self.state("zoomed")

    def MinimizeScreen(self):
        self.geometry('1200x700+150+50')
        self.resizable(0, 0)

    def SetGroupName(self, name):
        self.frames['GroupPage'].LG["text"] = name

    def toTaskBar(self):
        self.iconify()
        # self.attributes('-alpha', 0.9)

    def changeWindowSize(self):
        self.geometry('1200x700+150+50')


app = Main()
app.title("Bird System")
app.geometry('1200x700+150+50')
#app.resizable(0, 0)
app.iconbitmap('images/birdlogo.ico')
app.mainloop()


