from threading import Lock
from portfolio import Portfolio
from user import User

class PortfolioManager:
    
    _instance = None
    
    def __init__(self) -> None:
        if PortfolioManager._instance is not None:
            raise ValueError("Singleton Class!")
        self.users = {}
        self.lock = Lock()
        return
    
    @staticmethod
    def getInstance(self):
        if PortfolioManager._instance is None:
            PortfolioManager._instance = PortfolioManager()
            return PortfolioManager._instance
        raise ValueError("Singleton Class!")
    
    def addUser(self, user: User):
        self.users[user.userID] = user
        return
    
    def removeUser(self, userID):
        x = self.users.get(userID)
        if x:
            del self.users[userID]
        return
    
    def addHolding(self, user, asset):
        with self.lock:
            user.portfolio.addHolding(asset)
            return
    
    def removeHolding(self, user, asset):
        with self.lock:
            user.portfolio.removeHolding(asset)
            return
        
    def addToWatchList(self, user, asset):
        with self.lock:
            user.watchlist.addtowatchlist(asset)
        return
        
    def removeToWatchList(self, user, asset):
        with self.lock:
            user.watchlist.removeFromWatchList(asset)
        return
    

    
