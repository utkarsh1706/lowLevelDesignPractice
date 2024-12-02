from assets import Assets

class Stock(Assets):
    def __init__(self, name, quantity, price) -> None:
        super().__init__(name, quantity)
        self.price = price
        return
    
    def getValue(self):
        return self.quantity * self.price
    
    def getPrice(self):
        return self.price
    
    def getName(self):
        return self.name