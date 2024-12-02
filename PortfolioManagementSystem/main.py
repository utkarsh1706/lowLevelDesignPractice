from portfolioManager import PortfolioManager
from user import User
from portfolio import Portfolio
from assets import Assets
from crypto import Crypto
from stock import Stock
from mutualFund import MutualFunds
from reportGenerator import ReportGenerator

class PortfolioManagementSystem:
    
    @staticmethod
    def run():
        pms = PortfolioManager()
        
        user1 = User(1, "Utkarsh")
        user2 = User(2, "Aditya")
        
        pms.addUser(user1)
        pms.addUser(user2)
        
        stock1 = Stock("AAPL", 20, 100)
        token1 = Crypto("BTC", 1, 96000)
        mutualFund = MutualFunds("UTI", 10, 1000)
        
        pms.addHolding(user1, stock1)
        pms.addHolding(user1, mutualFund)

        pms.addToWatchList(user2, token1)

        print("User 2 Watchlist:", user2.getWatchlist().getWatchlistData())

        pms.removeToWatchList(user2, token1)
        
        print(ReportGenerator.generateReport(user1.getPortfolio()))
        return

if __name__=="__main__":
    PortfolioManagementSystem.run()