"""
Name: backend_main.py

Purpose: This is the backend component of the equation solver project.

Usage: backend_main.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def main():
    app.run()


if __name__ == '__main__':
    main()
