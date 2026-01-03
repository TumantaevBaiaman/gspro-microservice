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

COPY ./chat_service/pyproject.toml ./chat_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./chat_service /app
COPY ./shared /shared

#RUN make proto

EXPOSE 50055
CMD ["python", "-u", "main.py"]