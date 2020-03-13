from flask import Flask, jsonify, make_response, send_file
from pymongo import MongoClient
from .db_connectors import connectors
from furl import furl


DB_NAME = 'cortex-db'


def run_api_server(host='localhost', port='5000', database_url='mongodb://localhost:27017'):
    server = Flask(__name__)
    db = furl(database_url)
    if db.scheme not in connectors:
        raise Exception(f'No connector for the {db.scheme} scheme was found. Make sure it is defined and located in the db_connectors package')

    connector = connectors[db.scheme](db_url = database_url)
 

    @server.route('/users')
    def get_users():
        return make_response(jsonify(connector.get_all_users()), 200)

    @server.route('/users/<int:id>')
    def get_specific_user(id):
        result = connector.get_user(id)
        if not result:
            return make_response('User not found\n', 404)
        return make_response(jsonify(result), 200)

    @server.route('/users/<int:id>/snapshots')
    def get_user_snapshots(id):
        result = connector.get_user_snapshots(id)
        if not result:
            return make_response('User not found\n', 404)
        return make_response(jsonify(result), 200)

    @server.route('/users/<int:user_id>/snapshots/<int:snap_id>')
    def get_snapshot(user_id, snap_id):
        result = connector.get_snapshot(user_id, snap_id)
        if not result:
            return make_response('Snapshot not found\n', 404)

        return make_response(jsonify(result), 200)

    @server.route('/users/<int:user_id>/snapshots/<int:snap_id>/<result_name>')
    def get_result(user_id, snap_id, result_name):
        result = connector.get_result(user_id, snap_id, result_name)
        if not result:
            return make_response('Snapshot result not found\n', 404)
        return make_response(jsonify(result), 200)

    @server.route('/users/<int:user_id>/snapshots/<int:snap_id>/<result_name>/data')
    def get_result_data(user_id, snap_id, result_name):
        result = connector.get_result(user_id, snap_id, result_name)
        if not result or 'data' not in result:
            return make_response('Snapshot result not found or has no data\n', 404)
        return send_file(result['data'])

    server.run(host=host, port=port)
