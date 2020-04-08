import click
from . import upload_sample



@click.group()
def main():
    pass

@main.command('upload-sample')
@click.option('-h', '--host', default= 'localhost', help="The host of the cortex.server endpoint")
@click.option('-p', '--port', default= 8000, help="The port of the cortex.server endpoint")
@click.argument('path')
def sample(host, port, path):
    """
    Uploads the snapshot in the given sample file to the server. Supports only .mind and .mind.gz files
    """
    upload_sample(path=path, host=host, port=port)




if __name__ == '__main__':
    main()