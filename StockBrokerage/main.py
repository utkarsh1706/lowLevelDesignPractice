from stockBroker import StockBroker
from user import User
from account import Account
from stock import Stock
from sellOrder import SellOrder
from buyOrder import BuyOrder

class StockBrokerage:
    @staticmethod
    def run():
        stockBroker = StockBroker.getInstance()
        
        stock1 = Stock(1, "OLA", 78)
        stock2 = Stock(2, "UBER", 200)
        
        stockBroker.addStock(stock1)
        stockBroker.addStock(stock2)
        
        user1 = User("Utkarsh", "1234")
        user2 = User("Manoj", "3456")
        
        stockBroker.addUser(user1)
        stockBroker.addUser(user2)
        
        account1 = Account(1000, user1)
        account2 = Account(2000, user2)
        
        stockBroker.addAccount(account1)
        stockBroker.addAccount(account2)

        order1 = SellOrder(1, stock1, account2, 5)
        stockBroker.executeOrder(order1)
        order2 = BuyOrder(2, stock1, account1, 10)
        stockBroker.executeOrder(order2)
        
        return

if __name__=="__main__":
    StockBrokerage.run()