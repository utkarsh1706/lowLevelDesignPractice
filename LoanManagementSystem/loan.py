from enum import Enum
from user import User

class LoanStatus(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

class Loan:
    def __init__(self, user: User, pa, tenure, interest, id: int) -> None:
        self.user = user
        self.status = LoanStatus.PENDING
        self.interest = interest
        self.principalAmount = pa
        self.tenure = tenure
        self.id = id
        self.outstandingAmount = self.calculateTotalAmount()
        return
    
    def calculateEMI(self):
        rate = self.interest / 12 / 100
        numerator = self.principalAmount * rate * ((1 + rate) ** self.tenure)
        denominator = ((1 + rate) ** self.tenure) - 1
        return round(numerator / denominator, 2)
    
    def calculateTotalAmount(self):
        return self.calculateEMI() * self.tenure
    
    def updateOutstading(self, amount):
        self.outstandingAmount += amount
        return
    
    def updateStatus(self, status: LoanStatus):
        self.status = status
        return
