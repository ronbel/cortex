import click
from . import run_server


@click.group()
def main():
    pass

@main.command('run-server')
@click.option('-h', '--host', default='localhost')
@click.option('-p', '--port', default=8080)
@click.option('-H', '--api-host', default='localhost')
@click.option('-P', '--api-port', default=5000)
def start_gui(host, port, api_host, api_port):
    run_server(host=host,port=port,api_host=api_host, api_port=api_port)


if __name__ == '__main__':
    main()