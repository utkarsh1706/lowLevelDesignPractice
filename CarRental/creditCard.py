from payment import Payment

class CreditCard(Payment):
    def processPayment(self) -> None:
        print("Processing payment using Credit Card... Payment Done!")