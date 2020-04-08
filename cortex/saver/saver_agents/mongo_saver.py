from pymongo import MongoClient
from . import saver

@saver('mongodb')
class MongoSaver:
    """
    A saver that interacts with a MongoDB database
    """

    def __init__(self, db_url):
        self.db = MongoClient(db_url)['cortex-db']
    
    def save(self, data, field):
        """
        Saves the data of the given snapshot and the respective field.

        :param data: Parsed data dict as received from the parser of the respective field
        :param field: The field of the parser from which the data was received
        """
        self.db.users.find_one_and_update({'user_id': data['user_info']['user_id']}, {'$set': {**data['user_info']}}, upsert = True)
        self.db.snapshots.find_one_and_update({'_id': data['snapshot_id']}, {'$set': {field: data[field], 'by_user': data['user_info']['user_id']}}, upsert=True)