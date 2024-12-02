class Stock:
    def __init__(self, id, name, price) -> None:
        self.name = name
        self.stockID = id
        self.price = price

    def getPrice(self):
        return self.price
    
    def updatePrice(self, updatedPrice):
        self.price = updatedPrice
        return
    
    def getSymbol(self):
        return self.name