from tkinter import *
from tkinter.ttk import *


class MainPage(Frame):
    def __init__(self, parent, logic):
        self.logic = logic

        from Logic.mSettings import Settings
        from Pages.signUp import SignUpPage

        Frame.__init__(self, parent)

        logo = PhotoImage(file="res/sharedtool.png")
        label = Label(self, image=logo)
        label.image = logo
        label.pack()

        Label(self, text="SharedPower", font=Settings.lFont).pack(padx=10, pady=10)
        Label(self, text="Login:", font=Settings.lFont).pack(padx=10, pady=10)
        Label(self, text="Password:", font=Settings.lFont).pack(padx=10, pady=10)
        self.error = Label(self, text="", font=Settings.sFont)

        self.login = Entry(self, textvariable=Settings.login)
        self.password = Entry(self, show="*", textvariable=Settings.pswd)
        Button(self, text="Sign up", command=lambda: logic.show_frame(SignUpPage)).pack(padx=10, pady=10)

        self.login.pack()
        self.password.pack()
        self.error.pack()

        Button(self, text="Sign in", command=self.signIn).pack(padx=10, pady=10)

    def signIn(self):
        from Pages.searchEngine import Search

        if self.logic.session.session :
            self.logic.session.logout()

        self.logic.session.login(self.login.get(), self.pswd.get())

