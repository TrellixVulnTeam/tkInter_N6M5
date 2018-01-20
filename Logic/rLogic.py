from Logic.dbLogic import DataBaseLogic
from Logic.uLogic import UserLogic

import time


class LeaseLogic:

    def isAvailable(self, tId, dStart, dEnd):
        db = DataBaseLogic
        if db.isAvailable(tId, time.mktime(dStart.timetuple()), time.mktime(dEnd.timetuple())):
            return False
        return True

    def addLease(self, uId, tId, dStart, dEnd):
        db = DataBaseLogic
        db.addLease(uId, tId, time.mktime(dStart.timetuple()), time.mktime(dEnd.timetuple()))

    def getLeasesUser(self, uId):
        db = DataBaseLogic
        return db.leaseUser(uId)

    def getLeases(self, lId):
        db = DataBaseLogic
        return db.getLease(lId)[0]

    def endLease(self, lId, price, uId):
        db = DataBaseLogic
        user = UserLogic
        user.walletBalance(uId, price)
        return db.endLease(lId)
