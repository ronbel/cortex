import pytest
from cortex.saver import Saver
from cortex.saver.saver_agents import saver_agents
import json
import pathlib
from pymongo import MongoClient




def test_save(mongodb, monkeypatch):
    
    def mockinit(self, url):
        self.db = mongodb['cortex-db']

    monkeypatch.setattr(saver_agents['mongodb'], '__init__', mockinit)    

    saver = Saver('mongodb://localhost:27017')
    path_to_message = str(pathlib.Path('tests/resources/example-message.json').absolute())
    message = json.load(open(path_to_message, 'r'))
    saver.save(message, 'feelings')
    snapshot = mongodb['cortex-db'].snapshots.find_one({'_id': "123"})
    assert snapshot is not None
    assert snapshot['feelings'] is not None
    assert snapshot['feelings']['happiness'] == 0.5
    assert snapshot['feelings']['hunger'] == 0.4
    assert snapshot['feelings']['thirst'] == 0.3
    assert snapshot['feelings']['exhaustion'] == 0.2


def test_saver_error():
    with pytest.raises(Exception):
        saver = Saver('badscheme://localhost:27017')