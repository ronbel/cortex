FROM cortex-base:latest

RUN mkdir parsers

ADD . /parsers

ENTRYPOINT ["python", "-m", "parsers", "run-parser"]

