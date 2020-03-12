
from inspect import isclass, isfunction, getmembers
import pathlib
import importlib
import sys
import os


def parser(field):
    def decorator(parser):
        parser._field = field
        return parser
    return decorator


parser_agents={}

root = pathlib.Path(__path__[0]).absolute()
sys.path.insert(0, str(root.parent))
for path in root.iterdir():
    if path.name.startswith('_') or not path.suffix == '.py':
        continue
    _module = importlib.import_module(f'{root.name}.{path.stem}', package=root.name)
    available_parsers = {member[1]._field: member[1] for member in getmembers(_module, lambda x: (isfunction(x) or isclass(x)) and hasattr(x, '_field'))}
    parser_agents.update(available_parsers)

    




    


