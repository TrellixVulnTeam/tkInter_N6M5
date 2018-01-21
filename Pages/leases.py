import time
import datetime

from tkinter import *
from tkinter.ttk import *
from datetime import timedelta, datetime

from Logic.rLogic import LeaseLogic
from Logic.mSettings import Settings
from Logic.ttkcalendar import *
from Logic.uLogic import UserLogic

from Pages.searchEngine import Result
from Pages.payments import PaymentPage


class Lease(Frame):
    def __init__(self, parent, logic):
        Frame.__init__(self, parent)

        from Pages.main import MainPage
        from Logic.tLogic import ToolLogic

        self.logic = logic
        self.lease = LeaseLogic()
        self.tool = ToolLogic()

        Frame.__init__(self, parent)

        self.logic = logic

        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()
        Button(self, text='Go back', command=lambda: self.logic.show_frame(Result)).pack(padx=10, pady=10)

        Label(self, text='Check Availability', font=Settings.lFont).pack(padx=10, pady=10)

        Label(self, text='Start Date', font=Settings.lFont).pack(padx=10, pady=10)
        self.dStart = Calendar(self, firstweekday=calendar.SUNDAY)
        self.dStart.pack()

        Label(self, text='End Date', font=Settings.lFont).pack(padx=10, pady=10)
        self.dEnd = Calendar(self, firstweekday=calendar.SUNDAY)
        self.dEnd.pack()

        Button(self, text='Check Availability', command=self.isAvail).pack()

        self.errors = Label(self, text='', font=Settings.sFont)
        self.errors.pack()
        self.rent = Button(self, text='Lease',
                           state=DISABLED, command=self.rent)
        self.rent.pack()
        
        if 'win' not in sys.platform:
            style = ttk.Style()
            style.theme_use('alt')

    def lease(self):
        from Pages.succeded import Success
        if self.dStart.selection > self.dEnd.selection:
            self.errors['text'] = "You can't return tool before you lease it!"
            return
        if self.lease.isAvailable(self.logic.tId, self.dStart.selection, self.dEnd.selection):
            self.lease.addLease(self.logic.session.uId, self.logic.tId, self.dStart.selection, self.dEnd.selection)
            self.logic.show_frame(Success)
        else:
            self.errors['text'] = 'Sorry, tool is unavailable in that time'

    def isAvail(self):
        self.errors['text'] = ''
        if self.dStart.selection > self.dEnd.selection :
            self.errors['text'] = "You can't return tool before you lease it!"
            return
        elif self.dEnd.selection - self.dStart.selection>timedelta(days=3) and self.logic.price == 0:
            self.errors['text'] = "Renting can't be longer than 3 days"
        elif self.dStart.selection <= datetime.now():
            self.errors['text'] = 'Start Date has to be in future'
        if self.lease.isAvailable(self.logic.tId, self.dStart.selection, self.dEnd.selection):
            self.lease.config(state=NORMAL)
        else:
            self.errors['text'] = 'Sorry, tool is unavailable in that time'

    def run(self):
        pass


class FinishLease(Frame):
    leasedItem = ''
    leaseSum = 0
    fee = 0
    insurance = 5
    totalPrice = 0
    items = []
    oId = 0
    
    def __init__(self, parent, logic):
        Frame.__init__(self, parent)
        from Pages.main import MainPage
        from Pages.searchEngine import Result
        from Logic.mSettings import Settings
        from Logic.tLogic import ToolLogic
        from Logic.rLogic import LeaseLogic
        
        self.logic = logic
        self.tool = ToolLogic()
        self.lease = LeaseLogic()
        self.logic = logic
        
        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()
        Label(self, text='Return Tool', font=Settings.lFont).pack(padx=10, pady=10)
        
        Button(self, text='Go back!', command=lambda: self.logic.show_frame(Result)).pack(padx=10, pady=10)
        Label(self, text='Payment List:', font=Settings.lFont).pack(padx=10, pady=10)
        
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)
        
        Label(self, text='Additional Info:', font=Settings.lFont).pack(padx=10, pady=10)
        self.addInfo = Label(self, text='Additional Info:', font=Settings.lFont)
        self.addInfo.pack(padx=10, pady=10)
        
        Label(self, text='Photos:', font=Settings.lFont).pack()
        Button(self, text='Browse', command=self.addToolPhoto).pack()
        
        Label(self, text='Price', font=Settings.lFont).pack(padx=10, pady=10)
        self.price = Label(self, text='Price', font=Settings.lFont)
        self.price.pack(padx=10, pady=10)

        Button(self, text='Confirm', command=self.makeLease).pack()

    def makeLease(self):
        self.lease.endLease(self.logic.lId, self.totalPrice, self.logic.session.uId)
        self.payments.addPayment(self.logic.session.uId, self.items, self.totalPrice)
        self.logic.show_frame(PaymentPage)

    def addToolPhoto(self):
        from Logic.fLogic import FileLogic
        file = FileLogic()
        self.photos = file.addPhoto()
        print(self.photos)

    def run(self):
        from Logic.pLogic import PaymentsLogic
        self.payments = PaymentsLogic()
        self.leaseItem = self.lease.getLeases(self.logic.selectrental)
        tool = self.tool.searchId(self.leasedItem['tId'])
        self.oId = tool['uId']
        fee = int(tool['price'])
        now = time.time()
        if (self.leasedItem['dEnd'] < now):
            self.addInfo.config(
                text='Your payment is multiplied 2 times, because you should finish renting before end date')
            fee = int(fee) * 2
        Label(self.frame, text=tool['name']).pack(padx=10, pady=10)
        days = datetime.datetime.utcfromtimestamp(now) - datetime.datetime.utcfromtimestamp(
            self.leasedItem['dStart'])
        itemPrice = fee * int(days.days)
        self.itemlist = [tool['name'] + ' Price:' + str(itemPrice), 'Insurance Price:' + str(self.insurance)]

        Label(self.frame, text='Price: ' + str(itemPrice),
              font=Settings.lFont).pack(padx=10, pady=10)
        Label(self.frame, text='Insurance: ').pack(padx=10, pady=10)
        Label(self.frame, text='Price: ' + str(self.insurance),
              font=Settings.lFont).pack(padx=10, pady=10)
        price = int(itemPrice) + self.insurance

        self.price.config(
            text='Total:' + str(price))
        self.totalPrice = price
