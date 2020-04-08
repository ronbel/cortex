import pika
import json
from . import listener

@listener('rabbitmq')
def run_rabbit(host, port, saver):
    """
    A function that initalizes the saver service that listens to a RabbitMQ server.
    Listens to the 'saver' queue for 'save.*' topic by default, and upon receiving message saved the field (*) into the appropriate snapshot in the DB


    :param host: The host of the RabbitMQ server
    :param port: The port of the RabbitMQ server
    :param saver: An instance of the Saver class connecting to the appropriate DB
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host, port=port, retry_delay=10, connection_attempts=10))

    channel = connection.channel()

    channel.exchange_declare(exchange='cortex', exchange_type='topic')

    channel.queue_declare('saver')

    channel.queue_bind(
        exchange='cortex', queue='saver', routing_key='save.*')

    def callback(ch, method, properties, body):
        field = method.routing_key.split('.').pop()
        data = json.loads(body)
        print(f'Saving {field} for snapshot {data["snapshot_id"]}')
        saver.save(field = field, data= data)
    
    channel.basic_consume(
    queue='saver', on_message_callback=callback, auto_ack=True)

    print('Saver started listening to save messages')

    channel.start_consuming()
