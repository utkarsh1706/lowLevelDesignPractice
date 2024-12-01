from logAppender import LogAppender

class FileAppender(LogAppender):
    
    def __init__(self, name) -> None:
        self.filename = name

    def append(self, logMessage):
        with open(self.filename, "a") as file:
            file.write(f"Message: {logMessage.message}, LogLevel: {logMessage.logLevel}")
        print(f"Added to DB: {logMessage.message} at timestamp:{logMessage.timestamp} of logLevel: {logMessage.logLevel}")
        return