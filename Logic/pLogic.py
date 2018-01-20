from Logic.dbLogic import DataBaseLogic


class PaymentsController:
    db = DataBaseLogic

    def addPayment(self, uId, items, price, oId, photos):
        self.db.addPayment(uId, items, price, oId, photos)

    def getPaymentUser(self, uId):
        return self.db.getPaymentUser(uId)

    def getPayment(self, pId):
        return self.db.getPayment(pId)

    def getPaymentByUser(self, uId):
        return self.db.getPaymentByUser(uId)
