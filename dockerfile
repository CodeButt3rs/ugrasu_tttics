FROM ubuntu:22.04

LABEL maintainer="tekrimon4ever@yandex.ru"
LABEL name="Ugrasu TimeTable to iCS"
LABEL description="Переводит расписание в формат файла ics"

ENV WEB_APP_HOST="0.0.0.0"
ENV WEB_APP_PORT="80"

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR ~

COPY webapp .
COPY requirements.txt .

EXPOSE 80/tcp
EXPOSE 80/udp
RUN apt update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN yes | apt install python3.12
RUN yes | apt install python3-pip
RUN pip install ics requests flask gunicorn

CMD gunicorn --workers=2 --bind=$WEB_APP_HOST:$WEB_APP_PORT web:app

