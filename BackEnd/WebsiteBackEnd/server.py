"""
Name: server.py

Purpose: This is the backend component of the equation solver project.

Usage: server.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

from string import digits

from flask import Flask
from flask_api import status

from consts import EquationConsts, RabbitMQConsts
from rabbitmq_utilities import publish_message

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
    try:
        publish_message(equation, RabbitMQConsts.BROKER_IP, RabbitMQConsts.EXCHANGE_NAME, RabbitMQConsts.EXCHANGE_TYPE)
    except RuntimeError as exception:
        print(exception)


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
