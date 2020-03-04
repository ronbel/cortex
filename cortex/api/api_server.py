from flask import Flask, jsonify, make_response, send_file
from pymongo import MongoClient


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
        result = users.find_one({"user_id": id}, {"snapshots": 0, "_id": 0})
        if not result:
            return make_response('User not found\n', 404)
        return make_response(jsonify(result), 200)

    @server.route('/users/<int:id>/snapshots')
    def get_user_snapshots(id):
        result = users.find_one({"user_id": id}, {"snapshots.snapshot_id": 1, "snapshots.datetime": 1, "_id": 0})
        if not result:
            return make_response('User not found\n', 404)
        return make_response(jsonify(result['snapshots']), 200)
    
    @server.route('/users/<int:user_id>/snapshots/<int:snap_id>')
    def get_snapshot(user_id,snap_id):
        result = users.find_one({"user_id": user_id, "snapshots.snapshot_id": snap_id}, {"_id": 0, "snapshots": {"$elemMatch": {"snapshot_id": snap_id}} })
        if not result:
            return make_response('Snapshot not found\n', 404)

        snapshot = result['snapshots'][0]
        observations = [key for key in snapshot if key not in ['snapshot_id', 'datetime']]
        json_result = jsonify({'snapshot_id': snapshot['snapshot_id'], 'datetime': snapshot['datetime'], 'results': observations})

        return make_response(json_result, 200)

    @server.route('/users/<int:user_id>/snapshots/<int:snap_id>/<result_name>')
    def get_result(user_id, snap_id, result_name):
        query_result =  users.find_one({"user_id": user_id, "snapshots.snapshot_id": snap_id, f'snapshots.{result_name}': {"$exists": True}}, {"_id": 0, "snapshots": {"$elemMatch": {"snapshot_id": snap_id}} })
        if not query_result:
            return make_response('Snapshot result not found\n', 404)
        return make_response(jsonify(query_result['snapshots'][0][result_name]), 200)

    @server.route('/users/<int:user_id>/snapshots/<int:snap_id>/<result_name>/data')
    def get_result_data(user_id, snap_id, result_name):
        query_result =  users.find_one({"user_id": user_id, "snapshots.snapshot_id": snap_id, f'snapshots.{result_name}.data': {"$exists": True}}, {"_id": 0, "snapshots": {"$elemMatch": {"snapshot_id": snap_id}} })
        if not query_result:
            return make_response('Snapshot result not found or has no data\n', 404)
        return send_file(query_result['snapshots'][0][result_name]['data'])               


    server.run(host=host, port=port)
