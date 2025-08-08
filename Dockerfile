FROM python:3.8-alpine
COPY . /main
WORKDIR /main
RUN pip install -r requirements.text
CMD python3 main.py
