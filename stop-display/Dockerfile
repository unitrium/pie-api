FROM python:3.11-slim

COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false
RUN poetry install --compile
COPY src ./src

ENTRYPOINT poetry run gunicorn -b 0.0.0.0:8080 --workers 1 --threads 1 --timeout 0 src.api:app
EXPOSE 8080