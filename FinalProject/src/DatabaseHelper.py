'''
Created on 2014-03-25

@author: mo
'''
import datetime

from mysql.connector import errorcode
import mysql.connector
from Entities import *
from datetime import date
import Statements
import datetime


DATABASE_USER = 'cp363'
DATABASE_PASSWORD = 'cp363'
DATABASE_ADDRESS = '127.0.0.1'
DATABASE_NAME = 'CarCompany'
ERROR_CONNECTING = 'ERROR CONNECTING TO DATABASE'
ERROR_NO_DB = 'ERROR: DATABASE DOES NOT EXIST'
MESSAGE_CLOSED = "DATABASE CONNECTION WAS CLOSED"
MESSAGE_CONNECTED = "CONNECTED TO DATABASE"

# Connection functions
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
#Create Tables
def createTables(cnx):
    cursor = cnx.cursor()
    print("CHECKING TABLES...")
    for name, ddl in Statements.TABLES.items():
        try:
            cursor.execute(ddl)
            print('TABLE: {}..OK'.format(name))
        except mysql.connector.Error as err:
            print('ERROR CREATING TABLE: {} \nERR: {}'.format(name, err.msg))
    cursor.close()
    return

# add entities
def addCar(cnx, car, user):
    SQLDeleteInsertUpdate(cnx, Statements.INSERT['Cars'], car.toTuple())
    SQLDeleteInsertUpdate(cnx, Statements.INSERT['UpdateCars'], (user.getEmployee().getId(), car.getVin(), date.today(), 'Added Vehicle'))
    return
def addCustomer(cnx, customer, user):
    cust_id = SQLInsertGetId(cnx, Statements.INSERT['Customer'], customer.toTuple()[1:])
    if cust_id != -1:
        customer.setId(cust_id)
        SQLDeleteInsertUpdate(cnx, Statements.INSERT['HasCustomer'], (user.getEmployee().getId(), customer.getId(), date.today(), 'New Customer'))
    return
def addEmployee(cnx, newuser):
    employee = newuser.getEmployee()
    emp_id = SQLInsertGetId(cnx, Statements.INSERT['Employee'], employee.toTuple()[1:])
    if emp_id != -1:
        newuser.getEmployee().setId(emp_id)
        SQLDeleteInsertUpdate(cnx, Statements.INSERT['Login'], newuser.toTuple())
    return
def addExpense(cnx, ex, user):
    ex_id = SQLInsertGetId(cnx, Statements.INSERT['Expenses'], ex.toTuple()[1:])
    if ex_id != -1:
        ex.setId(ex_id)
        SQLDeleteInsertUpdate(cnx, Statements.INSERT['UpdateExpenses'], (ex.getId(), user.getEmployee().getId()))
    return

# remove entites
def removeEmployee(cnx, empid):
    SQLDeleteInsertUpdate(cnx, Statements.DELETE['Employee'], (empid,))
    return
def removeExpense(cnx, xid):
    SQLDeleteInsertUpdate(cnx, Statements.DELETE['Expenses'], (xid,))
    return
# get entities
def getAccount(cnx, u, p):
    r = SQLSelect(cnx, Statements.USER_LOGIN, (u, p))
    user = None
    for c in r:
        if len(c) == 7:
            e = Employee(c[0], c[1], c[2], c[3], c[4], c[5]==1, c[6])
            user = User(u, p, e)
    return user

# generic statement handlers
def SQLDeleteInsertUpdate(cnx, stmt, values):
    print(stmt)
    print(values)
    cursor = cnx.cursor()
    cursor.execute(stmt, values)
    cnx.commit()
    cursor.close()
    return
def SQLInsertGetId(cnx, stmt, values):
    print(stmt)
    print(values)
    cursor = cnx.cursor()
    cursor.execute(stmt, values)
    i = cursor.lastrowid
    cnx.commit()
    cursor.close()
    return i
def SQLSelect(cnx, stmt, values, header=False):
    cursor = cnx.cursor()
    cursor.execute(stmt, values)
    result = []
    if header:
        result.append(cursor.column_names)
    for c in cursor:
        row = []
        for d in c:
            row.append(d)
        result.append(row)
    cursor.close
    return result
