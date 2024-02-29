FROM python:3.11.4-alpine

WORKDIR /usr/scr/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requiremnets.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/entrypoint.sh

