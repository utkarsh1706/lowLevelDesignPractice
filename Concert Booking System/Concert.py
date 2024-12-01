from seats import *
from typing import List

class Concert:
    def __init__(self, performer: str, seats: List[Seat], date, venue: str) -> None:
        self.performer = performer
        self.seats = seats
        self.date = date
        self.venue = venue
    
    def getAvailableSeats(self, seatType: SeatType) -> List[Seat]:
        available = []
        for s in self.seats:
            if s.checkAvailabilty() and s.seatType==seatType:
                available.append(s)
        return available
    
    def getPerformer(self):
        return self.performer
    
    def getDate(self):
        return self.date
    
