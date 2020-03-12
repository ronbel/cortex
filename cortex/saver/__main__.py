import click
from . import Saver
from .mq_listeners import listeners
from furl import furl


@click.group()
def main():
    pass


@main.command('save')
@click.option('-d', '--database', default='mongodb://localhost:27017')
@click.argument('field')
@click.argument('result_path')
def save(field, result_path, database):
    saver = Saver(database)
    with open(result_path, 'r') as f:
        data = f.read()
        saver.save(data, field)


@main.command('run-saver')
@click.argument('database')
@click.argument('mq')
def run_service(database, mq):
    saver = Saver(database)

    mq = furl(mq)
    if mq.scheme not in listeners:
        raise Exception(f'No listener for the {mq.scheme} was found. Make sure it is defined and located in the mq_listeners package')
    listeners[mq.scheme](host=mq.host, port=mq.port, saver=saver)



if __name__ == '__main__':
    main()