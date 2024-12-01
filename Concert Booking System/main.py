from BookingManager import BookingManager
from Concert import Concert
from user import User
from seats import Seat, SeatType

class ConcertBooking:
    @staticmethod
    def createSeats(count):
        seats = []
        for i in range(count):
            if i < 500:
                seats.append(Seat(i, SeatType.ECONOMY, 100))
            elif i < 800:
                seats.append(Seat(i, SeatType.PREMIUM, 500))
            else:
                seats.append(Seat(i, SeatType.VIP, 1000))
        return seats

    @staticmethod
    def run():
        bookingManager = BookingManager.getInstance()
        
        user1 = User("Utkarsh", 123)
        user2 = User("Aditya", 345)

        seats1 = ConcertBooking.createSeats(1000)
        concert1 = Concert("Diljit", seats1, "13 December", "Delhi")

        seats2 = ConcertBooking.createSeats(5000)
        concert2 = Concert("Arijit", seats2, "14 December", "Mumbai")

        bookingManager.addConcert(concert1)
        bookingManager.addConcert(concert2)
        bookingManager.addUser(user1)
        bookingManager.addUser(user2)

        concertsByPerformer = bookingManager.findConcert("Diljit")
        if not concertsByPerformer:
            raise ValueError("Concert not found")

        concertToBook = concertsByPerformer[0]

        availableSeats = bookingManager.bookSeats(concertToBook, SeatType.PREMIUM, 20)
        bookingID = bookingManager.addBooking(concertToBook, availableSeats, user1)

        bookingManager.cancelBooking(bookingID)

if __name__ == "__main__":
    ConcertBooking.run()
