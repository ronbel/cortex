from .parser_agents import parser_agents
from .mq_listeners import listeners
from inspect import isclass
import pika
from furl import furl

def run_parser(field, data):
    if field not in parser_agents:
        raise Exception(f'No parser that handles {field} was found. Make sure it is defined and place under the parser_agents package')
    callable_parser = parser_agents[field]() if isclass(
        parser_agents[field]) else parser_agents[field]
    return callable_parser(data)


def run_parser_service(field, mq_url):
    if field not in parser_agents:
        raise Exception(f'No parser that handles {field} was found. Make sure it is defined and place under the parser_agents package')

    callable_parser = parser_agents[field]() if isclass(
        parser_agents[field]) else parser_agents[field]

    mq = furl(mq_url)

    if mq.scheme not in listeners:
        raise Exception(f'No listener that handles the {mq.scheme} scheme was found. Make sure it is defined and place under the mq_listeners package')

    listeners[mq.scheme](host=mq.host,port=mq.port,parser=callable_parser)




