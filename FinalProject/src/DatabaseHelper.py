'''
Created on 2014-03-25

@author: mo
'''
import mysql.connector
from mysql.connector import errorcode
from Statements import *

DATABASE_USER = 'cp363'
DATABASE_PASSWORD = 'cp363'
DATABASE_ADDRESS = '127.0.0.1'
DATABASE_NAME = 'CarCompany'
ERROR_CONNECTING = 'ERROR CONNECTING TO DATABASE'
ERROR_NO_DB = 'ERROR: DATABASE DOES NOT EXIST'
MESSAGE_CLOSED = "DATABASE CONNECTION WAS CLOSED"
MESSAGE_CONNECTED = "CONNECTED TO DATABASE"

def close(cnx):
    if cnx is not None:
        cnx.close()
        print(MESSAGE_CLOSED)
    return

def connect():
    try:
        cnx = mysql.connector.connect(user=DATABASE_USER,
                              password=DATABASE_PASSWORD,
                              host=DATABASE_ADDRESS,
                              database=DATABASE_NAME)
        print(MESSAGE_CONNECTED)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(ERROR_CONNECTING)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(ERROR_NO_DB)
        else:
            cnx.close()
        return None

def createTables(cnx):
    cursor = cnx.cursor()
    print("CREATING TABLES...")
    for name, ddl in TABLES.items():
        print()
        try:
            cursor.execute(ddl)
            print('CREATED TABLE: {}'.format(name))
        except mysql.connector.Error as err:
            print('ERROR CREATING TABLE: {} \nERR: {}'.format(name, err.msg))
    cursor.close()
    return

