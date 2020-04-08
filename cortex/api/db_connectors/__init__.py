
"""
This package contains all the connector classes to enable the API to connect to different databases
To add a connector to a new database, simply add a class to this folder and decorate it with @connector and your desired url scheme
"""


from inspect import isclass, isfunction, getmembers
import pathlib
import importlib
import sys
import os


def connector(scheme):
    """
    A decorator function to decorate classes that connect to a certain type of database.
    In case you want to use any database other than MongoDB, add a connector class similar to the given one, place it in the db_connectors subfolder and decorate it with this

    :param scheme: The URL scheme that corresponds to the database that is being used by the connector
    """
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

    




    



