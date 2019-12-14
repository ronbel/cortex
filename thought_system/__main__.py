import click
from .client import upload_thought
from .server import run_server
from .website import run_webserver


def addr_string_to_tuple(addr):
    addr_param = addr.split(':')
    addr_param[1] = int(addr_param[1])
    return tuple(addr_param)


@click.group()
def main():
    pass


@main.command('upload-thought')
@click.argument('address', type=str)
@click.argument('user', type=int)
@click.argument('thought', type=str)
def send_thought(address, user, thought):
    click.echo(f'Uploading to {address} a thought by user {user}')
    addr_param = addr_string_to_tuple(address)
    upload_thought(addr_param, user, thought)


@main.command('serve')
@click.argument('address', type=str)
@click.argument('data_dir', type=str)
def serve(address, data_dir):
    click.echo(f'Starting a server on {address} which stores data in {data_dir}')
    addr_param = addr_string_to_tuple(address)
    run_server(addr_param, data_dir)


@main.command('serve-web')
@click.argument('address', type=str)
@click.argument('data_dir', type=str)
def serve_web(address, data_dir):
    click.echo(f'Starting a webserver on {address} which reads data from {data_dir}')
    addr_param = addr_string_to_tuple(address)
    run_webserver(addr_param, data_dir)


if __name__ == '__main__':
    main()
