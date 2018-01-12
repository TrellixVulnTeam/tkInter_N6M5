from tkinter import *
import os


creds = 'users.txt'
base = 'search.txt'
credss = {}


def signUp():
    global windowSignIn
    global entryLogin
    global entryPswd
    global msgError
#window 1
    windowLogin.destroy()
    windowSignIn = Tk()
    windowSignIn.title('Sign up')
    windowSignIn.config(bg="PeachPuff2")
    windowSignIn.geometry("250x400")
    instruction = Label(windowSignIn, text='Please enter new credidentials\n', bg="PeachPuff2")
    instruction.grid(row=0, column=0, sticky=E)

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

    msgError = Label(windowSignIn, bg="PeachPuff3")
    msgError.grid(row=3, columnspan=1, sticky=W)

    windowSignIn.mainloop()


def bSignup():
    with open(creds, 'r') as f:
        for line in f:
            user, pswd = line.strip().split(':')
            x=user

    checkUsr = entryLogin.get()
    if checkUsr in user:
        msgError.configure(text='User exists already!')
    else:
        with open(creds, 'a') as f:
            f.write(entryLogin.get())
            f.write(':')
            f.write(entryPswd.get())
            f.write('\n')
            f.close()

    windowSignIn.destroy()
    logIn()

# window 1 close
def logIn():
    global entryLoginL
    global entryPswdL
    global windowLogin
    global error
#window 2
    windowLogin = Tk()
    windowLogin.title('Login')
    windowLogin.config(bg="PeachPuff2")
    windowLogin.geometry("250x400")



    instruction = Label(windowLogin, text='             Log in!\n', bg="PeachPuff2", font="-weight bold")
    instruction.grid(sticky=E)
    labelLoginL = Label(windowLogin, text='Login: ', bg="PeachPuff2")
    labelLoginL.grid(row=1, sticky=W)
    labelPswdL = Label(windowLogin, text='Password: ', bg="PeachPuff2")
    labelPswdL.grid(row=2, sticky=W)

    entryLoginL = Entry(windowLogin)
    entryLoginL.grid(row=1, column=1)
    entryPswdL = Entry(windowLogin, show='*')
    entryPswdL.grid(row=2, column=1)

    buttonLog = Button(windowLogin, text='Login', command=checkLogin, bg="PeachPuff3")
    buttonReg = Button(windowLogin, text='Register', command=signUp, bg="PeachPuff3")
    buttonLog.grid(columnspan=2, sticky=W)
    buttonReg.grid(columnspan=2, sticky=W)

    error = Label(windowLogin, bg="PeachPuff2")
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
        error.configure(text="Credentials are wrong", bg="PeachPuff2")
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
    gName.grid(row=1, column=1)
    gDay.grid(row=2, column=1)
    gHDay.grid(row=3, column=1)

    eName = Entry(windowAddTool)
    eDay = Entry(windowAddTool)
    eHDay = Entry(windowAddTool)
    eName.grid(row=1, column=2)
    eDay.grid(row=2, column=2)
    eHDay.grid(row=3, column=2)

    addButton = Button(windowAddTool, text='Add', command=addTool, bg="PeachPuff3")
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

#window 5 close
def logOut():
    windowLogged.destroy()
    logIn()

#window 3 close
if os.path.isfile(creds):
    logIn()
else:
    signUp()