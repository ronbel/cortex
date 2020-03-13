import requests
import click
import json



@click.group()
def main():
    pass


@main.command('get-users')
@click.option('-h', '--host', default= 'localhost')
@click.option('-p', '--port', default= 5000)
def get_users(host,port):
    print(requests.get(f'http://{host}:{port}/users').json())


@main.command('get-user')
@click.option('-h', '--host', default= 'localhost')
@click.option('-p', '--port', default= 5000)
@click.argument('user_id')
def get_user(host,port, user_id):
    print(requests.get(f'http://{host}:{port}/users/{user_id}').json())

@main.command('get-snapshots')
@click.option('-h', '--host', default= 'localhost')
@click.option('-p', '--port', default= 5000)
@click.argument('user_id')
def get_snapshots(host,port, user_id):
    print(requests.get(f'http://{host}:{port}/users/{user_id}/snapshots').json())


@main.command('get-snapshot')
@click.option('-h', '--host', default= 'localhost')
@click.option('-p', '--port', default= 5000)
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(host,port, user_id, snapshot_id):
    print(requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}').json())

@main.command('get-result')
@click.option('-h', '--host', default= 'localhost')
@click.option('-p', '--port', default= 5000)
@click.option('-s', '--save')
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result')
def get_result(host,port, save, user_id, snapshot_id, result):
    query_result = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}').json()
    print(query_result)
    if save:
        with open(save, 'w') as f:
            try:
                f.write(json.dumps(query_result))
                print(f'Result saved to {save}')
            except:
                print('Save failed')



if __name__ == '__main__':
    main()