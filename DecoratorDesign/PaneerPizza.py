from pizzaDecorator import PizzaDecorator

class PaneerPizza(PizzaDecorator):
    def getDescription(self):
        return self._pizza.getDescription() + ", Paneer"
    
    def getPrice(self):
        return self._pizza.getPrice() + 100