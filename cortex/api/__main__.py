import click
from . import run_api_server


@click.group()
def main():
    pass


@main.command('run-server')
@click.option('-h', '--host')
@click.option('-p', '--port')
@click.option('-d', '--database')
def run_api(host='localhost', port='5000',database='mongodb://localhost:27017'):
    run_api_server(host=host,port=port,database_url=database)



if __name__ == '__main__':
    main()
