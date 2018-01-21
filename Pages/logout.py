from tkinter import *
from tkinter.ttk import *

class Logout(Frame):
    def __init__(self, parent, controller):
        from Pages.main import MainPage
        from Pages.searchEngine import Search
        Frame.__init__(self, parent)

        Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()
        Button(self, text="Back", command=lambda: controller.show_frame(Search)).pack()

    def run(self):
        pass