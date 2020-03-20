FROM cortex-base:latest

RUN mkdir saver

ADD . /saver

ENTRYPOINT ["python", "-m", "saver", "run-saver"]

CMD ["mongodb://localhost:27017","rabbitmq://localhost:5672"]
