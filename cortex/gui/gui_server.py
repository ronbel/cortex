from flask import Flask, render_template, jsonify,make_response
from flask_cors import CORS
import requests


def run_server(host='127.0.0.1', port=8080, api_host='localhost', api_port=5000):
    """ Initializes a server that serves the GUI and connects to a running instance of cortex.api

    :param host: The host on which the GUI should run
    :param port: The port on which the GUI should run
    :param api_host: The address of a running instance of cortex.api
    :param api_port: The port of a running instance of cortex.api 
    """
    app = Flask(__name__,
                static_folder="./cortex-gui/dist/",
                template_folder="./cortex-gui/dist")

    cors = CORS(app, resources={r"*": {"origins": "*"}})

    @app.route('/api/<path:path>')
    def api_call(path):
        if(path.endswith('data')):
            return make_response(jsonify(f'http://{api_host if api_host != "api" else "localhost"}:{api_port}/{path}'),200)
        return make_response(jsonify(requests.get(f'http://{api_host}:{api_port}/{path}').json()), 200)

    @app.route('/')
    @app.route('/about')
    @app.route('/users')
    def catch_all():
        return render_template('index.html')

    app.run(host=host, port=port) 

 