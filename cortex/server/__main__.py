import click
from . import run_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default='localhost')
@click.option('-p', '--port', default=8000)
@click.argument('mq')
def run(host,port,mq):
    run_server(host=host, port= port, mq_address=mq)


if __name__ == '__main__':
    main()
