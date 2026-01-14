FROM gspro-python-base AS builder

WORKDIR /app

COPY ./gateway/pyproject.toml ./gateway/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./gateway /app
COPY ./shared /shared

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
