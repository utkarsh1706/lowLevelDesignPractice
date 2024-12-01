import uuid
from user import User
from Concert import Concert
from booking import Booking
from threading import Lock

class BookingManager:
    _instance = None

    def __init__(self):
        if BookingManager._instance is not None:
            raise ValueError("Instance is already created!")
        BookingManager._instance = self
        self.bookings = {}
        self.users = []
        self.concerts = []
        self.lock = Lock()

    @staticmethod
    def getInstance():
        if BookingManager._instance is None:
            with Lock():
                if BookingManager._instance is None:
                    BookingManager._instance = BookingManager()
        return BookingManager._instance

    def addBooking(self, concert, seats, user):
        with self.lock:
            bookingID = self.generateBookingID()
            booking = Booking(bookingID, concert, seats, user)
            booking.processPayment("CreditCard")
            self.bookings[bookingID] = booking
        return bookingID

    def cancelBooking(self, bookingID):
        with self.lock:
            booking = self.bookings.get(bookingID)
            if booking is None:
                raise ValueError("No such booking found")
            booking.cancelBooking()
            del self.bookings[bookingID]

    def addConcert(self, concert: Concert):
        with self.lock:
            self.concerts.append(concert)

    def addUser(self, user: User):
        with self.lock:
            self.users.append(user)

    def findConcert(self, performer):
        with self.lock:
            return [c for c in self.concerts if c.performer == performer]

    def bookSeats(self, concert, typeSeat, seatCount):
        with self.lock:
            seatsConcert = concert.getAvailableSeats(typeSeat)
            if len(seatsConcert) < seatCount:
                raise ValueError("Not enough seats present")
            seatsToBook = seatsConcert[:seatCount]
            for s in seatsToBook:
                s.bookSeat()
            return seatsToBook

    def generateBookingID(self):
        return str(uuid.uuid4()).replace('-', '')[:8]
