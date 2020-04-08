import click
from . import run_server


@click.group()
def main():
    """
    The GUI CLI
    """
    pass

@main.command('run-server')
@click.option('-h', '--host', default='localhost', help='The host of the GUI server')
@click.option('-p', '--port', default=8080, help="The port of the GUI server")
@click.option('-H', '--api-host', default='localhost', help="The host of a running instance of cortex.api")
@click.option('-P', '--api-port', default=5000, help="The port of a running instance of cortex.api")
def start_gui(host, port, api_host, api_port):
    """
    Starts a server that server the GUI
    """
    run_server(host=host,port=port,api_host=api_host, api_port=api_port)


if __name__ == '__main__':
    main()