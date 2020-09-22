"""
Name: rabbitmq_utilities.py.py

Purpose: Housing useful functions used to interact with the rabbit broker.

Usage: rabbitmq_utilities.py.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

import pika


def publish_message(message: str, broker_ip: str, exchange_name: str, exchange_type: str):
    """
    This function publishes the message to the RabbitMQ Exchange located
    at the rabbit broker provided.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=broker_ip))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True)
    channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
    print(f'Published {message} to the exchange')
    connection.close()
