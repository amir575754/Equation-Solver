"""
Name: equation_solver_component.py

Purpose: Reads equations from the queue, solves them and pushed them to the db.

Usage: equation_solver_component.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

import pika
from timeit import default_timer as timer
from sympy import symbols, solve, Eq
from sqlite3 import Error as SQLiteError

from consts import RabbitMQConsts, EquationConsts
from equation_db_handler import EquationsDBHandler
from equation_utilities import pythonize_equation


def solve_equation(equation: str) -> list:
    """
    Receives an equation as a string.
    Returns all possible solutions to the equation in a list.
    """
    solution = []
    try:
        side1, side2 = equation.split(EquationConsts.SPLIT_CHARACTER)
        x = symbols(EquationConsts.SYMBOL)
        expression = Eq(eval(side1), eval(side2))
        solution = solve(expression)
    except ValueError as exception:
        print(f'A value error occurred: {exception}')
    except NameError as exception:
        print(f'A name error occurred: {exception}')
    except SyntaxError as exception:
        print(f'A syntax error occurred: {exception}')
    finally:
        return solution


def new_equation_callback(channel: pika.adapters.blocking_connection.BlockingChannel, method: pika.spec.Basic.Deliver,
                          properties: pika.spec.BasicProperties, body: bytes):
    """
    Called when a new equation is consumed from the line.
    """
    time_before_solving_equation = timer()
    equation = body.decode()
    final_equation = pythonize_equation(equation)
    solution = solve_equation(final_equation)
    time_to_solve_equation = timer() - time_before_solving_equation
    insert_equation_to_db(equation, solution, time_to_solve_equation)
    print(f'New Equation Solved: {equation} - {solution}')
    channel.basic_ack(delivery_tag=method.delivery_tag)


def insert_equation_to_db(original: str, solution: list, time: float):
    """
    Receives a new equation's details and inserts it to the DB.
    """
    try:
        db_handler = EquationsDBHandler()
        db_handler.insert_new_equation(original, solution.__str__(), time)
    except SQLiteError as exception:
        print(exception)


def declare_consuming_channel(broker_ip: str, exchange_name: str, exchange_type: str,
                              queue_name: str) -> pika.adapters.blocking_connection.BlockingChannel:
    """
    Returns a channel that can consume from the exchange at broker_ip
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_ip))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True)
    # Declare a queue that can only be accessed by the current connection, and can survive broker reboots.
    result = channel.queue_declare(queue=queue_name, durable=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=exchange_name, queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=new_equation_callback)
    return channel


def consume_equations():
    """
    Connects to the rabbit server and starts solving equations.
    After every equation solved, it pushed the result to a DB.
    """
    channel = declare_consuming_channel(RabbitMQConsts.BROKER_IP, RabbitMQConsts.EXCHANGE_NAME,
                                        RabbitMQConsts.EXCHANGE_TYPE, RabbitMQConsts.QUEUE_NAME)
    channel.start_consuming()
    try:
        pass
    except Exception as exception:
        print(f'{type(exception)}: {exception}')


def main():
    consume_equations()


if __name__ == '__main__':
    main()
