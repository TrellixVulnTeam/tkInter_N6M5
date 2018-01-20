from tinydb import *
import time


class DataBaseLogic:

    dbClient = ''
    dbTool = ''
    dbLease = ''
    dbPay = ''

    def __init__(self):

        self.dbClient = TinyDB('Db/clients.json')
        self.dbLease = TinyDB('Db/leases.json')
        self.dbPay = TinyDB('Db/payments.json')
        self.dbTool = TinyDB('Db/tools.json')

    #client database related queries
    def addClient(self, user, pswd):

        self.dbClient.insert({
            'uId': int(time.time()), 'cName': user, 'cPass': pswd, 'mAvail': 0
        })

    def getClient(self, action, uName, uPswd):
        client = Query()
        if action == 'login':
            return self.dbClient.search(
                (client.name == uName) &(client.pswd == uPswd)
            )

    def getClientDetail(self, uId):
        client = Query()
        return self.dbClient.search(client.id == uId)

    def uWalletBalance(self, uId, price):
        client = Query()
        temp = self.dbClient.search(client.id == uId)
        temp = temp[0]
        self.dbClient.update({
            'mAvail': temp['mAvail'] - price},
            client.id == uId
        )

    #payments database related querries
    def addPayment(self, uId, items, price, oId, photos):
        self.dbPay.insert({
            "id": str(time.time()), 'uId': uId, 'items': items, 'price': price, 'made': time.time(), "from": oId, "photos": photos
        })

    def getPaymentUser(self, uId):
        paym = Query()
        return self.dbPay.search(paym.uId == uId)

    def getPayment(self, pId):
        paym = Query()
        return self.dbPay.search(paym.id == pId)

    def getPaymentByUser(self, uId):
        paym = Query()
        return self.dbPay.search(paym.oId == uId)


    #tool database related queries
    def addTool(self, uId, name, type, condition, photos, description, price):

        self.dbTool.insert({
            'id': int(time.time()), 'user': uId, 'name': name, 'type': type, 'condition': condition, 'photo': photos, 'dscp': description, 'price': price
        })

    def getTool(self, search, query):
        tool = Query()
        if search == "tType":
            return self.dbTool.search(tool.tType == query)
        elif search == "name":
            return self.dbTool.search(tool.name == query)
        elif search == "uId":
            return self.dbTool.search(tool.uId == query)
        elif search == 'tId':
            return self.dbTool.search(tool.tId == query)

    #lease database related queries
    def addLease(self, uId, tId, sDate, eDate):

        self.dbLease.insert({
            'id': int(time.time()), 'user': uId, 'tool': tId, 'start': sDate, 'end': eDate, 'isAvailable': 0
        })

    def isAvailable(self, tId, dStart, dEnd):
        lease = Query()

        return self.dbLease.search(
            lease.tId == tId and (lease.dStart >= dStart or lease.dEnd <= dEnd or lease.dEnd >= dEnd or lease.dEnd >= dStart)
        )

    def leaseUser(self, uId):
        lease = Query()
        return self.dbLease.search((lease.uId == uId) & (lease.status == 0))

    def getLease(self, lId):
        lease = Query()
        return self.dbLease.search(lease.id == lId)

    def endLease(self, lId):
        lease = Query()

        self.dbLease.update({'isAvailable': 1}, lease.id == lId)