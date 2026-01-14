FROM gspro-python-base AS builder

WORKDIR /app

COPY ./course_service/pyproject.toml ./course_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./course_service /app
COPY ./shared /shared

RUN make proto

EXPOSE 50052
CMD ["python", "-u", "main.py"]