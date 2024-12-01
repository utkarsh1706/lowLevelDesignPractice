from abc import ABC, abstractmethod

class LogAppender(ABC):
    @abstractmethod
    def append(self, logMessage):
        pass