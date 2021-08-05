FROM python:3.9.2-slim-buster

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /Code

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY tests tests
COPY src src