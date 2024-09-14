FROM ubuntu:22.04

LABEL maintainer="tekrimon4ever@yandex.ru"
LABEL name="Ugrasu TimeTable to iCS"
LABEL description="Переводит расписание в формат файла ics"

ENV WEB_APP_HOST="127.0.0.1"
ENV WEB_APP_PORT="80"

COPY web ~/webapp
COPY requirements.txt ~/equirements.txt

EXPOSE 80/tcp
EXPOSE 80/udp

RUN ["apt", "update"]
RUN ["apt", "install", "python3.12.5"]
RUN ["pip", "install", "-r", "~/requirements.txt"]

ENTRYPOINT ["gunicorn", "--workers=2", "--bind=${WEB_APP_HOST}", "--port=${WEB_APP_PORT}}", "~/webapp/web:app"]

