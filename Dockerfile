FROM python:3.8-alpine
COPY . /main
WORKDIR /main
RUN python3 main.py
