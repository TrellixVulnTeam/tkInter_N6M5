from tkinter import *
import os

creds = 'users.txt'
base = 'search.txt'
credss = {}


def signUp():
    global windowSignIn
    global entryLogin
    global entryPswd
    windowLogin.destroy()
    windowSignIn = Tk()
    windowSignIn.title('Sign up')
    instruction = Label(windowSignIn, text='Please enter new credidentials\n')
    instruction.grid(row=0, column=0, sticky=E)

    labelLogin = Label(windowSignIn, text='New login: ')
    labelLogin.grid(row=1, column=0, sticky=W)
    labelPswd = Label(windowSignIn, text='New password: ')
    labelPswd.grid(row=2, column=0, sticky=W)

    entryLogin = Entry(windowSignIn)
    entryLogin.grid(row=1, column=1)
    entryPswd = Entry(windowSignIn, show='*')
    entryPswd.grid(row=2, column=1)

    buttonSign = Button(windowSignIn, text='Sign up', command=bSignup)
    buttonSign.grid(columnspan=2, sticky=W)
    windowSignIn.mainloop()


def bSignup():
    with open(creds, 'w') as f:
        f.write(entryLogin.get())
        f.write(':')
        f.write(entryPswd.get())
        f.write('\n')
        f.close()

    windowSignIn.destroy()
    logIn()


def logIn():
    global entryLoginL
    global entryPswdL
    global windowLogin
    global error

    windowLogin = Tk()
    windowLogin.title('Login')

    instruction = Label(windowLogin, text='Log in!\n')
    instruction.grid(sticky=E)
    labelLoginL = Label(windowLogin, text='Login: ')
    labelLoginL.grid(row=1, sticky=W)
    labelPswdL = Label(windowLogin, text='Password: ')
    labelPswdL.grid(row=2, sticky=W)

    entryLoginL = Entry(windowLogin)
    entryLoginL.grid(row=1, column=1)
    entryPswdL = Entry(windowLogin, show='*')
    entryPswdL.grid(row=2, column=1)

    buttonLog = Button(windowLogin, text='Login', command=checkLogin)
    buttonReg = Button(windowLogin, text='Register', command=signUp)
    buttonLog.grid(columnspan=2, sticky=W)
    buttonReg.grid(columnspan=2, sticky=W)

    error = Label(windowLogin)
    error.grid(row=6)

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
        error.configure(text="Credentials are wrong")
        windowLogin.mainloop()


def mainWindow():
    global windowLogged

    windowLogged = Tk()
    windowLogged.title('Search Engine')
    windowLogged.geometry('120x350')

    sEngineB = Button(windowLogged, text="Search", command=searchEngine)
    sAddB = Button(windowLogged, text='Add', command=winAddTool)
    logOutB = Button(windowLogged, text="Logout", command=logOut)

    sEngineB.place(relx=0.5, rely=0.1, anchor=CENTER)
    sAddB.place(relx=0.5, rely=0.2, anchor=CENTER)
    logOutB.place(relx=0.5, rely=0.3, anchor=CENTER)
    windowLogged.mainloop()


def searchEngine():
    windowSearch = Tk()
    windowSearch.title('Tools')
    i = 2
    gName = Label(windowSearch, text='Name', font='bold')
    gDay = Label(windowSearch, text='Per Day', font='bold')
    gHDay = Label(windowSearch, text='Half of Day', font='bold')
    gIsAvail = Label(windowSearch, text='Is Available', font='bold')
    gName.grid(row=1, column=1)
    gDay.grid(row=1, column=2)
    gHDay.grid(row=1, column=3)
    gIsAvail.grid(row=1, column=4)
    with open(base, 'r') as f:
        for line in f:
            name, day, hday, isAvailable = line.strip().split(':')
            nm = Label(windowSearch, text=name)
            dy = Label(windowSearch, text=day)
            hdy = Label(windowSearch, text=hday)
            isAvail = Label(windowSearch, text=isAvailable)
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

    windowAddTool = Tk()
    windowAddTool.title('Add new tool')

    gName = Label(windowAddTool, text='Name', font='bold')
    gDay = Label(windowAddTool, text='Price per Day', font='bold')
    gHDay = Label(windowAddTool, text='Price per half day', font='bold')
    gName.grid(row=1, column=1)
    gDay.grid(row=2, column=1)
    gHDay.grid(row=3, column=1)

    eName = Entry(windowAddTool)
    eDay = Entry(windowAddTool)
    eHDay = Entry(windowAddTool)
    eName.grid(row=1, column=2)
    eDay.grid(row=2, column=2)
    eHDay.grid(row=3, column=2)

    addButton = Button(windowAddTool, text='Add', command=addTool)
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

    windowAddTool.destroy()


def logOut():
    windowLogged.destroy()
    logIn()


if os.path.isfile(creds):
    logIn()
else:
    signUp()