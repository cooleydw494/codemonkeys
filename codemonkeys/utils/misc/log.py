import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional

from codemonkeys.defs import STOR_PATH
from codemonkeys.types import OStr


class Log:
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
        cls._get_instance().logger.info(message)

    @classmethod
    def error(cls, message: str):
        cls._get_instance().logger.error(message)

    @classmethod
    def warning(cls, message: str):
        cls._get_instance().logger.warning(message)

    @classmethod
    def debug(cls, message: str):
        cls._get_instance()
        cls._instance.logger.debug(message)

    @classmethod
    def critical(cls, message: str):
        cls._get_instance().logger.critical(message)

    @classmethod
    def exception(cls, message: str):
        cls._get_instance().logger.exception(message)

    @classmethod
    def _get_instance(cls) -> 'Log':
        cls._instance = cls._instance or cls()
        return cls._instance
