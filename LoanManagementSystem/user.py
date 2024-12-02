from loan import Loan
from Repayment import Repayment

class User:
    def __init__(self, name, phNo, cs) -> None:
        self.name = name
        self.phNo = phNo
        self.loans = []
        self.creditScore = cs
        self.repayments = []

    def getCreditScore(self):
        return self.creditScore
    
    def getLoans(self):
        return self.loans
    
    def getRepayments(self):
        return self.repayments
    
    def addLoan(self, loan: Loan):
        self.loans.append(loan)
        return
    
    def addRepayment(self, repayment: Repayment):
        self.repayments.append(repayment)
        return