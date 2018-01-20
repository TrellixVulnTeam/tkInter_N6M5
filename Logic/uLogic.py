from Logic.dbLogic import DataBaseLogic


class UserLogic:
    def __init__(self):
        return

    def clientCreate(self, uName, pswd):
        db = DataBaseLogic()
        db.addClient(uName, pswd)

    def getClientDetail(self, uId):
        db = DataBaseLogic()
        db.getClientDetail(uId)

    def walletBalance(self, userid, price):
        db = DataBaseLogic()
        db.uWalletBalance(userid, price)