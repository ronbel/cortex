
import time
from .utils import Connection
from . import Thought


def upload_thought(address, user, thought):
    conn = Connection.connect(*address)

    new_thought = Thought(user, int(time.time()), thought)

    conn.send(new_thought.serialize())

    conn.close()



