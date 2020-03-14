from . import parser
import json



@parser('feelings')
def parse_feelings(snap_json):
    return json.dumps({'user_info': snap['user_info'], 'snapshot_id': snap['snapshot_id'], 'feelings': snap['feelings']})