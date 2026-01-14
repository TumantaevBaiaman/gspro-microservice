FROM gspro-python-base AS builder

WORKDIR /app

COPY ./reviews_service/pyproject.toml ./reviews_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./reviews_service /app
COPY ./shared /shared

#RUN make proto

EXPOSE 50053
CMD ["python", "-u", "main.py"]