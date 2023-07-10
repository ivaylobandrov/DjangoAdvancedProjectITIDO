FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY poetry.lock pyproject.toml .env /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY app /app/

EXPOSE 8000
