FROM gspro-python-base AS builder

WORKDIR /app

COPY ./media_service/pyproject.toml ./media_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./media_service /app
COPY ./shared /shared

EXPOSE 50056
CMD ["python", "-u", "main.py"]