FROM python:3.13.3
COPY . /main
WORKDIR /main
RUN sh "python3 main.py"
