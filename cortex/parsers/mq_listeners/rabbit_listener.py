from . import listener
import pika
import json

@listener('rabbitmq')
def rabbit_listener(host,port,parser):
    """
    A listener function that connects to a RabbitMQ server, listens to requests, parses them and publishes back a message with parsed data
    The listener uses the field to listen to the topic 'parse.#.<field>.#' for parse requests and publishes them back with the 'save.<field>' topic

    :param host: The host of the RabbitMQ server
    :param port: The port of the RabbitMQ server
    :param parser: A parser function or callable class, has a _field attribute that indicates which field it paarses
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host, port=port, retry_delay=10, connection_attempts=10))
    channel = connection.channel()

    channel.exchange_declare(exchange='cortex', exchange_type='topic')
    channel.queue_declare(parser._field)

    channel.queue_bind(
        exchange='cortex', queue=parser._field, routing_key=f'parse.#.{parser._field}.#')

    def callback(ch, method, properties, body):
        message = json.loads(body)
        print(f'Parsing {parser._field} for snapshot {message["snapshot_id"]}')
        channel.basic_publish(
            exchange='cortex', routing_key=f'save.{parser._field}', body=parser(message))
    
    channel.basic_consume(
    queue=parser._field, on_message_callback=callback, auto_ack=True)

    print(f'{parser._field} parser started listening')

    channel.start_consuming()