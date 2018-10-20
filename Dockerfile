FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y \
  gcc

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
