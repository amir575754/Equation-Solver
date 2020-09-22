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
    DB_SAVE_FILE = r'D:\EquationSolver\BackEnd\equations.db'
    EQUATIONS_TABLE_NAME = 'equations'
    CREATE_TABLE_TEMPLATE = 'CREATE TABLE {} (' \
                            'Original text NOT NULL, ' \
                            'Solution text NOT NULL, ' \
                            'Time real NOT NULL)'
    INSERT_EQUATION_TEMPLATE = 'INSERT INTO {} (' \
                               'Original, ' \
                               'Solution, ' \
                               'Time)' \
                               " VALUES ('{}', '{}', {})"
    QUERY_ALL_EQUATIONS = 'SELECT Original, Solution, Time FROM {}'


class EquationConsts:
    SYMBOL = 'x'
    SPLIT_CHARACTER = "="
