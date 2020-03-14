from . import parser
import json

@parser('pose')
def parse_pose(snap_json):
    return json.dumps({'user_info': snap['user_info'], 'snapshot_id': snap['snapshot_id'], 'pose': snap['pose']})
