FROM cortex-base:latest

RUN mkdir gui

ADD . /gui


EXPOSE 8080

ENTRYPOINT [ "python", "-m", "gui", "run-server"]

CMD [ "-h", "0.0.0.0" ]