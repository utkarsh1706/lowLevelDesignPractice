from payment import *

class UPI(Payment):
    def payment(self):
        return super().payment()
    
    def setPaymentStatus(self):
        return super().setPaymentStatus()