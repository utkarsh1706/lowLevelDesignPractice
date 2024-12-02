class Portfolio:
    
    def __init__(self, user) -> None:
        self.user = user
        self.holdings = []
        return
    
    def addHolding(self, asset):
        self.holdings.append(asset)
        return
    
    def removeHolding(self, assetName):
        self.holdings = [h for h in self.holdings if h.getName()!=assetName]
        return
    
    def getPortfolioValue(self):
        totalValue = 0
        for h in self.holdings:
            totalValue += h.getValue()
        return totalValue
    
    def getBreakDown(self):
        breakdown = {}
        for h in self.holdings:
            breakdown[h.getName()] = h.getValue()
        return breakdown