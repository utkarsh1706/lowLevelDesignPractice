class Portfolio:
    def __init__(self, account) -> None:
        self.holdings = {}
        self.account=  account

    def addStock(self, stock, quantity):
        self.holdings[stock.getSymbol()] += quantity
        return
    
    def getPortfolio(self):
        return self.holdings
    
    def removeStock(self, stock, quantity):
        currStockQ = self.holdings.get(stock.getSymbol(), 0)
        if currStockQ==0:
            raise ValueError("No stock is found")
        if currStockQ < quantity:
            raise ValueError("Not enough quantity")
        currStockQ -= quantity
        self.holdings[stock.getSymbol()] = currStockQ
        if currStockQ==0:
            del self.holdings[stock]
        return

