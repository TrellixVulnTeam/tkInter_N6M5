from tkinter import *
from tkinter.ttk import *

from Logic.mSettings import Settings
from Logic.pLogic import PaymentsLogic


class PaymentPage(Frame):
    def __init__(self, parent, logic):        
        Frame.__init__(self, parent)
        
        from Pages.main import MainPage
        from Pages.searchEngine import Result
        from Logic.tLogic import ToolLogic
        
        self.logic = logic
        self.tool = ToolLogic()
        
        Frame.__init__(self, parent)
        
        self.logic = logic
        
        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()
        Button(self, text='Go Back!', command=lambda: self.logic.show_frame(PaymentsPage)).pack(padx=10, pady=10)
        
        Label(self, text='Return Tool', font=Settings.lFont).pack(padx=10, pady=10)       
        self.pName = Label(self, text='Payment: ', font=Settings.lFont)
        Label(self, text='Payments List: ', font=Settings.lFont).pack(padx=10, pady=10)
        Label(self, text='Additional Info: ', font=Settings.lFont).pack(padx=10, pady=10)
        Label(self, text='Price: ', font=Settings.lFont).pack(padx=10, pady=10)
        self.price = Label(self, text='Price: ', font=Settings.lFont)

        self.addInf = Label(self, text='Additional Info: ', font=Settings.lFont)
        self.addInf.pack(padx=10, pady=10)
        self.photos = Label(self, text='Photos: ', font=Settings.lFont)

        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.photosFrame = Frame(self, relief=RAISED, borderwidth=1)

        self.price.pack(padx=10, pady=10)
        self.pName.pack(padx=10, pady=10)
        self.photosFrame.pack(fill=BOTH, expand=True)
        self.frame.pack(fill=BOTH, expand=True)
        self.photos.pack()

    def run(self):
        self.photos.pack_forget()
        if self.logic.selPaymId != 0:
            pass
        elif self.logic.selPaymeId != 0:
            self.photos.pack()

        pass


class PaymentsPage(Frame):
    paymList = []
    paymeList = []

    def __init__(self, parent, logic):
        Frame.__init__(self, parent)

        from Pages.main import MainPage
        from Pages.searchEngine import Result
        from Logic.tLogic import ToolLogic

        self.logic = logic
        self.tool = ToolLogic()
        self.payments = PaymentsLogic()
        
        Button(self, text='Logout', command=lambda: logic.show_frame(MainPage)).pack()
        Button(self, text='Go back!', command=lambda: self.logic.show_frame(Result)).pack(padx=10, pady=10)

        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.paymBox = Listbox(self, yscrollcommand=scrollBar.set)
        for line in range(100):
            self.paymBox.insert(END, 'Payment number' + str(line))
        scrollBar.config(command=self.paymBox.yview())
        Label(self, text='Payments of my rentings:', font=Settings.lFont).pack(padx=10, pady=10)

        scrollBar = Scrollbar(self)

        self.paymeBox = Listbox(self, yscrollcommand=scrollBar.set)
        for line in range(100):
            self.paymeBox.insert(END, 'Payment number' + str(line))
        scrollBar.config(command=self.paymeBox.yview())
        scrollBar.pack(side=RIGHT, fill=Y)

        self.paymeBox.pack(fill=BOTH)
        self.paymBox.pack(fill=BOTH)

    def run(self):
        if self.logic.session.session:
            payment = self.payments.addPayment(self.logic.session.userdetails['id'])
            self.paymBox.delete(0, END)
            for index, payment in enumerate(payment):
                self.paymBox.insert(END, 'payment' + payment['id'])
                self.paymBox.bind('<<ListboxSelect>>', self.selectPayment)
                self.paymList.append(payment)

            paym = self.payments.getPaymentByUser(self.logic.session.userdetails['id'])
            self.paymeBox.delete(0, END)
            for index, payment in enumerate(paym):
                self.paymeBox.insert(END, 'payment' + payment['id'])
                self.paymeBox.bind('<<ListboxSelect>>', self.selectPaymentByUser)
                self.paymeList.append(payment)

    def selectPayment(self, evt):
        q = evt.widget
        print(q.curselection())
        index = int(q.curselection()[0])
        value = q.get(index)
        self.logic.sPayment = value
        self.logic.sPaymentId = self.paymList[index]['id']
        self.logic.show_frame(PaymentPage)

    def selectPaymentByUser(self, evt):
        q = evt.widget
        print(q.curselection())
        index = int(q.curselection()[0])
        value = q.get(index)
        self.logic.sPayment = value
        self.logic.sPaymentIdByUser = self.paymList[index]['id']
        self.logic.show_frame(PaymentPage)
