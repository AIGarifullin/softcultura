FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -U pip && \
    pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

EXPOSE 5000
