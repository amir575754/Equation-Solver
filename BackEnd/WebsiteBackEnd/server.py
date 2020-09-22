"""
Name: server.py

Purpose: This is the backend component of the equation solver project.

Usage: server.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

from flask import Flask
from flask.json import dumps
from flask_api import status
from sqlite3 import Error as SQLiteError

from consts import RabbitMQConsts
from rabbitmq_utilities import publish_message
from equations_db_handler import EquationsDBHandler

app = Flask(__name__)


def publish_equation(equation: str):
    """
    This function publishes the equation to the RabbitMQ Exchange
    for it be solved by the solver component later on.
    """
    try:
        publish_message(equation, RabbitMQConsts.BROKER_IP, RabbitMQConsts.EXCHANGE_NAME, RabbitMQConsts.EXCHANGE_TYPE)
    except Exception as exception:
        print(exception)


@app.route('/equations')
def equations_route():
    """
    Responsible for returning a json of all the dictionaries
    """
    equation_list = []
    try:
        db_handler = EquationsDBHandler()
        equation_list = db_handler.get_equations_json()
    except SQLiteError as exception:
        print(exception)
    finally:
        equation_response = app.make_response(dumps({'equations': equation_list}))
        equation_response.headers["Access-Control-Allow-Origin"] = "*"
        return equation_response


@app.route('/upload_equation/<equation>')
def upload_equation_route(equation: str):
    """
    Responsible for uploading a new equation to the equations rabbit queue.
    """
    publish_equation(equation)
    print(f'{equation} Published!')
    equation_response = app.make_response(("", status.HTTP_200_OK))
    equation_response.headers["Access-Control-Allow-Origin"] = "*"
    return equation_response


def main():
    app.run()


if __name__ == '__main__':
    main()
