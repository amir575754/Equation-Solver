"""
Name: consts.py

Purpose: Housing the consts for the website backend

Usage: consts.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""


class RabbitMQConsts:
    SERVER_IP = "10.100.102.15"
    EXCHANGE_NAME = "equations"
    EXCHANGE_TYPE = "fanout"


class EquationConsts:
    SPLIT_CHARACTER = "="
