"""
Name: equation_solver_component.py

Purpose: Reads equations from the queue, solves them and pushed them to the db.

Usage: equation_solver_component.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""


import pika


def consume_equations():
    
