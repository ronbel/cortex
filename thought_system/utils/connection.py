import socket


class Connection:
    @classmethod
    def connect(cls, ip, port):
        sock = socket.socket()
        sock.connect((ip, port))
        return cls(sock)

    def __init__(self, sock):
        self.sock = sock

    def __repr__(self):
        name = self.sock.getsockname()
        peer = self.sock.getpeername()
        return f'<Connection from {name[0]}:{name[1]} to {peer[0]}:{peer[1]}>'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def send(self, data):
        self.sock.sendall(bytes(data))

    def receive(self, size):
        try:
            data = b''
            while len(data) != size:
                new_data = self.sock.recv(size)
                if len(new_data) == 0:
                    break
                data += new_data
            if len(data) != size:
                raise Exception
            return data
        except Exception:
            raise

    def close(self):
        self.sock.close()
