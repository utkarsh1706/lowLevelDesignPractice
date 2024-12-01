from abc import ABC, abstractmethod
from enum import Enum

class PaymentStatus(Enum):
    DONE =  1
    PENDING= 2
    FAILED= 3

class Payment:
    def __init__(self) -> None:
        self.paymentStatus = PaymentStatus.PENDING
    
    @abstractmethod
    def payment(self):
        print("Payment is in process!")

    @abstractmethod
    def setPaymentStatus(self):
        self.paymentStatus = PaymentStatus.DONE