
from werkzeug.wrappers.response import Response
from cortex.client import upload_sample
from cortex_pb2 import Snapshot,User
from furl import furl
import requests
import pathlib


import pytest

def check_sample(req):
    binary = req.data
    user_len = int.from_bytes(binary[:4], 'little')
    user = User.FromString(binary[4:4+user_len])
    assert user.username == 'Ron Belkin'
    assert user.gender == 0
    assert user.birthday == 11111
    assert user.user_id == 24
    snapshot = Snapshot.FromString(binary[4+user_len:])
    assert snapshot.feelings.exhaustion == 0.30000001192092896
    assert snapshot.feelings.happiness == 0.949999988079071
    assert snapshot.feelings.thirst == 0.699999988079071
    assert snapshot.feelings.hunger == 0.20000000298023224
    assert snapshot.pose.rotation.x == 0.13
    assert snapshot.pose.rotation.y == 0.851
    return Response(response='OK', content_type='text/plain', status=200)
    
   
    

def test_upload_sample(httpserver):
    httpserver.expect_request("/snapshots/upload").respond_with_handler(check_sample)
    url = furl(httpserver.url_for("/snapshots/upload"))
    filepath = str(pathlib.Path('tests/resources/example.mind.gz').absolute())
    successful_uploads = upload_sample(filepath, host=url.host, port=url.port)
    assert successful_uploads == 1
    
    