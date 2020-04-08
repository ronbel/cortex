import click
from . import run_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default='localhost', help="The host on which to run the server")
@click.option('-p', '--port', default=8000, help="The port on which to run the server")
@click.argument('mq')
def run(host,port,mq):
    """
    Starts a server on the given host and port. Receives a url to a RabbitMQ server (other message queues are supported only with the exported run_server function)
    """
    run_server(host=host, port= port, mq_address=mq)


if __name__ == '__main__':
    main()
