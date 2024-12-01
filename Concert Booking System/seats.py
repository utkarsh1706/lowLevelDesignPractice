from enum import Enum

class SeatType(Enum):
    PREMIUM = 1
    ECONOMY = 2
    VIP = 3

class Seat:
    def __init__(self, num, seatType: SeatType, price) -> None:
        self.seatNo = num
        self.seatType = seatType
        self.price = price
        self.isAvailable = True

    def checkAvailabilty(self):
        return self.isAvailable
    
    def bookSeat(self):
        self.isAvailable = False

    def getPrice(self):
        return self.price
    
    def cancelSeat(self):
        self.isAvailable = True
    


    