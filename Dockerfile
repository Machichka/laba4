FROM python:3.11-slim

WORKDIR /workspace

# Встановлюємо залежності для компіляції (якщо будуть потрібні для asyncpg/psycopg)
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock* /workspace/

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

COPY . /workspace

EXPOSE 8000

# Запуск uvicorn з авторестартом та монтуванням папки (буде вказано в docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
