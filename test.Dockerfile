FROM python:3.9.2-slim-buster

RUN apt-get update -y && apt-get upgrade -y
RUN apt install dos2unix
WORKDIR /Code

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY src src
COPY test_pytest test_pytest
