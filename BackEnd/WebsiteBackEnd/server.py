"""
Name: server.py

Purpose: This is the backend component of the equation solver project.

Usage: server.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

from string import digits

import pika
from flask import Flask
from flask_api import status

from consts import EquationConsts, RabbitMQConsts

app = Flask(__name__)


def pythonize_expression(expression: str) -> str:
    """
    Replaces all power signs with the python power signs.
    Adds a '*' sign between x and its multiplier.
    Returns the result.
    """
    expression = expression.replace("^", "**")
    new_expression = ""
    for letter_index in range(len(expression) - 1):
        if expression[letter_index] in digits and expression[letter_index + 1] == 'x':
            new_expression += expression[letter_index] + "*"
        else:
            new_expression += expression[letter_index]
    new_expression += expression[-1]
    return new_expression


def pythonize_equation(equation: str) -> str:
    """
    Pythonizes the equation
    """
    sides = equation.split(EquationConsts.SPLIT_CHARACTER)
    return "=".join(list(map(lambda side: pythonize_expression(side), sides)))


def publish_equation(equation: str):
    """
    This function publishes the equation to the RabbitMQ Exchange
    for it be solved by the solver component later on.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RabbitMQConsts.SERVER_IP))
    channel = connection.channel()
    channel.exchange_declare(exchange=RabbitMQConsts.EXCHANGE_NAME, exchange_type=RabbitMQConsts.EXCHANGE_TYPE,
                             durable=True)
    channel.basic_publish(exchange=RabbitMQConsts.EXCHANGE_NAME, routing_key='', body=equation)
    print(f'Published {equation} to the exchange')
    connection.close()


@app.route('/upload_equation/<equation>')
def upload_equation_route(equation: str):
    """
    Responsible for uploading a new equation to the equations rabbit queue.
    """
    final_equation = pythonize_equation(equation)
    publish_equation(final_equation)
    equation_response = app.make_response(("", status.HTTP_200_OK))
    equation_response.headers["Access-Control-Allow-Origin"] = "*"
    return equation_response


def main():
    app.run()


if __name__ == '__main__':
    main()
