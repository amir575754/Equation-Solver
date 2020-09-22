"""
Name: consts.py

Purpose: Housing the consts for the consumer

Usage: consts.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""


class RabbitMQConsts:
    BROKER_IP = "10.100.102.15"
    EXCHANGE_NAME = "equations"
    QUEUE_NAME = "equations_queue"
    EXCHANGE_TYPE = "fanout"


class DBConsts:
    DB_SAVE_FILE = r'D:\EquationSolver\BackEnd'
    SOLUTIONS_TABLE_NAME = 'solutions'
    CREATE_TABLE_TEMPLATE = 'CREATE TABLE {} (' \
                            'Original text NOT NULL, ' \
                            'Solution text NOT NULL, ' \
                            'Time text NOT NULL PRIMARY KEY, ' \
                            'Address text, ' \
                            'Email text)'


class EquationConsts:
    SYMBOL = 'x'
    SPLIT_CHARACTER = "="
