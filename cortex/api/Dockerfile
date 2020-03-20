FROM cortex-base:latest

RUN mkdir api

ADD . /api

EXPOSE 5000

ENTRYPOINT ["python", "-m", "api", "run-server" ]

CMD ["-h", "0.0.0.0"]
