from .parser_agents import parser_agents
from .mq_listeners import listeners
from inspect import isclass
import pika
from furl import furl

def run_parser(field, data):
    """
    Runs the respective parser for the given field and data and returns the parsed result

    :param field: The field name to be parsed
    :param data: A snapshot message as received from the message queue (json format by default)
    :return: (dict) The parsed result
    """
    if field not in parser_agents:
        raise Exception(f'No parser that handles {field} was found. Make sure it is defined and place under the parser_agents package')
    callable_parser = parser_agents[field]() if isclass(
        parser_agents[field]) else parser_agents[field]
    return callable_parser(data)


def run_parser_service(field, mq_url):
    """
    Runs a parser service that listens to a message queue, parses incoming messages and publishes back a message with parsed data

    :param field: The field name to be parsed
    :param mq_url: The address of the message queue (+scheme) to connect and listen to. The MQ listener is determined by the scheme (see mq_listeners module)

    """
    if field not in parser_agents:
        raise Exception(f'No parser that handles {field} was found. Make sure it is defined and place under the parser_agents package')

    callable_parser = parser_agents[field]() if isclass(
        parser_agents[field]) else parser_agents[field]

    mq = furl(mq_url)

    if mq.scheme not in listeners:
        raise Exception(f'No listener that handles the {mq.scheme} scheme was found. Make sure it is defined and place under the mq_listeners package')

    listeners[mq.scheme](host=mq.host,port=mq.port,parser=callable_parser)




