from pymongo import MongoClient


class MongoSaver:

    def __init__(self, db_url):
        self.db = MongoClient(db_url)['cortex-db']
    
    def save(self, data, field):
        self.db.users.find_one_and_update({'user_id': data['user_info']['user_id']}, {'$set': {**data['user_info']}}, upsert = True)
        self.db.snapshots.find_one_and_update({'_id': data['snapshot_id']}, {'$set': {field: data[field], 'by_user': data['user_info']['user_id']}}, upsert=True)