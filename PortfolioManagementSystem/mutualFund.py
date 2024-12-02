from assets import Assets

class MutualFunds(Assets):
    def __init__(self, name, quantity, faceValue) -> None:
        super().__init__(name, quantity)
        self.faceValue = faceValue
        return
    
    def getValue(self):
        return self.quantity * self.faceValue
    
    def getPrice(self):
        return self.faceValue
    
    def getName(self):
        return self.name