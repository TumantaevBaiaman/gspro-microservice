from loguru import logger
import sys
from .formatters import CONSOLE_FORMAT, JSON_FORMAT
from .filters import exclude_health_checks


def setup_logger():
    logger.remove()

    # Console for dev
    logger.add(
        sys.stdout,
        format=CONSOLE_FORMAT,
        level="INFO",
        filter=exclude_health_checks,
        enqueue=True,
        backtrace=True,
        diagnose=True
    )

    # File JSON for prod
    logger.add(
        "logs/src.log",
        format=JSON_FORMAT,
        rotation="10 MB",
        retention="10 days",
        compression="zip",
        level="INFO",
        enqueue=True
    )

    return logger


logger = setup_logger()
