import click
from . import run_parser, run_parser_service


@click.group()
def main():
    pass


@main.command('parse')
@click.argument('field')
@click.argument('data_path')
def parse(field, data_path):
    """
    Receives a field name and a path to a file with a message (as received from the message queue) and prints the parsed result
    """
    with open(data_path, 'r') as f:
        print(run_parser(field, f.read()))


@main.command('run-parser')
@click.argument('field')
@click.argument('mq_url')
def serve(field, mq_url):
    """
    Receives a field name and a url to a message queue (+scheme) and starts a service that listens to messages and sends back parsed data
    """
    run_parser_service(field, mq_url)


if __name__ == '__main__':
    main()