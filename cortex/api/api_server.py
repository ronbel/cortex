from flask import Flask, jsonify, make_response
from pymongo import MongoClient
from .config import get_config

DB_NAME = 'cortex-db'


def run_api_server(host='localhost', port='5000', database_url='mongodb://localhost:27017'):
    server = Flask(__name__)
    db = MongoClient(database_url)[DB_NAME]
    users = db.users

    @server.route('/users')
    def get_users():
        return make_response(jsonify(list(users.find({}, {"_id": 0, "username": 1, "user_id": 1}))), 200)

    @server.route('/users/<int:id>')
    def get_specific_user(id):
        result = users.find_one({"user_id": str(id)}, {
                                "user_id": 1, "username": 1, "birthday": 1, "gender": 1, "_id": 0})
        if not result:
            return make_response('User not found\n', 404)
        return make_response(jsonify(result), 200)

    @server.route('/users/<int:id>/snapshots')
    def get_user_snapshots(id):
        result = users.find_one({"user_id": str(id)}, {"snapshots": {
                                "snapshot_id": 1, "datetime": 1}, "_id": 0})
        if not result:
            return make_response('User not found\n', 404)
        return make_response(jsonify(result.snapshots), 200)
    
    @server.route('/users/<int:user_id>/snapshots/<int:snap_id>')
    def get_snapshot(user_id,snap_id):
        result = users.find_one({"user_id": str(user_id), "snapshots": {"snapshot_id": snap_id}}, {"_id": 0, "snapshots":1 })
        if not result:
            return make_response('Snapshot not found\n', 404)
        return make_response(jsonify(result.snapshots[0]), 200)


    server.run(host=host, port=port)
