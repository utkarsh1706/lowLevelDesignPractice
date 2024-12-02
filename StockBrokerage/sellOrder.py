from order import *

class SellOrder(Order):
    def __init__(self, id, stock, account, quantity) -> None:
        super().__init__(id, stock, account, quantity)

    def execute(self):
        amount = self.stock.getPrice() * self.quantity
        self.account.depositBalance(amount)
        self.orderStatus = OrderStatus.EXECUTED
        return