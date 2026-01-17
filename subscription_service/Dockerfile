FROM gspro-python-base AS builder

WORKDIR /app

COPY ./subscription_service/pyproject.toml ./subscription_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./subscription_service /app
COPY ./shared /shared

EXPOSE 50054
CMD ["python", "-u", "main.py"]