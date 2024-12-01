import uuid
from enum import Enum
from Concert import *
from seats import *
from payment import *
from typing import List
from Creditcard import *
from upi import *
from threading import Lock
from user import User

class BookingStatus(Enum):
    DONE = 1
    CANCELED = 2
    INPROGRESS = 3

class Booking:
    def __init__(self, bookingID, concert: Concert, seats: List[Seat], user: User) -> None:
        self.bookingID = bookingID
        self.concert = concert
        self.seatsBooked = seats
        self.totalPrice = 0
        self.paymentStatus = PaymentStatus.PENDING
        self.bookingStatus = BookingStatus.INPROGRESS
        self.lock = Lock()
        self.user = user
    
    def cancelBooking(self):
        self.bookingStatus = BookingStatus.CANCELED
        for s in self.seatsBooked:
            s.cancelSeat()
        return
    
    def getPrice(self):
        total = 0
        for s in self.seatsBooked:
            total += s.getPrice()
        self.totalPrice = total
        return total

    def processPayment(self, method):
        print("Processing Payment")
        if method=="CreditCard":
            p = CreditCard()
        else:
            p = UPI()
        p.setPaymentStatus()
        self.bookingStatus = BookingStatus.DONE
        self.paymentStatus = PaymentStatus.DONE
        return