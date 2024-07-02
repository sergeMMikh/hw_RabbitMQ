#!/usr/bin/env python
import pika, sys, os


def main():
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    credentials = pika.PlainCredentials('test', 'test')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        while True:
            try:
                main()
            except KeyboardInterrupt:
                print('Interrupted')
                sys.exit(0)
            except Exception as e:
                print(f'An error occurred: {e}')
    except SystemExit:
        os._exit(0)
        
