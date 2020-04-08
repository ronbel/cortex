import click
from . import Saver
from .mq_listeners import listeners
from furl import furl


@click.group()
def main():
    pass


@main.command('save')
@click.option('-d', '--database', default='mongodb://localhost:27017', help="The url (+scheme) of the database to save the result in")
@click.argument('field')
@click.argument('result_path')
def save(field, result_path, database):
    """
    Receives a path to a result message (as received from a parser) file and a field name, saves the result to the specified database
    """
    saver = Saver(database)
    with open(result_path, 'r') as f:
        data = f.read()
        saver.save(data, field)


@main.command('run-saver')
@click.argument('database')
@click.argument('mq')
def run_service(database, mq):
    """
    Receives urls (+scheme) to a database and a message queue and runs the saver service, which listens to the queue and saves message to the database
    """
    saver = Saver(database)

    mq = furl(mq)
    if mq.scheme not in listeners:
        raise Exception(f'No listener for the {mq.scheme} was found. Make sure it is defined and located in the mq_listeners package')
    listeners[mq.scheme](host=mq.host, port=mq.port, saver=saver)



if __name__ == '__main__':
    main()