import pytest
from cortex.parsers import run_parser
import pathlib
import json


def test_feelings_parser():
    path_to_message = str(pathlib.Path(
        'tests/resources/example-message.json').absolute())
    message = json.load(open(path_to_message, 'r'))
    parsed_result = json.loads(run_parser('feelings', message))
    assert parsed_result is not None
    assert parsed_result['feelings']['happiness'] == 0.5
    assert parsed_result['feelings']['hunger'] == 0.4
    assert parsed_result['feelings']['thirst'] == 0.3
    assert parsed_result['feelings']['exhaustion'] == 0.2

def test_pose_parser():
    path_to_message = str(pathlib.Path(
        'tests/resources/example-message.json').absolute())
    message = json.load(open(path_to_message, 'r'))
    parsed_result = json.loads(run_parser('pose', message))
    assert parsed_result is not None
    assert parsed_result['pose']['translation']['x'] == parsed_result['pose']['translation']['y']
    assert parsed_result['pose']['translation']['z'] == 0.5
    assert parsed_result['pose']['rotation']['w'] == 0.4