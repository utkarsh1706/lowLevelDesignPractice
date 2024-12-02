from enum import Enum
import time

class OrderStatus(Enum):
    EXECUTED = 1
    FAILED = 2
    INPROCESS = 3

class Order:
    def __init__(self, id, stock, account, quantity) -> None:
        self.orderID = id
        self.stock = stock
        self.account = account
        self.quantity = quantity
        self.timestamp = int(time.time())
        self.orderStatus = OrderStatus.INPROCESS
        return
    
    def execute(self):
        pass