from google.protobuf import json_format
import numpy as np
import uuid
import json

class JsonMessageMaker:
    def __init__(self, file_saver):
        self.file_saver = file_saver
    
    def make_message(self, user, snapshot):
        user_dict = json_format.MessageToDict(user, preserving_proto_field_name=True)
        user_dict['gender'] = user.gender

        snap_id = str(uuid.uuid4())

        snap_dict = json_format.MessageToDict(snapshot,  preserving_proto_field_name=True)

        snap_dict['color_image']['data'] = self.file_saver.save_file(f'{snap_id}_color.data', snapshot.color_image.data)
        snap_dict['depth_image']['data'] = self.file_saver.save_file(f'{snap_id}_depth.data', np.array(snapshot.depth_image.data,'float').tostring())

        return json.dumps({'user_info': user_dict, 'snapshot_id': snap_id, **snap_dict})
