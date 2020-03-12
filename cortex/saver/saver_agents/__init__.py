
from inspect import isclass, isfunction, getmembers
import pathlib
import importlib
import sys
import os


def saver(scheme):
    def decorator(saver):
        saver._scheme = scheme
        return saver
    return decorator


saver_agents={}

root = pathlib.Path(__path__[0]).absolute()
sys.path.insert(0, str(root.parent))
for path in root.iterdir():
    if path.name.startswith('_') or not path.suffix == '.py':
        continue
    _module = importlib.import_module(f'{root.name}.{path.stem}', package=root.name)
    available_savers = {member[1]._scheme: member[1] for member in getmembers(_module, lambda x: isclass(x) and hasattr(x, '_scheme'))}
    saver_agents.update(available_savers)

    




    



