from enum import Enum

class CarType(Enum):
    SUV = 1
    MUV = 2
    HATCHBACK = 3

class Car:
    def __init__(self, make, name, seatCount, carType: CarType, price) -> None:
        self.make = make
        self.name = name
        self.isAvailable = True
        self.seats = seatCount
        self.carType = carType
        self.price = price

    def bookCar(self):
        self.isAvailable = False
        return
    
    def cancelCar(self):
        self.isAvailable = True
        return
    
    def getSeatCount(self):
        return self.seats
    
    def getMaker(self):
        return self.make
    
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getCarType(self):
        return self.carType