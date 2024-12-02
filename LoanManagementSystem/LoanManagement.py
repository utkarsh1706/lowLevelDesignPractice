from loan import *
from user import User
from admin import Admin
from Repayment import Repayment
from abc import ABC, abstractmethod

class LoanSystem:
    _instance = None
    def __init__(self) -> None:
        if LoanSystem._instance is not None:
            raise ValueError("Singleton Class")
        self.loans = []
        self.repayments = {}
        self.admins = []
        return
    
    @abstractmethod
    def getInstance(self):
        if LoanSystem._instance is None:
            raise ValueError("Singleton Class")
        
        LoanSystem._instance = LoanSystem()
        return LoanSystem._instance
    
    def validateLoan(self, loan: Loan, admin: Admin):
        if admin.loanApprovalCheck(loan.user, loan) is LoanStatus.APPROVED:
            self.loans.append(loan)
        else:
            raise ValueError("Credit Score is low!")
        return
    
    def addLoan(self, loan):
        self.loans.append(loan)
        return