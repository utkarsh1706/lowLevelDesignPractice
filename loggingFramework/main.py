from LoggingFramework import LoggingFramework
from loggerConfig import LoggerConfig
from logLevel import LogLevel
from fileAppender import FileAppender

class LoggingFrameworkDemo:
    @staticmethod
    def run():
        logger = LoggingFramework.getInstance()
        
        logger.info("This is an information message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        
        config = LoggerConfig(LogLevel.DEBUG, FileAppender("app.log"))
        logger.setConfig(config)
        
        logger.debug("This is a debug message")
        logger.info("This is an information message")

if __name__ == "__main__":
    LoggingFrameworkDemo.run()