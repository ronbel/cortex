import struct
import datetime

HEADER_SIZE = 20


def deserial(bytes):
    header = struct.unpack('qqcxxx', bytes[:HEADER_SIZE])
    return Thought(header[0], datetime.datetime.fromtimestamp(header[1]), bytes[HEADER_SIZE:].decode('utf-8'))


class Thought:
    deserialize = deserial

    def __init__(self, user_id, timestamp, thoguht):
        self.user_id = user_id
        self.timestamp = timestamp
        self.thought = thoguht

    def __eq__(self, other):
        if not isinstance(other, Thought):
            return NotImplemented
        return self.user_id == other.user_id and self.timestamp == other.timestamp and self.thought == other.thought

    def __repr__(self):
        return f'Thought(user_id={self.user_id!r}, timestamp={self.timestamp!r}, thought={self.thought!r})'

    def __str__(self):
        return f'[{self.timestamp:%Y-%m-%d %H:%M:%S}] user {self.user_id}: {self.thought}'

    def serialize(self):
        return (struct.pack('qqcxxx', self.user_id, int(self.timestamp.timestamp()), b'\n') + bytes(
            self.thought,
            'utf-8'))
