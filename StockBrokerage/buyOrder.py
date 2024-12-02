from order import *

class BuyOrder(Order):
    def __init__(self, id, stock, account, quantity) -> None:
        super().__init__(id, stock, account, quantity)

    def execute(self):
        amount = self.stock.getPrice() * self.quantity
        currBalance = self.account.getBalance()
        if currBalance < amount:
            self.orderStatus = OrderStatus.FAILED
            raise ValueError("Balance is less!")
        self.account.depositBalance(amount)
        self.orderStatus = OrderStatus.EXECUTED
        return