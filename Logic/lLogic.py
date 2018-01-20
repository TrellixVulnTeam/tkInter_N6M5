from Logic.dbLogic import DataBaseLogic


class LoginLogic:
    uId = 0
    uDetails = ''
    session = False

    def __init__(self):
        pass

    def uLogIn(self, uName, uPswd):
        db = DataBaseLogic
        login = db.getClient('login', uName, uPswd)
        if login:
            self.session = True
            self.uId = login[0]['uId']
            self.uDetails = login[0]

    def uLogOut(self):
        self.session = False