FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk add --virtual build-deps musl-dev gcc && apk add --no-cache mariadb-dev
COPY requirements.txt .
RUN pip install -r requirements.txt && pip cache purge
RUN apk del --rdepends --purge build-deps musl-dev gcc
COPY . .
EXPOSE 8000