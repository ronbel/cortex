FROM nikolaik/python-nodejs:latest

COPY ./requirements.txt /

RUN pip install -r requirements.txt