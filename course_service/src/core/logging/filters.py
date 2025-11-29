def exclude_health_checks(record):
    msg = record["message"]
    return "/health" not in msg and "/metrics" not in msg


def exclude_uvicorn(record):
    return "uvicorn" not in record["name"]
