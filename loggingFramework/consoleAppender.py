from logAppender import LogAppender

class ConsoleAppender(LogAppender):
    def append(self, logMessage):
        print(f"Added to Console: {logMessage.message} at timestamp:{logMessage.timestamp} of logLevel: {logMessage.logLevel}")
        return