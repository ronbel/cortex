from .MindFileReader import MindFileReader as Reader
from .BaseReader import BaseReader
from .cortex_pb2 import User, Snapshot
import requests


def validate_user(binary_user):
    try:
        User.FromString(binary_user)
    except:
        raise


def validate_snapshot(binary_snapshot):
    try:
        Snapshot.FromString(binary_snapshot)
    except:
        raise


def upload_sample(path, host='127.0.0.1', port=8000, *,  reader=Reader):
    """
    Reads a sample file and uploads all the snapshots in it to the cortex.server instance

    :param path: The path to the sample file
    :param host: The host of the cortex.server instance
    :param port: The port of the cortex.server instance
    :param reader: An optional reader class in case you want to read from a differently formatted file. See BaseReader doc.
    """
    file_reader = reader(path)
    if not isinstance(file_reader, BaseReader):
        raise Exception(
            'Error: Bad reader provided, make sure you provide a reader class that extends BaseReader')

    
    user = file_reader.get_user_binary()
    validate_user(user)

    uploaded_snapshots_amount = 0
    for binary_snapshot in file_reader:
        try:
            validate_snapshot(binary_snapshot)
            user_len = int.to_bytes(len(user), 4, 'little')
            payload = user_len + user + binary_snapshot
            requests.post(f'http://{host}:{port}/snapshots/upload', data=payload,
                          headers={'Content-type': 'application/octet-stream'}).raise_for_status()
            uploaded_snapshots_amount+=1
        except:
            print('Error uploading snapshot')
    print(f'Successfully uploaded {uploaded_snapshots_amount} snapshots')
    return uploaded_snapshots_amount
