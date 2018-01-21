from tkinter import *
from tkinter.ttk import *

from Pages.leases import FinishLease
from Pages.leases import Lease
from Pages.payments import PaymentPage
from Pages.payments import PaymentsPage
from Pages.main import MainPage
from Pages.addTool import AddToolPage
from Pages.signUp import SignUpPage
from Pages.userTools import UserToolPage
from Pages.userTools import UserToolsPage
from Pages.viewTool import ToolPage
from Pages.searchEngine import Result
from Pages.searchEngine import Search
from Pages.succeded import Success

from Pages.logout import Logout
from Logic.lLogic import LoginLogic

class Main(Tk):
    session = LoginController()
    searchkeyword = ""
    selectedtool = ""
    selectedinvoice = ""
    selectedinvoiceid = 0
    selectedtoolid = 0
    selectrental = 0
    selectedrelinvoiceid = 0
    price = 0

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # title of the pages
        self.title("Shared Power")
        self.iconbitmap("res/favicon.ico")

        # store pages
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # list of pages
        for F in (
                MainPage, SignUpPage, Search, Result, AddToolPage, UserToolsPage, UserToolPage,  Logout, Success, Lease,
                FinishLease, ToolPage, PaymentPage, PaymentsPage):
            f = F(container, self)
            self.frames[F] = f
            f.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    def show_frame(self, count):
        f = self.frames[count]
        f.run()
        f.tkraise()


if __name__ == "__main__":
    app = Main()
    app.mainloop()