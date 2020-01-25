from .connection import Connection
import socket


class Listener:
    def __init__(self, port, host='0.0.0.0', backlog=1000, reuseaddr=True):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.reuseaddr = reuseaddr

        self.sock = socket.socket()
        if reuseaddr:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        address = (host, port)
        self.sock.bind(address)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def __repr__(self):
        return f'Listener(port={self.port!r}, host={self.host!r}, backlog={self.backlog}, reuseaddr={self.reuseaddr})'

    def start(self):
        self.sock.listen(self.backlog)

    def stop(self):
        self.sock.close()

    def accept(self):
        conn, addr = self.sock.accept()
        return Connection(conn)
