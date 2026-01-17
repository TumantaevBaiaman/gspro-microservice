FROM gspro-python-base AS builder

WORKDIR /app

COPY ./favorites_service/pyproject.toml ./favorites_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./favorites_service /app
COPY ./shared /shared

#RUN make proto

EXPOSE 50054
CMD ["python", "-u", "main.py"]