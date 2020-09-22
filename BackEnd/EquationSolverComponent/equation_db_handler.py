"""
Name: equation_db_handler.py

Purpose: Housing the EquationDBHandler class

Usage: equation_db_handler.py

Author: Amir Schreiber

Change Log:
    22/9/20 - Created
"""

import sqlite3
from sqlite3 import DatabaseError, ProgrammingError, OperationalError, IntegrityError
from sqlite3 import Error as SQLiteError

from consts import DBConsts


class EquationsDBHandler(object):
    """
    This class represents an object that helps the user manage the equations DB.
    """

    def __init__(self, db_file: str = None):
        """
        May raise an sqlite3.Error error if a problem occurs when connecting to the DB.
        """
        self.db_file = DBConsts.DB_SAVE_FILE if db_file is None else None
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
        except DatabaseError as exception:
            raise SQLiteError(f'A database error occurred when connecting to the DB: {exception}')
        except OperationalError as exception:
            raise SQLiteError(
                f'An operational error occurred when connecting to the DB: {exception}')

    def initialize_equations_table(self):
        """
        This function creates an empty equation table in the equations database.
        """
        table_initialize_query = DBConsts.CREATE_TABLE_TEMPLATE.format(DBConsts.EQUATIONS_TABLE_NAME)
        try:
            self.cursor.execute(table_initialize_query)
        except ProgrammingError:
            raise SQLiteError(
                f'A programming error occurred when creating the contacts table: {table_initialize_query}')
        except DatabaseError as exception:
            raise SQLiteError(f'A database error occurred when creating the contacts table: {exception}')
        except OperationalError as exception:
            raise SQLiteError(
                f'An operational error occurred when creating the contacts table: {exception}')

    def close(self):
        """
        May Raise a Database Error if an error occurred when closing the database or the cursor.
        """
        try:
            self.cursor.close()
            self.connection.close()
        except OperationalError as exception:
            raise SQLiteError(f'An operation error occurred when closing the connection\\cursor: {exception}')

    def insert_new_equation(self, original: str, solution: str, time: float):
        """
        Receives a new equation's details and inserts it to the table.

        May Raise a SQLiteError if the contact's number already exists.
        May raise a SQLiteError if there was an error with the SQL query.
        May raise a SQLiteError if there was an error with the database when inserting the data.
        """
        insert_query = DBConsts.INSERT_EQUATION_TEMPLATE.format(DBConsts.EQUATIONS_TABLE_NAME, original, solution, time)
        try:
            self.cursor.execute(insert_query)
            self.connection.commit()
        except ProgrammingError:
            raise SQLiteError(f'A programming error occurred when inserting the new equation: {insert_query}')
        except IntegrityError as exception:
            # If this error occurred, we know it's because there's already a contact with that number.
            raise SQLiteError(
                f'An integrity error occurred when inserting the new equation: {exception}')
        except DatabaseError as exception:
            raise SQLiteError(f'A database error occurred when inserting the new equation: {exception}')

    def query_all_equations(self) -> list:
        """
        Returns a list of tuples of all equations
        """
        query = DBConsts.QUERY_ALL_EQUATIONS.format(DBConsts.EQUATIONS_TABLE_NAME)
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return [] if results is None else results
        except ProgrammingError:
            raise SQLiteError(f'A programming error occurred when querying the DB: {query}')
        except IntegrityError as exception:
            raise SQLiteError(
                f'An integrity error occurred when querying the DB: {exception}')
        except DatabaseError as exception:
            raise SQLiteError(f'A database error occurred when querying the DB: {exception}')
