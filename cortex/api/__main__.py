import click
from . import run_api_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default = 'localhost')
@click.option('-p', '--port', default = '5000')
@click.option('-d', '--database', default = 'mongodb://localhost:27017')
def run_api(host, port, database):
    run_api_server(host=host, port=port, database_url=database)


if __name__ == '__main__':
    main()
