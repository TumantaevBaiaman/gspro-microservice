FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev curl make && \
    pip install --no-cache-dir poetry && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./gateway/pyproject.toml ./gateway/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./gateway /app
COPY ./shared /shared

#RUN make proto

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
