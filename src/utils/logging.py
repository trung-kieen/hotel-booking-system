"""
Author: Nguyen Khac Trung Kien
"""
import logging

from utils.constants import APP_NAME, LOG_FILE

def setup_logger_config(name: str =APP_NAME , log_file: str = LOG_FILE):
    """
    Call in start project entry point to setup logger
    Usage:
    - logger.info("Application has started.")
    - logger.error("An error occurred: %s", e)
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file)

    # Log everything debug, info, error, etc to console
    console_handler.setLevel(logging.DEBUG)


    # Log error, critical to specific file
    file_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
