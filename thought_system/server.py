import socket
import struct
import threading
from datetime import datetime
import time
import pathlib
from .utils import Listener
from . import Thought


class Handler(threading.Thread):
    lock = threading.Lock()

    def __init__(self, connection, data_dir):
        super().__init__()
        self.connection = connection
        self.data_dir = data_dir

    def run(self):
        full_msg = b''
        while True:
            curr = self.connection.receive(8)
            if len(curr) <= 0:
                self.connection.close()
                break
            full_msg += curr

        thought = Thought.deserialize(full_msg)

        self.lock.acquire()
        try:
            path = f'{self.data_dir}/{thought.user_id}'
            pathlib.PosixPath(path).mkdir(exist_ok=True, parents=True)
            try:
                all_msgs = open(f'{path}/{datetime.fromtimestamp(thought.timestamp):%Y-%m-%d_%H-%M-%S}.txt', 'r').read()
                all_msgs += '\n' + thought.thought
                open(f'{path}/{datetime.fromtimestamp(thought.timestamp):%Y-%m-%d_%H-%M-%S}.txt', 'w').write(all_msgs)
            except IOError:
                open(f'{path}/{datetime.fromtimestamp(thought.timestamp):%Y-%m-%d_%H-%M-%S}.txt', 'w').write(
                    thought.thought)

        finally:
            self.lock.release()


def run_server(address, data_dir):
    server = Listener(host=address[0], port=address[1])
    server.start()

    while True:
        conn = server.accept()
        handler = Handler(conn, data_dir)
        handler.start()
