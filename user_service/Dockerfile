FROM gspro-python-base AS builder

WORKDIR /app

COPY ./user_service/pyproject.toml ./user_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./user_service /app
COPY ./shared /shared

RUN make proto

EXPOSE 50051
CMD ["python", "main.py"]