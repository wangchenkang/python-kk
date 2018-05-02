#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pika
from multiprocessing import Process

process_list = list()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.9.141'))
channel = connection.channel()
channel.exchange_declare(exchange='kk', type='fanout')

result = channel.queue_declare(exclusive=True, durable=True)
queue_name = result.method.queue
channel.queue_bind(exchange='kk', queue=queue_name)

def callback(ch, method, properties, body):
    print ch, method, properties, body
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue_name, no_ack=False)
channel.start_consuming()
