from google.protobuf import json_format
import numpy as np
import uuid
import json

class JsonMessageMaker:
    def __init__(self, file_saver):
        self.file_saver = file_saver
    
    def make_message(self, user, snapshot):
        user_dict = json_format.MessageToDict(user)
        user_dict['gender'] = user.gender

        snap_id = str(uuid.uuid4())

        snap_dict = json_format.MessageToDict(snapshot)

        snap_dict['colorImage']['data'] = self.file_saver.save_file(f'{snap_id}_color.raw', snapshot.color_image.data)
        snap_dict['depthImage']['data'] = self.file_saver.save_file(f'{snap_id}_depth.raw', np.array(snapshot.depth_image.data,'float').tostring())

        return json.dumps({'user_info': user_dict, 'snapshot_id': snap_id, **snap_dict})
