FROM python:3

RUN pip install --no-cache-dir  pytest matplotlib pandas numpy seaborn
RUN mkdir /app
WORKDIR /app
COPY * .
