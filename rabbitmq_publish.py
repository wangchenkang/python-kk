#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.9.141'))
channel = connection.channel()
channel.exchange_declare(exchange='kk', type='fanout')
#channel.queue_declare(queue='kk', durable=True)
for i in xrange(2):
    channel.basic_publish(exchange='kk',routing_key='', properties=pika.BasicProperties(delivery_mode=2), body='hello world')
connection.close()
