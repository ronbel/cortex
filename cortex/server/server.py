from flask import Flask, make_response, request
from .cortex_pb2 import User, Snapshot
from .file_saver import BinaryFileSaver
from .message_maker import JsonMessageMaker
import os
from furl import furl
import pika
import json
import uuid


def parse_data(binary):
    user_len = int.from_bytes(binary[:4], 'little')
    user = User.FromString(binary[4:4+user_len])
    snapshot = Snapshot.FromString(binary[4+user_len:])
    return (user, snapshot)


def default_publish(user, snapshot):
    """
    The default publish function, the formats the user and the snapshot into a JSON message and publishes it to RabbitMQ
    The messages are published to the queue with the topic 'parse.<all the fields of the snapshot>

    :param user: A User instance, as specified in cortex.proto
    :param snapshot: A Snapshot instance, as specified in cortex.proto
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=globals()['mq_host'], port=globals()['mq_port']))
    channel = connection.channel()

    channel.exchange_declare(exchange='cortex', exchange_type='topic')

    file_saver = BinaryFileSaver(os.environ.get(
        'SHARED_SAVE_PATH', '/home/user/Cortex'))
    message_maker = JsonMessageMaker(file_saver)

    message = message_maker.make_message(user, snapshot)
    routing_key = f'parse.{".".join([field[0].name for field in snapshot.ListFields() if field[0].name != "datetime"])}'
    channel.basic_publish(
        exchange='cortex', routing_key=routing_key, body=message)
    
    snapshot_id , user_info = ((x := json.loads(message))['snapshot_id'], x['user_info'])

    channel.basic_publish(
        exchange='cortex', routing_key='save.datetime', body=json.dumps({'user_info': user_info, 'snapshot_id': snapshot_id, 'datetime': snapshot.datetime}))


    connection.close()


def run_server(host='localhost', port=8000, publish=default_publish, *, mq_address='rabbitmq://localhost:5672'):
    """
    Starts a server that listens to client requests and publish them to a message queue
    The server receives messages in the following format:
    <user_length, 4 bytes><serialized_user, user_length bytes><serialized_snapshot, the rest of the message>

    :param host: The host of the server
    :param port: The port of the server
    :param publish: A custom publish function. The function will be called with user and snapshot params, which are the respective class instances as specified in cortex.proto.

    """
    server = Flask(__name__)
    mq_url = furl(mq_address)

    if mq_url.scheme != 'rabbitmq':
        raise Exception('The server CLI supports only message queues with the rabbitmq scheme. If you wish to use another message queue, create your own publish function and pass it through the API (see documentation)')

    globals()['mq_host'] = mq_url.host
    globals()['mq_port'] = mq_url.port

    @server.route('/snapshots/upload', methods=['POST'])
    def upload_snapshot():
        try:
            user, snapshot = parse_data(request.data)
        except:
            return make_response('Could not read data. Make sure it is in the following binary format: <user_len><serialized_user><serialized_snapshot>', 401)

        publish(user, snapshot)
        return make_response('Ok', 200)

    server.run(host=host, port=port, threaded=True)
