from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def processPayment(self) -> None:
        pass