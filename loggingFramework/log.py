from logLevel import LogLevel
import time

class Log:
    def __init__(self, loglevel: LogLevel, message) -> None:
        self.logLevel = loglevel
        self.message = message
        self.timestamp = int(time.time())