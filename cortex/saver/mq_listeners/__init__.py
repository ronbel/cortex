
from inspect import isclass, isfunction, getmembers
import pathlib
import importlib
import sys
import os


def listener(scheme):
    def decorator(f):
        f._scheme = scheme
        return f
    return decorator


listeners = {}

root = pathlib.Path(__path__[0]).absolute()
sys.path.insert(0, str(root.parent))
for path in root.iterdir():
    if path.name.startswith('_') or not path.suffix == '.py':
        continue
    _module = importlib.import_module(
        f'{root.name}.{path.stem}', package=root.name)
    available_listeners = {member[1]._scheme: member[1] for member in getmembers(
        _module, lambda x: (isfunction(x) or isclass(x)) and hasattr(x, '_scheme'))}
    listeners.update(available_listeners)
