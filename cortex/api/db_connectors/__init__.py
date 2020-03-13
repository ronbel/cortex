
from inspect import isclass, isfunction, getmembers
import pathlib
import importlib
import sys
import os


def connector(scheme):
    def decorator(connector):
        connector._scheme = scheme
        return connector
    return decorator


connectors={}

root = pathlib.Path(__path__[0]).absolute()
sys.path.insert(0, str(root.parent))
for path in root.iterdir():
    if path.name.startswith('_') or not path.suffix == '.py':
        continue
    _module = importlib.import_module(f'{root.name}.{path.stem}', package=root.name)
    available_connectors = {member[1]._scheme: member[1] for member in getmembers(_module, lambda x: isclass(x) and hasattr(x, '_scheme'))}
    connectors.update(available_connectors)

    




    



