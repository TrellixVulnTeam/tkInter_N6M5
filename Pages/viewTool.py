from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk, Image

from Logic.mSettings import Settings

from Pages.leases import Lease


class ToolPage(Frame):
    fee = 0
    
    def __init__(self, parent, logic):
        from Pages.main import MainPage
        from Pages.searchEngine import Result
        
        from Logic.tLogic import ToolLogic
        
        self.logic = logic
        self.tool = ToolLogic()
        
        Frame.__init__(self, parent)
        self.logic = logic

        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()
        Button(self, text='Go back!', command=lambda: logic.show_frame(Result)).pack(padx=10, pady=10)
        
        Label(self, text='Tool Details', font=Settings.lFont).pack(padx=10, pady=10)
        Label(self, text='Name:', font=Settings.sFont).pack()
        self.name = Label(self, text='Name:', font=Settings.sFont)
        self.name.pack()
        
        Label(self, text='Description:', font=Settings.sFont).pack()
        self.dscp = Label(self, text='Name:', font=Settings.sFont)
        self.dscp.pack()
        
        Label(self, text='Photos:', font=Settings.sFont).pack()
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        Label(self, text='Price:', font=Settings.sFont).pack()
        self.price = Label(self, text='Name:', font=Settings.sFont)
        self.price.pack()
        Button(self, text='Rent', command=self.rental).pack(padx=10, pady=10)

    def run(self):
        tools = self.tool.searchName(self.logic.sTool)

        tool = tools[0]
        self.fee = tool['price']
        self.name['text'] = tool['name']
        self.price['text'] = tool['price']
        self.logic.sToolId = tool['id']
        self.dscp['text'] = tool['Description']

        for photo in tool['photos']:
            av_file = ImageTk.PhotoImage(Image.open(photo).resize((100, 50), Image.ANTIALIAS))
            avatar = Label(self.frame, image=av_file)
            avatar.image = av_file
            avatar.config(image=av_file)
            avatar.pack()

    def rental(self):
        self.logic.price = self.fee

        self.logic.show_frame(Lease)
