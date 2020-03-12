import click
from . import run_parser, run_parser_service


@click.group()
def main():
    pass


@main.command('parse')
@click.argument('field')
@click.argument('data_path')
def parse(field, data_path):
    with open(data_path, 'r') as f:
        print(run_parser(field, f.read()))


@main.command('run-parser')
@click.argument('field')
@click.argument('mq_url')
def serve(field, mq_url):
    run_parser_service(field, mq_url)


if __name__ == '__main__':
    main()