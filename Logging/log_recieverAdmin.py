#!/usr/bin/env python
import pika
<<<<<<< HEAD
from pika import DeliveryMode
from pika.exchange_type import ExchangeType

credentials = pika.PlainCredentials('admin', '490Pass') #Put in your rabbitMQ user/pass here
parameters = pika.ConnectionParameters('10.147.20.15', 5672, 'testHost', credentials)
=======
from datetime import datetime
now = datetime.now()

credentials = pika.PlainCredentials('RedAdmin', '490Pass') #Put in your rabbitMQ user/pass here
parameters = pika.ConnectionParameters('10.147.20.57', 5672, 'testHost', credentials)
>>>>>>> 8ad3bb780f247f0284cfa360eaba6937d2a28b97
connection = pika.BlockingConnection(parameters)

channel=connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout',
 passive=False, durable=True, auto_delete=False)
 
<<<<<<< HEAD
queue = channel.queue_declare(queue='')
=======
queue = channel.queue_declare(queue='logging', durable=True)
>>>>>>> 8ad3bb780f247f0284cfa360eaba6937d2a28b97
queue_name = queue.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

def callback(ch, method, properties, body):
	print(f" [x] {body}") 
 
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()


