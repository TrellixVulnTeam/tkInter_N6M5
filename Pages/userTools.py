from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

from Pages.leases import FinishLease
from Pages.main import MainPage
from Pages.searchEngine import Search
from Pages.searchEngine import Result

from Logic.mSettings import Settings
from Logic.tLogic import ToolLogic
from Logic.rLogic import LeaseLogic

class UserToolPage(Frame):
    def __init__(self, parent, logic):
        self.logic = logic
        self.tool = ToolLogic()
        
        Frame.__init__(self, parent)
        
        self.logic = logic

        Button(self, text="Logout", command=lambda: logic.show_frame(MainPage)).pack()
        Button(self, text="Back", command=lambda: logic.show_frame(Result)).pack(pady=10, padx=10)

        Label(self, text="Tool Details: ", font=Settings.lFont).pack(pady=10, padx=10)

        Label(self, text="Name:", font=Settings.sFont).pack()
        self.name = Label(self, text="Name:", font=Settings.sFont)
        self.name.pack()

        Label(self, text="Description:", font=Settings.sFont).pack()
        self.dscp = Label(self, text="Name:", font=Settings.sFont)
        self.dscp.pack()

        Label(self, text="Photos:", font=Settings.sFont).pack()
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        Label(self, text="Price:", font=Settings.sFont).pack()
        self.price = Label(self, text="Name:", font=Settings.sFont)
        self.price.pack()

    def run(self):
        tools = self.tool.searchName(self.logic.sTool)
        tool = tools[0]
        self.name["text"] = tool["name"]
        self.price["text"] = tool["price"]
        self.dscp["text"] = tool["dscp"]

        for photo in tool["photos"]:
            avFile = ImageTk.PhotoImage(Image.open(photo).resize((100, 50), Image.ANTIALIAS))
            avatar = Label(self.frame, image=avFile)
            avatar.image = avFile
            avatar.config(image=avFile)
            avatar.pack()
    
        
class UserToolsPage(Frame):
    sTool = ''
    listTool = []
    listToolToLease = []
    
    def __init__(self, parent, logic):
        self.logic = logic
        self.tool = ToolLogic()
        self.lease = LeaseLogic()
        
        Frame.__init__(self, parent)

        Button(self, text="Logout", command=lambda: self.logic.show_frame(MainPage)).pack()
        Button(self, text="Back", command=lambda: self.logic.show_frame(Search)).pack(pady=10, padx=10)

        self.topic = Label(self, text="Your balance is: £" + str(Settings.mAvail),font=Settings.lFont)
        self.topic.pack(pady=10, padx=10)

        Label(self, text="Leased:", font=Settings.lFont).pack(pady=10, padx=10)

        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.record = Listbox(self, yscrollcommand=scrollBar.set)
        tools = self.tool.getListAll(1514206410.671336)
        for index, itemTool in enumerate(tools):
            self.record.insert(END, itemTool["name"] + str(index))
        self.record.pack(fill=BOTH)
        scrollBar.config(command=self.record.yview())

        Label(self, text="Rented:", font=Settings.lFont).pack(pady=10, padx=10)

        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.rRecord = Listbox(self, yscrollcommand=scrollBar.set)
        for line in range(100):
            self.rRecord.insert(END, "Tool number" + str(line))
        self.rRecord.pack(fill=BOTH)
        scrollBar.config(command=self.rRecord.yview())


    def run(self):
        self.sTool = ""
        if self.logic.session.session:
            tools = self.tool.getListAll(self.logic.session.uDetails["id"])
            self.record.delete(0, END)
            self.topic.config(text="Your balance is: £" + str(self.logic.session.uDetails["balance"]))
            for index, itemTool in enumerate(tools):
                self.record.insert(END, itemTool["name"])
                self.record.bind('<<ListboxSelect>>', self.select)
                self.listTool.append(itemTool)
            leases = self.lease.getLeasesUser(self.logic.session.uDetails["id"])
            self.rRecord.delete(0, END)
            for index, rental in enumerate(leases):
                itemTool = self.tool.searchId(rental["tId"])
                self.rRecord.insert(END, itemTool["name"])
                self.rRecord.bind('<<ListboxSelect>>', self.selectLease)
                self.rRecord.append(rental)

    def select(self, evt):
        q = evt.widget
        index = int(q.curselection()[0])
        value = q.get(index)
        self.logic.sTool = value
        self.logic.sTool = self.listTool[index]["id"]

        self.logic.show_frame(UserToolPage)

    def selectLease(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.logic.selectLease = value
        self.logic.selectLease = self.listToolToLease[index]["id"]
        
        self.logic.show_frame(FinishLease)