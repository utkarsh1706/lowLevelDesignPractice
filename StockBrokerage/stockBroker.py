from threading import Lock
from queue import Queue

class StockBroker:
    _instance = None

    def __init__(self) -> None:
        if StockBroker._instance is not None:
            raise ValueError("Singleton Class")
        
        self.orderQueue = Queue()
        self.lock = Lock()
        self.users = []
        self.stocks = []
        self.accounts = {}
        return
    
    @staticmethod
    def getInstance():
        if StockBroker._instance is None:
            StockBroker._instance = StockBroker()
            return StockBroker._instance
        raise ValueError("Singleton Class")
    
    def addStock(self, stock):
        self.stocks.append(stock)
        return
    
    def addAccount(self, account):
        self.accounts[account.getID()] = account
        return
    
    def addUser(self, user):
        self.users.append(user)
        return
    
    def executeOrder(self, order):
        with self.lock:
            self.orderQueue.put(order)
            self.processOrders()
        return
    
    def processOrders(self):
        while not self.orderQueue.empty():
            order = self.orderQueue.get()
            try:
                print("Order Executing")
                order.execute()
            except Exception as e:
                print(f"Order failed: {str(e)}")
        return