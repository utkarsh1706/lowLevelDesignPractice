from user import User
from car import Car, CarType
from bookingManager import BookingManager

class CarRental:
    @staticmethod
    def run():
        user1 = User("Utkarsh", "KDLP", "123")
        user2 = User("Aditya", "BHCP", "987")

        car1 = Car("Toyota", "Innova", 7, CarType.MUV, 400)
        car2 = Car("Hyundai", "Creta", 5, CarType.SUV, 300)
        car3 = Car("Maruti", "Swift", 5, CarType.HATCHBACK, 200)

        bookingManager = BookingManager.getInstance()

        bookingManager.addCar(car1)
        bookingManager.addCar(car2)
        bookingManager.addCar(car3)
        bookingManager.addUser(user1)
        bookingManager.addUser(user2)

        carsAvailable = bookingManager.findCar(CarType.SUV, 3)
        if not carsAvailable:
            print("no cars available!")
            return
        
        booking = bookingManager.createBooking(carsAvailable[0], user2, "UPI")
        bookingManager.cancelBooking(booking.bookingID)

if __name__=="__main__":
    CarRental.run()