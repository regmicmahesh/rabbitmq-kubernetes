#!/usr/bin/env python

import pika
import time
import os

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))


channel = connection.channel()
channel.queue_declare(queue='hello')
i = 0
while True:
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World ' + str(i))
    print("[Sender]-> Sent " + str(i) )
    i += 1
    time.sleep(5)

connection.close()
