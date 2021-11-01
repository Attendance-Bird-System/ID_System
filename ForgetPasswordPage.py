from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import messagebox


background_color = "white"
mov_color = "#bb7beb"

class ForgetPasswordPage(Frame):

    def back(self):
        self.controller.show_frame("SignInPage")

    def sendEmail(self):
        messagebox.showinfo(f"Reset Password Email", f"Sent to {self.email_text.get()}")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.email_text = StringVar()

        #   ---------------------------------------------------------------------
        myFont = font.Font(size=20, weight='bold')
        bigFont = font.Font(size=40, weight='bold')
        regFont = font.Font(size=12)
        #   ---------------------------------------------------------------------
        m = Canvas(self, width=2000, height=1000, bg="#3F3F3F")
        m.place(x=-90, y=-130)
        #w.create_rectangle(60, 20, 150, 90, outline='red')
        m.create_oval(200, -140, 1200, 800, fill=background_color, width=0)

        #   ---------------------------------------------------------------------
        global photo
        path = "images/backicon.png"
        photo = ImageTk.PhotoImage(Image.open(path).resize((60, 60), Image.ANTIALIAS))
        buttonback = Button(self, text="<", relief=FLAT, font=bigFont, bg="#3F3F3F", fg="#7A1481",
                            command=lambda: self.back(), image=photo, activebackground="#3F3F3F")
        buttonback.place(x=30, y=30)
        #   ---------------------------------------------------------------------
        L1 = Label(self, text="Reset Password", font=bigFont, bg=background_color, fg="#7A1481")
        L1.place(x=390, y=70)
        #   ---------------------------------------------------------------------
        L2 = Label(self, text="Email", font=myFont, bg=background_color, fg="#7A1481")
        L2.place(x=300, y=300)
        E1 = Entry(self, relief=FLAT, font=myFont, fg="#7A1481", textvariable=self.email_text,
                   highlightbackground="#b4de22", highlightthickness=1)
        E1.place(x=300, y=340, width=600)
        #   ---------------------------------------------------------------------
        buttonback = Button(self, text="Send", relief=FLAT, font=myFont, bg="#A9F261", fg="#7A1481",
                            command=lambda: self.sendEmail(), activebackground="#7A1481", activeforeground="#A9F261")
        buttonback.place(x=300, y=400,width=600)
        #   ---------------------------------------------------------------------

