from flask import Flask, make_response, request
from .cortex_pb2 import User, Snapshot
from .file_saver import FileSaver
from .message_maker import JsonMessageMaker
import os
from furl import furl
import pika
import json
import uuid


def mq_connect(host, port):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
    channel = connection.channel()
    channel.exchange_declare(exchange='cortex', exchange_type='topic')
    return channel

def parse_data(binary):
    user_len = int.from_bytes(binary[:4], 'little')
    user = User.FromString(binary[4:4+user_len])
    snapshot = Snapshot.FromString(binary[4+user_len:])
    return (user, snapshot)


   

def run_server(publish ,host='localhost', port=8000 , *, mq_address='rabbitmq://localhost:5672'):
    server = Flask(__name__)
    file_saver = FileSaver(os.environ.get('SHARED_SAVE_PATH','/home/user/my_project/tmp'))
    message_maker = JsonMessageMaker(file_saver)

    mq_url = furl(mq_address)
    channel = mq_connect(mq_url.host, mq_url.port)

    
    @server.route('/snapshots/upload', methods=['POST'])
    def upload_snapshot():
        try:
            user, snapshot = parse_data(request.data)
        except:
            return make_response('Could not read data. Make sure it is in the following binary format: <user_len><serialized_user><serialized_snapshot>', 401)
        
        message = message_maker.make_message(user, snapshot)
        print(message)
        channel.basic_publish(exchange = 'cortex', routing_key = 'parse', body=message)
        return make_response('Ok', 200)

      


    server.run(host=host, port=port, threaded=True)
