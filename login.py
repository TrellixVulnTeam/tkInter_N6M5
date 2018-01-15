from tkinter import *
import os
from tkinter import messagebox
from PIL import Image, ImageTk
#imports tkInter library

#.txt files are bases for all the users and equipment added
creds = 'users.txt'
base = 'search.txt'
credss = {}

#defines what is needed in order to sign up
def signUp():
    global windowSignIn
    global entryLogin
    global entryPswd
#window 1

#window.destroy makes a window close after opening the other window
    windowLogin.destroy()

    windowSignIn = Tk()#imports tkInter
    windowSignIn.title('Sign up')#adds the "sign up" title
    windowSignIn.config(bg="PeachPuff2")#adds the background color
    windowSignIn.geometry("250x400")#defines the size of the window

    instruction = Label(windowSignIn, text='Please enter new credidentials\n', bg="PeachPuff2")
    instruction.grid(row=0, column=0, sticky=E)#creates a grid where sticky defines on which side should the content be

    labelLogin = Label(windowSignIn, text='New login: ', bg="PeachPuff2")
    labelLogin.grid(row=1, column=0, sticky=W)
    labelPswd = Label(windowSignIn, text='New password: ', bg="PeachPuff2")
    labelPswd.grid(row=2, column=0, sticky=W)

    entryLogin = Entry(windowSignIn)
    entryLogin.grid(row=1, column=1)
    entryPswd = Entry(windowSignIn, show='*')
    entryPswd.grid(row=2, column=1)

    buttonSign = Button(windowSignIn, text='Sign up', command=bSignup, bg="PeachPuff3")
    buttonSign.grid(columnspan=2, sticky=W)

    windowSignIn.mainloop()


def bSignup():
    with open(creds, 'r') as f:
        for line in f:
            user, pswd = line.strip().split(':')#indicates that the password and the log in should be divided by ':'
            credss[user] = pswd

    checkUsr = entryLogin.get()
    checkPswd = entryPswd.get()
    if checkUsr == '' and checkPswd == '':
        messagebox.showwarning('Error', 'Enter credentials!')
    elif checkPswd == '' and checkUsr != '':
        messagebox.showwarning('Error', 'Enter password!')
    elif checkUsr == '' and checkPswd != '':
        messagebox.showwarning('Error', 'Enter username!')
    else:
        if any(s in line for s in checkUsr):
            messagebox.showwarning('Error', 'User exists already!')
        else:
            with open(creds, 'a') as f:
                f.write(entryLogin.get())
                f.write(':')
                f.write(entryPswd.get())
                f.write('\n')
                f.close()

            messagebox.showwarning('Success!', 'User registered successfully!')
            windowSignIn.destroy()
            logIn()


# window 1 close
def logIn():
    global entryLoginL
    global entryPswdL
    global windowLogin
#window 2
    windowLogin = Tk()
    windowLogin.title('Login')
    windowLogin.config(bg="PeachPuff2")
    windowLogin.geometry("250x400")


    img_in = Image.open("sharedtool.png").resize((128,128), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img_in)
    Label(windowLogin, image=tkimage, bg="PeachPuff2").grid(row=0, column=1)

    instruction = Label(windowLogin, text='Log in!\n', bg="PeachPuff2", font="-weight bold")
    instruction.grid(row=1, column=1)
    labelLoginL = Label(windowLogin, text='Login: ', bg="PeachPuff2")
    labelLoginL.grid(row=2, sticky=W)
    labelPswdL = Label(windowLogin, text='Password: ', bg="PeachPuff2")
    labelPswdL.grid(row=3, sticky=W)

    entryLoginL = Entry(windowLogin)
    entryLoginL.grid(row=2, column=1)
    entryPswdL = Entry(windowLogin, show='*')
    entryPswdL.grid(row=3, column=1)

    buttonLog = Button(windowLogin, text='Login', command=checkLogin, bg="PeachPuff3")
    buttonReg = Button(windowLogin, text='Register', command=signUp, bg="PeachPuff3")
    buttonLog.grid(columnspan=2, sticky=W)
    buttonReg.grid(columnspan=2, sticky=W)

    windowLogin.mainloop()


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
#window 2 close


