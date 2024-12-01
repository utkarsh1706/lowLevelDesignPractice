from payment import *

class CreditCard(Payment):
    def payment(self):
        return super().payment()
    
    def setPaymentStatus(self):
        return super().setPaymentStatus()