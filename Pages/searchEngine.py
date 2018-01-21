from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk
from PIL import Image


class Search(Frame):
    uName = ''
    uDetails = ''
    search = ''

    def __init__(self, parent, logic):
        from Pages.userTools import UserToolsPage
        from Pages.addTool import AddToolPage
        from Pages.payments import PaymentsPage
        from Pages.main import MainPage

        from Logic.mSettings import Settings
        from Logic.uLogic import UserLogic
        from Logic.lLogic import LoginLogic

        Frame.__init__(self, parent)
        self.logic = logic

        avFile = PhotoImage(file='res/uIcon.png')
        self.avatar = Label(self, image=avFile)
        self.avatar.image = avFile
        self.avatar.pack()

        self.uName = Label(self, text='UserName', font=Settings.sFont)
        self.uName.pack()

        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()
        Button(self, text='Tools', command=lambda: logic.show_frame(UserToolsPage)).pack()
        Button(self, text='Payments', command=lambda: logic.show_frame(PaymentsPage)).pack()
        Button(self, text='Add tool', command=lambda: logic.show_frame(AddToolPage)).pack()

        self.sEntry = Entry(self, textvariable=Settings.search)
        self.sEntry.pack(pady=10, padx=10)
        Button(self, text='Search', command=self.search).pack()

    def run(self):
        self.sEntry.config(textvariable='')
        self.sEntry.delete(0, END)
        
        print('test')
        
        if self.logic.session.session:
            details = self.logic.session.uDetails

            self.uName['text'] = details['name']
            photo = Image.open((details['avatar']))
            photo = photo.resize((400, 300), Image.ANTIALIAS)
            avFile = ImageTk.PhotoImage(photo)

            self.avatar.image = avFile
            self.avatar.config(image=avFile)

    def search(self):
        self.logic.sKeyWord = self.sEntry.get()
        self.logic.show_frame(Result)


class Result(Frame):
    def __init__(self, parent, logic):
        from Pages.main import MainPage

        from Logic.tLogic import ToolLogic
        from Logic.rLogic import LeaseLogic
        from Logic.mSettings import Settings

        self.logic = logic
        self.tool = ToolLogic()
        self.lease = LeaseLogic()

        Frame.__init__(self, parent)

        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()
        Button(self, text='Go Back!', command=lambda: logic.show_frame(Search)).pack()

        self.sEntry = Entry(self, textvariable=Settings.search)
        self.sEntry.pack(pady=10, padx=10)
        Button(self, text='Search', command=self.search).pack()

        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.record = Listbox(self, yscrollcommand=scrollBar.set)
        for line in range(100):
            self.record.insert(END, 'Tool number')
        self.record.pack(fill=BOTH)
        scrollBar.config(command=self.record.yview())
        # scrollBar

    def run(self):

        toolName = self.tool.searchName(self.logic.s)
        self.record.delete(0, END)
        self.sEntry.insert(0, self.logic.sKeyWord)

        if toolName:
            for index, toolItem in enumerate(toolName):
                self.record.insert(END, toolItem['name'])
                self.record.bind('<<ListboxSelect>>', self.select)
        else:
            toolType = self.tool.searchType(self.logic.sKeyWord)
            for index, toolItem in enumerate(toolType):
                self.record.insert(END, toolItem['name'])
                self.record.bind('<<ListboxSelect>>', self.select)

    def search(self):
        self.logic.sKeyWord = self.sEntry.get()
        self.logic.show_frame(Result)

    def select(self, evt):
        from Pages.viewTool import ToolPage

        q = evt.widget
        index = int(q.curselection()[0])
        value = q.get(index)
        self.logic.selectedtool = value
        self.logic.show_frame(ToolPage)