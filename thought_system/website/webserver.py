from flask import Flask, render_template
import pathlib


def format_timestamp_name(name):
    name = name.strip('.txt')
    split_name = name.split('_')
    split_name[1] = split_name[1].replace('-', ':')
    return ' '.join(split_name)


def run_webserver(address, data_path, debug=True):
    server = Flask(__name__)
    data_dir = pathlib.Path(data_path)

    @server.route('/')
    def index():
        user_list = [user_dir.name for user_dir in data_dir.iterdir()]
        return render_template('index.html', users=user_list)

    @server.route('/users/<int:id>')
    def user_page(id):
        user_path = data_dir / str(id)
        thoughts = []
        for file in user_path.iterdir():
            thoughts.extend([{'timestamp': format_timestamp_name(file.name.strip('.txt')), 'content': line} for line in
                             open(file).readlines()])
        return render_template('user-page.html', thoughts=thoughts)

    server.run(host=address[0], port=address[1], debug=debug)
