from logAppender import LogAppender

class DBAppender(LogAppender):
    
    def __init__(self, name, password, username) -> None:
        self.dbname = name
        self.password = password
        self.username = username

    def append(self, logMessage):
        print(f"Added to DB: {logMessage.message} at timestamp:{logMessage.timestamp} of logLevel: {logMessage.logLevel}")
        return