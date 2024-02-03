# syntax=docker/dockerfile:1
FROM python:3.9-slim

WORKDIR /flask_app

COPY . /flask_app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-u", "app.py"]