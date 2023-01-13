FROM python:3.9-slim AS base

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get install make -y \
    && apt-get clean

FROM base AS app

WORKDIR /usr/warehouse-intexsoft-intership

COPY requirements.txt /usr/warehouse-intexsoft-intership/
RUN pip install -r requirements.txt

COPY .env alembic.ini entrypoint-celery.sh entrypoint-server.sh /usr/warehouse-intexsoft-intership/

COPY src /usr/warehouse-intexsoft-intership