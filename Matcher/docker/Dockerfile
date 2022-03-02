FROM python:3.7-slim

WORKDIR /usr/src/api

COPY requirements.txt ./

RUN pip install -r requirements \
  && rm -rf /root/.cache/pip

