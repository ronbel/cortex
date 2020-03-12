import click
from . import MongoSaver, run_saver


@click.group()
def main():
    pass


@main.command('save')
@click.option('-d', '--database', default='mongodb://localhost:27017')
@click.argument('field')
@click.argument('result_path')
def save(field, result_path, database):
    saver = MongoSaver(database)
    with open(result_path, 'r') as f:
        data = f.read()
        saver.save(data, field)


@main.command('run-saver')
@click.argument('database')
@click.argument('mq')
def run_service(database, mq):
    saver = MongoSaver(database)
    run_saver(mq, saver)



if __name__ == '__main__':
    main()