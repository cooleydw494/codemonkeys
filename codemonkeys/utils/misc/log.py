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

    Attributes:
        _instance (Optional['Log']): The singleton instance of the Log class.

    Args:
        name (str): The name of the logger.
        level (int): The logging level, e.g., logging.INFO, logging.DEBUG.
        log_file_path (OStr): Full path where the log file will be stored.
        max_bytes (int): Maximum bytes a log file should have before being rotated.
        backup_count (int): How many backup files to keep.

    Note: Log uses the RotatingFileHandler for rotating logs after reaching max_bytes.

    Example:
        >>> Log.info('Application started')
        # Info message will be logged
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

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.info(message)

    @classmethod
    def error(cls, message: str):
        """
        Log an error level message.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.error(message)

    @classmethod
    def warning(cls, message: str):
        """
        Log a warning level message.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.warning(message)

    @classmethod
    def debug(cls, message: str):
        """
        Log a debug level message.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance()
        cls._instance.logger.debug(message)

    @classmethod
    def critical(cls, message: str):
        """
        Log a critical level message.

        :param message: The message to log.
        :type message: str
        """
        cls._get_instance().logger.critical(message)

    @classmethod
    def exception(cls, message: str):
        """
        Log an exception message and stack trace.

        :param message: The message associated with the exception.
        :type message: str
        """
        cls._get_instance().logger.exception(message)

    @classmethod
    def _get_instance(cls) -> 'Log':
        """
        Get or create the singleton instance of the Log class.

        :return: The singleton instance.
        :rtype: Log
        """
        cls._instance = cls._instance or cls()
        return cls._instance
