FROM gspro-python-base AS builder

WORKDIR /app

COPY ./chat_service/pyproject.toml ./chat_service/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./chat_service /app
COPY ./shared /shared

#RUN make proto

EXPOSE 50055
CMD ["python", "-u", "main.py"]