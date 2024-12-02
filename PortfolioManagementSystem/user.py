from watchlist import WatchList
from portfolio import Portfolio

class User:
    def __init__(self, id, name) -> None:
        self.userID = id
        self.name = name
        self.portfolio = Portfolio(self)
        self.watchlist = WatchList(self)
        return
    
    def getPortfolio(self):
        return self.portfolio
    
    def getWatchlist(self):
        return self.watchlist