FROM python:3.12-slim AS builder

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    curl \
    make \
    ca-certificates \
    && update-ca-certificates \
    && pip install --no-cache-dir poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./media_service/pyproject.toml ./media_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./media_service /app
COPY ./shared /shared

EXPOSE 50056
CMD ["python", "-u", "main.py"]