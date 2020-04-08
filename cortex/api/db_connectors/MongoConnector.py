from pymongo import MongoClient
from .import connector


@connector('mongodb')
class MongoConnector:
    """
    A connector class that interacts with MongoDB servers and provides an abstraction for queries
    Supported scheme: mongodb://
    """

    def __init__(self, db_url):
        client = MongoClient(db_url)
        db = client['cortex-db']
        self.users = db.users
        self.snapshots = db.snapshots

    def get_all_users(self):
        """
        Queries the database for a list of all the users

        :return: (list) A list of user documents 
        """
        return list(self.users.find({}, {"_id": 0, "username": 1, "user_id": 1}))

    def get_user(self, id):
        """
        Queries the database for a specific user

        :param id: The id of the desired user

        :return: (dict) A user document or None if user is not found
        """

        return self.users.find_one({"user_id": id}, {"_id": 0})

    def get_user_snapshots(self, user_id):
        """
        Queries the database for all the snapshots of a specific user

        :param user_id: The id of the desired user

        :return: (list) A list of snapshot documents
        """
        return list(self.snapshots.find({"by_user": user_id}, {"_id": 1, "datetime": 1}))

    def get_snapshot(self, user_id, snapshot_id):
        """
        Queries the database for a specific snapshot of a specific user

        :param user_id: The id of the desired user
        :param snapshot_id: The id of the desired snapshot

        :return: (dict) A snapshot document or None if snapshot is not found
        """

        snapshot = self.snapshots.find_one(
            {'_id': snapshot_id, 'by_user': user_id})
        if not snapshot:
            return None
        observations = [key for key in snapshot if key not in ['datetime']]
        return {'_id': snapshot['_id'], 'datetime': snapshot['datetime'], 'results': observations}

    def get_result(self, user_id, snapshot_id, result_name):
        """
        Gets a specific result's details from a specified snapshot by a specified user

        :param user_id: The id of the desired user
        :param snapshot_id: The id of the desired snapshot
        :param result_name: The name of the desired result

        :return: (dict) A result dict with all its fields or None if the snapshot or result are not found
        """
        snapshot = self.snapshots.find_one({'_id': snapshot_id, 'by_user': user_id, result_name: {
            "$exists": True}}, {'_id': 0, result_name: 1})
        if not snapshot:
            return None
        return snapshot[result_name]
