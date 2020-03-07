import click
from .client import upload_sample



@click.group()
def main():
    pass

@main.command('upload-sample')
@click.option('-h', '--host', default= 'localhost')
@click.option('-p', '--port', default= 8000)
@click.argument('path')
def sample(host, port, path):
    upload_sample(path=path, host=host, port=port)




if __name__ == '__main__':
    main()