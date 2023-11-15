import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional

from codemonkeys.defs import STOR_PATH
from codemonkeys.types import OStr


class Log:
    """
    A centralized logger utility class.

    This class is a singleton that provides a global logging interface.
    It manages logs using the RotatingFileHandler to keep the log files within manageable sizes,
    automatically handles file rotation, and keeps a number of backup log files.

    Attributes:
        _instance (Optional['Log']): The singleton instance of the Log class.

    Args:
        name (str): The name of the logger.
        level (int): The logging level, e.g., logging.INFO, logging.DEBUG.
        log_file_path (OStr): Full path where the log file will be stored.
        max_bytes (int): Maximum bytes a log file should have before being rotated.
        backup_count (int): How many backup files to keep. Refer to logging.handlers.RotatingFileHandler for more details.

    Note: The Log class uses the RotatingFileHandler for rotating logs after reaching 'max_bytes'.

    Example:
        Set up the logger:
        >>> log = Log(name='my_app', level=logging.INFO)

        Log an information message:
        >>> Log.info('Application started')
        # This info message will be logged

    """
    _instance: Optional['Log'] = None

    def __init__(self, name: str = 'monkey-log', level: int = logging.INFO, log_file_path: OStr = None,
                 max_bytes: int = 10*1024*1024, backup_count: int = 5):
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        log_file_path = log_file_path or f'{STOR_PATH}/logs'
        os.makedirs(log_file_path, exist_ok=True)
        file_handler = RotatingFileHandler(f"{log_file_path}/{name}.log", maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    @classmethod
    def info(cls, message: str):
        """
        Log an info level message.

        This class method logs a message at the INFO level. It can be conveniently
        called using 'Log.info' without needing to instantiate the Log class.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.info(message)

    @classmethod
    def error(cls, message: str):
        """
        Log an error level message.

        This class method logs a message at the ERROR level. Similar to 'info',
        it can be used without directly instantiating the Log class.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.error(message)

    @classmethod
    def warning(cls, message: str):
        """
        Log a warning level message.

        Allows logging of warnings at the WARNING level. Like 'info' and 'error',
        it's accessed statically via the Log class.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.warning(message)

    @classmethod
    def debug(cls, message: str):
        """
        Log a debug level message.

        Logs messages at the DEBUG level to the log file, useful for detailed debugging
        information during development or troubleshooting.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.debug(message)

    @classmethod
    def critical(cls, message: str):
        """
        Log a critical level message.

        Logs a message at the CRITICAL level. Useful for logging events that represent
        serious errors that may lead to termination of the application.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.critical(message)

    @classmethod
    def exception(cls, message: str):
        """
        Log an exception message and stack trace.

        This method is for logging exception information along with a stack trace. It is
        equivalent to calling 'logger.error()' with the additional information provided by
        the exception.

        :param message: The message associated with the exception.
        :type message: str
        """
        cls._get_instance().logger.exception(message)

    @classmethod
    def _get_instance(cls) -> 'Log':
        """
        Get or create the singleton instance of the Log class.

        This utility method ensures that only one instance of the Log class exists.
        If an instance doesn't exist, it will be created.

        :return: The singleton instance.
        :rtype: Log
        """
        cls._instance = cls._instance or cls()
        return cls._instance
