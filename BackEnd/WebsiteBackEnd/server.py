"""
Name: server.py

Purpose: This is the backend component of the equation solver project.

Usage: server.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

from flask import Flask, Response
from consts import HTTPStatusCodes, ServerConsts

app = Flask(__name__)


@app.route('/upload_equation/<equation>')
def upload_equation_route(equation: str):
    """
    Responsible for uploading a new equation to the DB.
    """
    print(equation)
    equation_response = app.make_response(("Fine!", HTTPStatusCodes.OK))
    equation_response.headers["Access-Control-Allow-Origin"] = "*"
    return equation_response


def main():
    app.run()


if __name__ == '__main__':
    main()
