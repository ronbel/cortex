from . import parser
import numpy as np
import matplotlib.pyplot as plt
import os
import json



@parser('depth_image')
def parse_depth_image(snapshot):
    with open(snapshot['depth_image']['data'], 'rb') as data_file:
        data = data_file.read()
        arr = np.frombuffer(data).reshape(snapshot['depth_image']['height'], snapshot['depth_image']['width'])
        plt.imshow(arr, cmap='hot')
        plt.savefig(f'{os.path.dirname(data_file.name)}/{snapshot["snapshot_id"]}_depth.png')
        snapshot['depth_image']['data'] = f'{os.path.dirname(data_file.name)}/{snapshot["snapshot_id"]}_depth.png'
        os.remove(os.path.abspath(data_file.name))
        return json.dumps({'user_info': snapshot['user_info'], 'snapshot_id': snapshot['snapshot_id'], 'depth_image': snapshot['depth_image']})