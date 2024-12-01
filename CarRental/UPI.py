from payment import Payment

class UPI(Payment):
    def processPayment(self) -> None:
        print("Processing payment using UPI... Payment Done!")