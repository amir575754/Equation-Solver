"""
Name: rabbitmq_utilities.py.py

Purpose: Housing useful functions used to interact with the rabbit broker.

Usage: rabbitmq_utilities.py.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

import pika

from consts import RabbitMQConsts


def publish_message(message: str):
    """
    This function publishes the message to the RabbitMQ Exchange
    for it be solved by the solver component later on.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RabbitMQConsts.SERVER_IP))
    channel = connection.channel()
    channel.exchange_declare(exchange=RabbitMQConsts.EXCHANGE_NAME, exchange_type=RabbitMQConsts.EXCHANGE_TYPE,
                             durable=True)
    channel.basic_publish(exchange=RabbitMQConsts.EXCHANGE_NAME, routing_key='', body=message)
    print(f'Published {message} to the exchange')
    connection.close()
