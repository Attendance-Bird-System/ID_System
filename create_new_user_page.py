from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import messagebox

background_color = "white"


class CreateNewUserPage(Frame):

    def back(self):
        self.controller.show_frame("SignInPage")

    def CreateNewUserButton(self):
        messagebox.showinfo(f"New User", "New User Account Created Successfully")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.FullName_text = StringVar()
        self.email_text = StringVar()
        self.password_text = StringVar()
        self.confirmpassword_text = StringVar()

        #   ---------------------------------------------------------------------
        m = Canvas(self, width=2000, height=1000, bg="#3F3F3F")
        m.place(x=-90, y=-130)
        # w.create_rectangle(60, 20, 150, 90, outline='red')
        m.create_oval(300, -60, 1500, 800, fill=background_color, width=0)

        #   ---------------------------------------------------------------------
        myFont = font.Font(size=20, weight='bold')
        bigFont = font.Font(size=30, weight='bold')
        regFont = font.Font(size=12)
        #   ---------------------------------------------------------------------
        global photo
        path = "images/backicon.png"
        photo = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(self, text="<", relief=FLAT, font=bigFont, bg="#3F3F3F", fg="#7A1481",
                            command=lambda: self.back(), image=photo)
        buttonback.place(x=30, y=30)
        #   ---------------------------------------------------------------------
        L0 = Label(self, text="User Information", font=bigFont, bg=background_color, fg="#7A1481")
        L0.place(x=600, y=30)
        #   ---------------------------------------------------------------------
        L1 = Label(self, text="Full Name", font=myFont, bg=background_color, fg="#7A1481")
        L1.place(x=600, y=100)
        E1 = Entry(self, relief=FLAT, font=myFont, fg="#7A1481", textvariable=self.FullName_text,
        highlightbackground = "#b4de22", highlightthickness = 1)
        E1.place(x=600, y=140, width=500)
        #   ---------------------------------------------------------------------
        L2 = Label(self, text="Email", font=myFont, bg=background_color, fg="#7A1481")
        L2.place(x=600, y=200)
        E2 = Entry(self, relief=FLAT, font=myFont, fg="#7A1481", textvariable=self.email_text,
                   highlightbackground="#b4de22", highlightthickness=1)
        E2.place(x=600, y=240, width=500)
        #   ---------------------------------------------------------------------
        L3 = Label(self, text="Password", font=myFont, bg=background_color, fg="#7A1481")
        L3.place(x=600, y=300)
        E3 = Entry(self, relief=FLAT, font=myFont, fg="#7A1481", textvariable=self.password_text, show="*",
                   highlightbackground="#b4de22", highlightthickness=1)
        E3.place(x=600, y=340, width=500)
        #   ---------------------------------------------------------------------
        L4 = Label(self, text="Confirm Password", font=myFont, bg=background_color, fg="#7A1481")
        L4.place(x=600, y=400)
        E4 = Entry(self, relief=FLAT, font=myFont, fg="#7A1481", textvariable=self.confirmpassword_text, show="*",
                   highlightbackground="#b4de22", highlightthickness=1)
        E4.place(x=600, y=440, width=500)
        #   ---------------------------------------------------------------------
        buttonback = Button(self, text="Create", relief=FLAT, font=myFont, bg="#A9F261", fg="#7A1481",
                            command=lambda: self.CreateNewUserButton(), activebackground="#7A1481", activeforeground="#A9F261")
        buttonback.place(x=600, y=500, width=500)
        #   ---------------------------------------------------------------------



