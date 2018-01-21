from tkinter import *
from tkinter.ttk import *

class Success(Frame):
    def __init__(self, parent, logic):
        from Pages.searchEngine import Search
        from Logic.mSettings import Settings

        Frame.__init__(self, parent)

        Label(self, text="Success", foreground="green", font= Settings.sFont).pack(padx=10, pady=10)

        Button(self, text='Go back!', command=lambda: logic.show_frame(Search)).pack()

    def run(self):
        pass