from user import User
from car import Car, CarType
from booking import Booking, BookingStatus
from threading import Lock
import uuid

class BookingManager:
    _instance = None

    def __init__(self) -> None:
        if BookingManager._instance is not None:
            raise ValueError("Singleton Class")
        
        self.bookings = {}
        self.users = []
        self.cars = []
        self.lock = Lock()
        return

    @staticmethod
    def getInstance():
        if BookingManager._instance is None:    
            BookingManager._instance = BookingManager()
        return BookingManager._instance
    
    def addCar(self, car: Car):
        self.cars.append(car)
        return
    
    def addUser(self, user: User):
        self.users.append(user)
        return
    
    def generateBookingID(self):
        return str(uuid.uuid4()).replace('-', '')[:8]
    
    def findCar(self, carType, seatCount):
        with self.lock:
            availableCars = []
            for c in self.cars:
                if c.isAvailable and c.getSeatCount()>=seatCount and c.getCarType()==carType:
                    availableCars.append(c)
            return availableCars
    
    def createBooking(self, car, user, method):
        with self.lock:
            bookingID = self.generateBookingID()
            booking = Booking(bookingID, car, user)
            booking.processPayment(method)
            self.bookings[bookingID] = booking
            car.bookCar()
            print(f"Booking Done {booking.bookingID}!")
        return booking
    
    def cancelBooking(self, bookingID):
        with self.lock:
            booking = self.bookings.get(bookingID)
            if booking is None:
                raise Exception("No such booking exists!")
            booking.cancelBooking()
            print(f"Booking Canceled {booking.bookingID}!")
            del self.bookings[bookingID]
        return
