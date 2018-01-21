from tkinter import *
from tkinter.ttk import *

from Logic.tLogic import ToolLogic


class AddToolPage(Frame):
    photos = []

    def __init__(self, parent, logic):
        from Pages.main import MainPage
        from Pages.searchEngine import Search
        from Logic.mSettings import Settings

        Frame.__init__(self, parent)
        self.logic = logic
        
        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()

        # back
        Button(self, text='Back', command=lambda: logic.show_frame(Search)).pack(padx=10, pady=10)

        # topic
        Label(self, text='Add tool', font=Settings.lFont).pack(padx=10, pady=10)

        # DATA
        Label(self, text='Name:', font=Settings.lFont).pack()
        self.name = Entry(self, textvariable=Settings.name)
        self.name.pack()
        Label(self, text='Type:', font=Settings.sFont).pack()
        self.type = Entry(self, textvariable=Settings.type)
        self.type.pack()

        Label(self, text='Condition:', font=Settings.lFont).pack()
        self.cond = Combobox(self)
        self.cond.pack()
        # add pic
        Label(self, text='Photo:', font=Settings.lFont).pack()

        Button(self, text='Browse', command=self.addToolPhoto).pack()
        # add PIC

        Label(self, text='Describe product:', font=Settings.lFont).pack()
        self.dscp = Entry(self, textvariable=Settings.dscp)
        self.dscp.pack()

        Label(self, text='Price in £', font=Settings.lFont).pack()

        Label(self, text='Per day:', font=Settings.sFont).pack()
        self.pDay = Entry(self, textvariable=Settings.pDay)
        self.pDay.pack()

        # DATA
        Button(self, text='Add tool', command=self.addTool).pack(padx=10, pady=10)

    def addTool(self):
        from Pages.succeded import Success
        tool = ToolLogic()
        tool.addTool(
            self.logic.session.uId, self.name.get(), self.pDay.get(), self.type.get(), self.photos, self.cond.get(), self.dscp.get())
        self.logic.show_frame(Success)

    def run(self):
        pass