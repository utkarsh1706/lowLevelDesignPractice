from user import User
from payment import Payment
from creditCard import CreditCard
from UPI import UPI
from car import Car
from enum import Enum

class BookingStatus(Enum):
    DONE = 1
    FAILED = 2
    INPROGRESS = 3
    CANCELLED = 4


class Booking:
    def __init__(self, bookingID, car: Car, user: User) -> None:
        self.bookingID = bookingID
        self.car = car
        self.user = user
        self.bookingStatus = BookingStatus.INPROGRESS
        self.price = self.car.getPrice()

    def cancelBooking(self):
        self.car.cancelCar()
        self.bookingStatus = BookingStatus.CANCELLED
        return
    
    def processPayment(self, method):
        if method=="UPI":
            p = UPI()
        elif method=="CreditCard":
            p = CreditCard()
        else:
            self.bookingStatus = BookingStatus.FAILED
            self.cancelBooking()
            return
        self.bookingStatus = BookingStatus.DONE
        return
    
    def getBookingID(self):
        return self.bookingID
    
