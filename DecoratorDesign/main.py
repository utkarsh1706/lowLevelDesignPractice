from Pizza import Pizza
from BasicPizza import BasicPizza
from PaneerPizza import PaneerPizza
from CheesePizza import CheesePizza
from pizzaDecorator import PizzaDecorator

class PizzaOrder:
    @staticmethod
    def run():
        pizza = BasicPizza()
        print(f"{pizza.getDescription()} - {pizza.getPrice()}")

        cheesePizza = CheesePizza(pizza)
        print(f"{cheesePizza.getDescription()} - {cheesePizza.getPrice()}")

        paneerPizza = PaneerPizza(cheesePizza)
        print(f"{paneerPizza.getDescription()} - {paneerPizza.getPrice()}")

if __name__=="__main__":
    PizzaOrder.run()