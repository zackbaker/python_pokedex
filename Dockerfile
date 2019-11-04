FROM python:3.8.0-buster
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt