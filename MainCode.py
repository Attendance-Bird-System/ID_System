# The main File That will be Run and call the screens 
# Finished File


from tkinter import *
from tkinter import ttk

from pyasn1.type.univ import Null
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
from edit_peson_page import *
from archivedGroup import *
from firebase import fireBase

class Main(Tk):

    def __init__(self, userBefor , *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.Groupname = "Group name"
        self.after(3000, self.StartCode)

        self.frames = {}
        for F in (DashBoardPage, SignInPage, StatisticsPage, ForgetPasswordPage, CreateNewUserPage,
                  Send_Whatsapp_page, GroupPage, WifiConf, AddPersonPage, addGroupPage, editPerson,
                  archivedGroup):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
    
        self.show_frame('DashBoardPage' if userBefor else 'SignInPage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def StartCode(self):
        print("Programme is started")

    def out(self):
        self.ws.quit()
        self.ws.destroy()

    def changesize(self):
        self.resizable(1, 1)
        self.state("zoomed")


    def MinimizeScreen(self):
        self.state('normal')
        self.geometry('1200x700+150+50')
        self.resizable(0, 0)

    def SetGroupName(self, name):
        self.frames['GroupPage'].LG["text"] = name

    def toTaskBar(self):
        self.iconify()
        # self.attributes('-alpha', 0.9)

    def changeWindowSize(self):
        self.geometry('1200x700+150+50')

    def drawcircle(self, canv, x, y, rad):
        canv.create_oval(x - rad, y - rad, x + rad, y + rad, width=0, fill='blue')

    def ShowLoadingScreen(self):
        #self.buttondev['state'] = "disable"
        self.window = Toplevel()
        self.window.title("Loading")
        self.window.geometry('600x400+200+200')
        self.window.resizable(0, 0)
        self.window.iconbitmap('images/birdlogo.ico')
        self.window.attributes('-topmost', True)
        self.window.config(bg='white')


        c = Canvas(self.window, width=400, height=400, )
        c.pack(anchor=CENTER)
        for i in range(90):
            c.delete("all")
            c.create_oval(10, 10, 210, 210, width=10)
            c.create_arc(30, 200, 90, 100, start=0,
                          extent=i, outline="#f11", width=8)



    def CloseLoadingScreen(self):
        self.geometry('1200x700+150+50')



userBefor = False 

# check if there any user Data befor 
try :
    with open("userData.txt" , 'r') as file :
         data = file.read()
         uId = data.split(',')[1]
         userBefor = data.split(',')[0] == "remeber"
         if userBefor :
             fireBase.setuId(uId)
except :
    pass 



app = Main(userBefor)
app.title("Bird System")
app.geometry('1200x700+150+50')    
#app.resizable(0, 0)
app.iconbitmap('images/birdlogo.ico')
app.mainloop()