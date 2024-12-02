from user import User
from loan import Loan, LoanStatus

class Admin:
    def __init__(self, name, id) -> None:
        self.name = name
        self.employeeID = id
        return
    
    def loanApprovalCheck(self, user: User, loan: Loan):
        if user.getCreditScore() >= 500:
            loan.updateStatus(LoanStatus.APPROVED)
            print("Loan Approved")
        else:
            loan.updateStatus(LoanStatus.REJECTED)
            print("Loan Rejected!")