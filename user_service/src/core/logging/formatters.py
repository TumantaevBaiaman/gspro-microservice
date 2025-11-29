CONSOLE_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> "
    "| <level>{level: <8}</level> "
    "| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> "
    "- <level>{message}</level>"
)

JSON_FORMAT = (
    '{{"time":"{time:YYYY-MM-DD HH:mm:ss}",'
    '"level":"{level}",'
    '"module":"{module}",'
    '"line":{line},'
    '"message":"{message}"}}'
)