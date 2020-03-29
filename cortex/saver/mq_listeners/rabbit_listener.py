import pika
import json
from . import listener

@listener('rabbitmq')
def run_rabbit(host, port, saver):
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
