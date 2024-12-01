from threading import Lock
from logLevel import LogLevel
from consoleAppender import ConsoleAppender
from loggerConfig import LoggerConfig
from log import Log

class LoggingFramework:
    _instance = None

    def __init__(self) -> None:
        if LoggingFramework._instance is not None:
            raise Exception("Singleton Class!")
        
        self.config = LoggerConfig(LogLevel.INFO, ConsoleAppender())
        self.lock = Lock()
        return
    
    @staticmethod
    def getInstance():
        if LoggingFramework._instance is None:
            LoggingFramework._instance = LoggingFramework()
        return LoggingFramework._instance
    
    def setConfig(self, config):
        self.config = config
        return
    
    def log(self, loglevel: LogLevel, message):
        if loglevel.value >= self.config.get_log_level().value:
            logMessage = Log(loglevel, message)
            self.config.get_log_appender().append(logMessage)
        return

    def debug(self, message):
        self.log(LogLevel.DEBUG, message)
    
    def info(self, message):
        self.log(LogLevel.INFO, message)
    
    def warning(self, message):
        self.log(LogLevel.WARNING, message)
    
    def error(self, message):
        self.log(LogLevel.ERROR, message)
    
    def fatal(self, message):
        self.log(LogLevel.FATAL, message)