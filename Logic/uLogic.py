from Logic.dbLogic import DataBaseLogic


class UserLogic:
    def __init__(self):
        return

    def userCreate(self, uName, pswd):
        db = DataBaseLogic()
        db.addClient(uName, pswd)

    def getUserDetail(self, uId):
        db = DataBaseLogic()
        db.getClientDetail(uId)

    def walletBalance(self, userid, price):
        db = DataBaseLogic()
        db.uWalletBalance(userid, price)
