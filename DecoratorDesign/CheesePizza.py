from pizzaDecorator import PizzaDecorator

class CheesePizza(PizzaDecorator):
    def getDescription(self):
        return self._pizza.getDescription() + ", Cheese"
    
    def getPrice(self):
        return self._pizza.getPrice() + 100