def mainWindow():
    global windowLogged
#window 3
    windowLogged = Tk()
    windowLogged.title('Search Engine')
    windowLogged.config(bg="PeachPuff2")
    windowLogged.geometry("250x400")

    sEngineB = Button(windowLogged, text="Search", command=searchEngine, bg="PeachPuff3")
    sAddB = Button(windowLogged, text='Add', command=winAddTool, bg="PeachPuff3")
    logOutB = Button(windowLogged, text="Logout", command=logOut, bg="PeachPuff3")

    sEngineB.place(relx=0.5, rely=0.1, anchor=CENTER)
    sAddB.place(relx=0.5, rely=0.2, anchor=CENTER)
    logOutB.place(relx=0.5, rely=0.3, anchor=CENTER)
    windowLogged.mainloop()


def searchEngine():
    #window 4
    windowSearch = Tk()
    windowSearch.title('Tools')
    windowSearch.config(bg="PeachPuff2")
    windowSearch.geometry("400x400")
    i = 2

    gName = Label(windowSearch, text='Name', font='bold', bg="PeachPuff2")
    gDay = Label(windowSearch, text='Per Day', font='bold', bg="PeachPuff2")
    gHDay = Label(windowSearch, text='Half of Day', font='bold', bg="PeachPuff2")
    gIsAvail = Label(windowSearch, text='Is Available', font='bold', bg="PeachPuff2")

    gName.grid(row=1, column=1)
    gDay.grid(row=1, column=2)
    gHDay.grid(row=1, column=3)
    gIsAvail.grid(row=1, column=4)

    with open(base, 'r') as f:
        for line in f:

            name, day, hday, isAvailable = line.strip().split(':')

            nm = Label(windowSearch, text=name, bg="PeachPuff2")
            dy = Label(windowSearch, text=day, bg="PeachPuff2")
            hdy = Label(windowSearch, text=hday, bg="PeachPuff2")
            isAvail = Label(windowSearch, text=isAvailable, bg="PeachPuff2")

            nm.grid(row=i, column=1)
            dy.grid(row=i, column=2)
            hdy.grid(row=i, column=3)
            isAvail.grid(row=i, column=4)
            i += 1

    windowSearch.mainloop()


def winAddTool():
    global windowAddTool
    global eName
    global eDay
    global eHDay
# window 5
    windowAddTool = Tk()
    windowAddTool.title('Add new tool')
    windowAddTool.config(bg="PeachPuff2")
    windowAddTool.geometry("250x400")

    gName = Label(windowAddTool, text='Name', font='bold', bg="PeachPuff2")
    gDay = Label(windowAddTool, text='Price per Day', font='bold', bg="PeachPuff2")
    gHDay = Label(windowAddTool, text='Price per half day', font='bold', bg="PeachPuff2")

    eName = Entry(windowAddTool)
    eDay = Entry(windowAddTool)
    eHDay = Entry(windowAddTool)

    addButton = Button(windowAddTool, text='Add', command=addTool, bg="PeachPuff3")

    gName.grid(row=1, column=1)
    gDay.grid(row=2, column=1)
    gHDay.grid(row=3, column=1)
    eName.grid(row=1, column=2)
    eDay.grid(row=2, column=2)
    eHDay.grid(row=3, column=2)
    addButton.grid(row=4, columnspan=2, sticky=W)

    windowAddTool.mainloop()


def addTool():
    with open(base, 'a') as f:
        f.write(eName.get())
        f.write(':')
        f.write(eDay.get())
        f.write(':')
        f.write(eHDay.get())
        f.write(':')
        f.write('true')
        f.write('\n')
        f.close()

    messagebox.showinfo('Success', 'Tool added')
    windowAddTool.destroy()

#window 5 close
def logOut():
    messagebox.showinfo('Logged out', 'Logged out successfully')
    windowLogged.destroy()
    logIn()

#window 3 close
if os.path.isfile(creds):
    logIn()
else:
    signUp()