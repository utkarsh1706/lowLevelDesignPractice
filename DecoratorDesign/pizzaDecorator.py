from Pizza import Pizza

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def getPrice(self):
        return self._pizza.getPrice()

    def getDescription(self):
        return self._pizza.getDescription()
