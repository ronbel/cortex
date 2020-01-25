
import time
import datetime
from .utils import Connection
from . import Thought


def upload_thought(address, user, thought):
    conn = Connection.connect(*address)

    new_thought = Thought(user, datetime.datetime.now(), thought)

    conn.send(new_thought.serialize())

    conn.close()
