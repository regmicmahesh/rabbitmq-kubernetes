#!/usr/bin/env python
import pika, sys, os


RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [Receiver]-> %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    main()
