FROM python:latest

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y chromium

RUN apt-get update && apt-get install -y curl build-essential file git

