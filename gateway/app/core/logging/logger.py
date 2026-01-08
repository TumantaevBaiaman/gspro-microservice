from loguru import logger
import sys
from .formatters import CONSOLE_FORMAT, JSON_FORMAT


def setup_logger(env: str = "dev"):
    logger.remove()

    if env == "dev":
        logger.add(sys.stdout, format=CONSOLE_FORMAT, level="DEBUG")

    if env == "prod":
        logger.add("logs/app.json", format=JSON_FORMAT, rotation="10MB", retention="10 days", compression="zip")

    return logger


logger = setup_logger()

