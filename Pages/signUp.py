from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from shutil import *


class SignUpPage(Frame):
    def __init__(self, parent, logic):
        from Logic.mSettings import Settings
        from Pages.main import MainPage

        Frame.__init__(self, parent)
        self.logic = logic

        Label(self, text='SharedPower', font=Settings.lFont).pack(pady=10, padx=10)
        Label(self, text='Login: ', font=Settings.sFont).pack()
        Label(self, text='Password: ', font=Settings.sFont).pack()
        Label(self, text='Password again: ', font=Settings.sFont).pack()
        Label(self, text='Avatar: ', font=Settings.sFont).pack()
        self.error = Label(self, text='', font=Settings.sFont)

        self.pswd = Entry(self, show='*', textvariable=Settings.nPswd)
        self.login = Entry(self, textvariable=Settings.nLogin)
        self.rPswd = Entry(self, show='*', textvariable=Settings.nPswd)

        self.login.pack()
        self.error.pack()
        self.pswd.pack()
        self.rPswd.pack()

        Button(self, text='Go back', command=lambda: logic.show_frame(MainPage)).pack(padx=10, pady=10)
        Button(self, text='Sign up!', command=self.reg).pack(padx=10, pady=10)

    def reg(self):
        from Pages.main import MainPage
        if self.pswd.get() == self.rPswd.get():
            from Logic.uLogic import UserLogic
            client = UserLogic
            client.userCreate(UserLogic, self.login.get(), self.pswd.get())
            self.logic.show_frame(MainPage)
        else:
            self.error['text'] = 'Enter correct passwords!'

    def openFile(self):
        from Logic.mSettings import Settings
        path = filedialog.askopenfilename(initialdir= '/', title = 'Add file', filetypes=(
            ('jpeg files','*.jpg'),('all files', "*.*")
        ))
        self.avatar = copy2(path, Settings.resPath).replace('\\','/')

    def start(self):
        pass
