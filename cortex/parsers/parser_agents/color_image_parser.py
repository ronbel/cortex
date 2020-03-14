from PIL import Image
from . import parser
import json
import os


@parser('color_image')
def parse(snapshot):
    with open(snapshot['color_image']['data'], 'rb') as data_file:
        data = data_file.read()
        size = snapshot['color_image']['width'], snapshot['color_image']['height']
        image = Image.frombytes('RGB', size, data)
        image.save(
            f'{os.path.dirname(data_file.name)}/{snapshot["snapshot_id"]}_color.png')
        snapshot['color_image']['data'] = f'{os.path.dirname(data_file.name)}/{snapshot["snapshot_id"]}_color.png'
        os.remove(os.path.abspath(data_file.name))
        return json.dumps({'user_info': snapshot['user_info'], 'snapshot_id': snapshot['snapshot_id'], 'color_image': snapshot['color_image']})
