from flask import Flask, jsonify, make_response
from pymongo import MongoClient

DB_NAME = 'cortex-db'


def run_api_server(host='localhost', port='8000', database_url='mongodb://localhost:27017'):
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

    server.run(host=host, port=port, debug=True)


run_api_server()
