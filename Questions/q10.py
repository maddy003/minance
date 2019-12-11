# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:04:28 2019

@author: MA073146
"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = 'EmployeeDeviceDetails.db'

    sql_create_db1 = """ CREATE TABLE IF NOT EXISTS EMPLOYEE_DETAILS (
         EMPLOYEE_ID     INT  PRIMARY KEY   NOT NULL UNIQUE ,
         F_NAME           TEXT    NOT NULL,
         L_NAME           TEXT    NOT NULL); """

    sql_create_db2 = """CREATE TABLE IF NOT EXISTS DEVICE_RELATIONSHIP (
         EMPLOYEE_ID INT NOT NULL,
         DEVICE_ID INT PRIMARY KEY NOT NULL UNIQUE,
         FOREIGN KEY(EMPLOYEE_ID) REFERENCES EMPLOYEE_DETAILS(EMPLOYEE_ID));"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_db1)

        # create tasks table
        create_table(conn, sql_create_db2)
    else:
        print("Error! cannot create the database connection.")

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())


main()
