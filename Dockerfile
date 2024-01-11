FROM python:3.11-alpine as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.2.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin"

WORKDIR /usr/local/src/python-project-52/

COPY . .

RUN apk add --no-cache \
    curl

RUN curl -sSL https://install.python-poetry.org | python3 - && poetry --version

RUN poetry install

CMD poetry run python manage.py runserver 0.0.0.0:8000