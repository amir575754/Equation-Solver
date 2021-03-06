"""
Name: consts.py

Purpose: Housing the consts for the website backend

Usage: consts.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""


class RabbitMQConsts:
    BROKER_IP = "10.100.102.15"
    EXCHANGE_NAME = "equations"
    EXCHANGE_TYPE = "fanout"


class DBConsts:
    DB_SAVE_FILE = r'D:\EquationSolver\BackEnd\equations_history.db'
    EQUATIONS_TABLE_NAME = 'equations'
    CREATE_TABLE_TEMPLATE = 'CREATE TABLE {} (' \
                            'Original text NOT NULL, ' \
                            'Solution text NOT NULL, ' \
                            'Time real NOT NULL)'
    QUERY_ALL_EQUATIONS = 'SELECT Original, Solution, Time FROM {}'


class JSONConsts:
    ORIGINAL_KEY = 'original'
    SOLUTION_KEY = 'solution'
    TIME_KEY = 'time'
