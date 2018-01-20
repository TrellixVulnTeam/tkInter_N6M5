from tkinter import *
import os
from tkinter import messagebox
from PIL import Image, ImageTk

creds = 'users.txt'
base = 'search.txt'
credss = {}

class register:
    def signUp():
        global windowSignIn
        global entryLogin
        global entryPswd
        # window 1

        # window.destroy makes a window close after opening the other window
        windowLogin.destroy()

        windowSignIn = Tk()  # imports tkInter
        windowSignIn.title('Sign up')  # adds the "sign up" title
        windowSignIn.config(bg="PeachPuff2")  # adds the background color (color of the page)
        windowSignIn.geometry("500x400")  # defines the size of the window

        instruction = Label(windowSignIn, text='Please enter new credidentials\n', bg="PeachPuff2", font="-weight bold")
        instruction.grid(row=0, column=0,
                         sticky=E)  # creates a grid where sticky defines on which side should the content be

        # adding a picture
        img_in2 = Image.open("login.png").resize((128, 128), Image.ANTIALIAS)
        tkimage2 = ImageTk.PhotoImage(img_in2)
        Label(windowSignIn, image=tkimage2, bg="PeachPuff2").grid(row=1,
                                                                  column=1)  # defines the place in the window grid

        labelLogin = Label(windowSignIn, text='New login: ', bg="PeachPuff2")
        labelLogin.grid(row=2, column=0, sticky=N)
        labelPswd = Label(windowSignIn, text='New password: ', bg="PeachPuff2")
        labelPswd.grid(row=3, column=0, sticky=N)

        entryLogin = Entry(windowSignIn)
        entryLogin.grid(row=2, column=1)
        entryPswd = Entry(windowSignIn, show='*')
        entryPswd.grid(row=3, column=1)

        buttonSign = Button(windowSignIn, text='Sign up', command=checks.checkSignUp, bg="PeachPuff3")
        buttonSign.grid(columnspan=2, sticky=N)

        windowSignIn.mainloop()



class checks:
    def checkSignUp():
        with open(creds, 'r') as f:
            for line in f:
                user, pswd = line.strip().split(
                    ':')  # indicates that the password and the log in should be divided by ':'
                credss[user] = pswd

    def checkLogin():
        with open(creds, 'r') as f:
            for line in f:
                user, pswd = line.strip().split(':')
                credss[user] = pswd

        username = entryLoginL.get()
        password = entryPswdL.get()

        if username in credss and credss[username] == password:
            windowLogin.destroy()
            mainWindow()
        else:
            messagebox.showwarning('Error', "Wrong credentials or user doesn't exist")
            windowLogin.mainloop()