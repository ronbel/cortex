import click
from . import run_api_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host', default = 'localhost', help="The host of the REST API server")
@click.option('-p', '--port', default = '5000', help="The host of the REST API server")
@click.option('-d', '--database', default = 'mongodb://localhost:27017', help="The url (+scheme) of the database the API serves data from")
def run_api(host, port, database):
    """
    Runs the Cortex REST API server
    """
    run_api_server(host=host, port=port, database_url=database)


if __name__ == '__main__':
    main()
