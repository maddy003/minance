# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:04:28 2019

@author: MA073146
"""

import sqlite3

def make_conn():
    conn = sqlite3.connect('EmployeeDevice.db')
    print ("Opened database successfully")
    conn.execute('''CREATE TABLE COMPANY
         (EMPLOYEE_ID    INT     NOT NULL,
         FNAME           TEXT    NOT NULL,
         LNAME           TEXT     NOT NULL,
         DEVICE_ID INT PRIMARY KEY NOT NULL);''')
    conn.close()
    
    
    
make_conn()










