"""
Name: equation_utilities.py

Purpose: Housing useful functions for parsing equations

Usage: equation_utilities.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

from string import digits

from consts import EquationConsts


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
