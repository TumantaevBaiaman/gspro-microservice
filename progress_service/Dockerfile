FROM gspro-python-base AS builder

WORKDIR /app

COPY ./progress_service/pyproject.toml ./progress_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./progress_service /app
COPY ./shared /shared

EXPOSE 50054
CMD ["python", "-u", "main.py"]