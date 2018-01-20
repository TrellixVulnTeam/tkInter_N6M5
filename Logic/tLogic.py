from Logic.dbLogic import DataBaseLogic
from Logic.rLogic import LeaseLogic


class ToolLogic:
    lease = LeaseLogic
    toolList = []

    def addTool(self, uId, name, type, condition, photos, description, price):
        db = DataBaseLogic
        db.addTool(uId, name, type, condition, photos, description, price)

    def getListAll(self, uId):
        db = DataBaseLogic
        return db.getTool('uId', uId)

    def searchType(self, type):
        db = DataBaseLogic
        return db.getTool('type', type)

    def searchName(self, name):
        db = DataBaseLogic
        return db.getTool('name', name)

    def searchId(self, tId):
        db = DataBaseLogic
        self.toolList = db.getTool('tId', tId)
        return self.toolList[0]