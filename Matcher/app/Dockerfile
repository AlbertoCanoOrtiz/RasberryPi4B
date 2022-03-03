FROM python:3.7-slim

WORKDIR /usr/src/api

COPY requirements.txt ./

RUN apt -y install libpq-dev python3.7-dev &&  pip3 install -r requirements \
  && rm -rf /root/.cache/pip

COPY . .

ENTRYPOINT['uvicorn','main:app','--host 0.0.0.0','--port 3000']