from . import listener
import pika
import json

@listener('rabbitmq')
def rabbit_listener(host,port,parser):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host, port=port))
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