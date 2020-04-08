
"""
This module is responsible for storing and collecting all the available parsers.
To add a parser function or callable class, use the @parser decorator
"""


from inspect import isclass, isfunction, getmembers
import pathlib
import importlib
import sys
import os


def parser(field):
    """
    The parser decorator. Decorate a function or a callable class with this and place it in the parser_agents folder and your parser will be available for use.

    By default, when a parser's parsing function is called, it is passed a snapshot message as recieved from the message queue


    :param field: The field name parsed by the parser
    """
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

    




    



