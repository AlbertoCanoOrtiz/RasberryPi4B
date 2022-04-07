FROM python:3.7-slim

WORKDIR /usr/src/api

COPY requirements ./

RUN  apt-get update -y && apt-get install --yes --no-install-recommends \
  libpq-dev gcc g++ \
  && pip3 install -r requirements \
  && rm -rf /root/.cache/pip

COPY . .

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]