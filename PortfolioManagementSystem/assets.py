from abc import ABC, abstractmethod

class Assets(ABC):
    def __init__(self, name, quantity) -> None:
        self.name = name
        self.quantity = quantity

    @abstractmethod
    def getValue(self):
        pass