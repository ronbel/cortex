FROM cortex-base:latest

RUN mkdir server

ADD . /server

EXPOSE 8000

ENTRYPOINT ["python", "-m", "server", "run-server"]

CMD ["-h", "0.0.0.0", "rabbitmq://localhost:5672"]

