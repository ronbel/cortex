from pymongo import MongoClient
from .import connector


@connector('mongodb')
class MongoConnector:

    def __init__(self, db_url):
        client = MongoClient(db_url)
        db = client['cortex-db']
        self.users = db.users
        self.snapshots = db.snapshots

    def get_all_users(self):
        return list(self.users.find({}, {"_id": 0, "username": 1, "user_id": 1}))

    def get_user(self, id):
        return self.users.find_one({"user_id": id}, {"_id": 0})

    def get_user_snapshots(self, user_id):
        return list(self.snapshots.find({"by_user": user_id}, {"_id": 1, "datetime": 1}))

    def get_snapshot(self, user_id, snapshot_id):
        snapshot = self.snapshots.find_one(
            {'_id': snapshot_id, 'by_user': user_id})
        if not snapshot:
            return None
        observations = [key for key in snapshot if key not in ['datetime']]
        return {'_id': snapshot['_id'], 'datetime': snapshot['datetime'], 'results': observations}

    def get_result(self, user_id, snapshot_id, result_name):
        snapshot = self.snapshots.find_one({'_id': snapshot_id, 'by_user': user_id, result_name: {
            "$exists": True}}, {'_id': 0, result_name: 1})
        if not snapshot:
            return None
        return snapshot[result_name]
