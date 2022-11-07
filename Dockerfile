FROM python:3.9-bullseye

ADD . /app
WORKDIR /app
COPY ./ /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r dev-requirements.txt
