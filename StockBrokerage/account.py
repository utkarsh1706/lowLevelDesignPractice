from user import User
from portfolio import Portfolio
import uuid

class Account:
    def __init__(self, balance: float, user: User) -> None:
        self.accountID = self.generateAccountID()
        self.balance = balance
        self.user = user
        self.portfolio = Portfolio(self)

    def depositBalance(self, b):
        self.balance += b
        return
    
    def withdrawBalance(self, b):
        if self.balance < b:
            raise ValueError("Low Balance")
        self.balance -= b
        return
    
    def getBalance(self):
        return self.balance
    
    def generateAccountID(self):
        return str(uuid.uuid4()).replace('-', '')[:12]
    
    def getID(self):
        return self.accountID
    
