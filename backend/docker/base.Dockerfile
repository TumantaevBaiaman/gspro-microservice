FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    make \
    ca-certificates \
 && update-ca-certificates \
 && pip install poetry==1.8.3 \
    --default-timeout=300 \
    --retries=15 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
