from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import messagebox
import webbrowser

background_color = "#FFFFFF"
green_color = "#b4de22"
mov_color = "#bb7beb"


class SignInPage(Frame):
    def callback(self, url):
        webbrowser.open_new_tab(url)

    def aboutdev(self):
        self.buttondev['state'] = "disable"
        self.window = Toplevel()
        self.window.title("About")
        self.window.geometry('600x400+200+200')
        self.window.resizable(0, 0)
        self.window.iconbitmap('images/birdlogo.ico')
        self.window.attributes('-topmost', True)
        self.window.protocol("WM_DELETE_WINDOW", self.close_top)
        self.window.config(bg='white')
        frame = Frame(self.window, bg='white')

        L1 = Label(frame, text="Ahmed Khaled Ibrahem", font=self.exfont, bg='white', fg="#5A5C6A")
        L2 = Label(frame, text="Abdelmenam Tarek Abdelmenam", font=self.exfont, bg='white', fg="#5A5C6A")

        L3 = Label(self.window, text="Bird System\r V 1.0", font=self.hugeFont, bg='white', fg="#5A5C6A")

        L4 = Label(frame, text="Developers", font=self.exfont, bg='white', fg="#099070")

        ahmedlink = Label(frame, text="LinkedIn Link", font=self.exfont, fg="blue", cursor="hand2", bg='white')
        ahmedlink.bind("<Button-1>", lambda e: self.callback("https://www.linkedin.com/in/ahmed-khaled-037967206"))
        mn3mlink = Label(frame, text="LinkedIn Link", font=self.exfont, fg="blue", cursor="hand2", bg='white')
        mn3mlink.bind("<Button-1>", lambda e: self.callback("https://www.linkedin.com/in/abdelmenam-tarek-abdelmenam-elbahy"))

        L3.pack(anchor=CENTER, expand=1)
        frame.pack(anchor=CENTER, expand=1)
        L4.pack(anchor=CENTER, pady=20)
        L1.pack(anchor=CENTER)
        ahmedlink.pack(anchor=CENTER)
        L2.pack(anchor=CENTER)
        mn3mlink.pack(anchor=CENTER)

    def close_top(self):
        self.buttondev['state'] = "normal"
        self.window.destroy()

    def signin(self):
        if self.pass_text.get() == "2000":
            self.controller.changesize()
            self.controller.show_frame("DashBoardPage")
        else:
            messagebox.showinfo("WrongPassword", "that is a wrong password\n the correct is 2000")

    def signinByEnter(self, event):
        if self.pass_text.get() != "":
            if self.pass_text.get() == "2000":
                self.controller.changesize()
                self.controller.show_frame("DashBoardPage")
            else:
                messagebox.showinfo("WrongPassword", "that is a wrong password\n the correct is 2000")
            self.E2.delete(0, 'end')

    def forget_pass(self):
       self.controller.show_frame("ForgetPasswordPage")

    def create_user(self):
        self.controller.show_frame("CreateNewUserPage")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.user_text = StringVar()
        self.pass_text = StringVar()
        self.rememberbox = IntVar()

        #   ---------------------------------------------------------------------
        m = Canvas(self, width=2000, height=1000, bg="#3F3F3F")
        m.place(x=-90, y=-130)
        #w.create_rectangle(60, 20, 150, 90, outline='red')
        m.create_oval(-10, -40, 1000, 800, fill=background_color, width=0)
        #   ---------------------------------------------------------------------

        global img
        path = "images/birdlogo.png"
        img = ImageTk.PhotoImage(Image.open(path).resize((200, 200), Image.ANTIALIAS))
        panel = Label(self, image=img, width=300, height=300, bg=background_color)
        panel.place(x=430, y=20)
        #   ---------------------------------------------------------------------
        myFont = font.Font(size=20, weight='bold')
        self.hugeFont = font.Font(size=30, weight='bold')
        regFont = font.Font(size=12)
        self.exfont = font.Font(size=12)

        #   ---------------------------------------------------------------------
        L1 = Label(self, text="Email", font=myFont, bg=background_color, fg="#7A1481")
        L1.place(x=430, y=300)
        E1 = Entry(self, relief=FLAT, font=myFont, fg="#7A1481", textvariable=self.user_text,
                   highlightbackground=green_color, highlightthickness=1)
        E1.place(x=430, y=340)
        E1.focus()
        #   ---------------------------------------------------------------------
        L2 = Label(self, text="Password", font=myFont, bg=background_color, fg="#7A1481")
        L2.place(x=430, y=400)
        self.E2 = Entry(self, relief=FLAT, font=myFont, show="*", fg="#7A1481", textvariable=self.pass_text,
                   highlightbackground=green_color, highlightthickness=1)
        self.E2.place(x=430, y=440)

        self.E2.bind('<Return>', self.signinByEnter)

        #   ---------------------------------------------------------------------
        button1 = Button(self, text="Sign In",  relief=FLAT, font=myFont, bg=green_color, fg="#7A1481",
                            command=lambda: self.signin(), activebackground="#7A1481", activeforeground="#A9F261")
        button1.place(x=430, y=500, width=300)
        #   ---------------------------------------------------------------------
        L3 = Label(self, text="Beta Version", font=regFont, bg="#3F3F3F", fg="white")
        L3.place(x=1070, y=650)
        L4 = Label(self, text="By HOMATION", font=regFont, bg="#3F3F3F", fg="white")
        L4.place(x=1070, y=670)

        #   ---------------------------------------------------------------------
        c1 = Checkbutton(self, text='Remember me', variable=self.rememberbox, onvalue=1, offvalue=0, font=regFont, bg=background_color, fg="#7A1481")
        c1.place(x=430, y=570)
        #   ---------------------------------------------------------------------
        button2 = Button(self, text="Forget Password", relief=FLAT, font=regFont, bg=green_color, fg="#3F3F3F",
                         command=lambda: self.forget_pass(), activebackground="#3F3F3F", activeforeground=green_color)
        button2.place(x=1040, y=20, width=140)

        button3 = Button(self, text="Create New User", relief=FLAT, font=regFont, bg=green_color, fg="#3F3F3F",
                         command=lambda: self.create_user(), activebackground="#3F3F3F", activeforeground=green_color)
        button3.place(x=1040, y=60, width=140)

        self.buttondev = Button(self, text="About ?", relief=FLAT, font=regFont, bg=green_color, fg="#3F3F3F",
                                command=lambda: self.aboutdev(), activebackground="#3F3F3F", activeforeground=green_color)
        self.buttondev.place(x=1040, y=100, width=140)


