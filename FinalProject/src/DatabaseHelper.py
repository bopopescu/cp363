'''
Created on 2014-03-25

@author: mo
'''

from mysql.connector import errorcode
import mysql.connector
from Entities import *
from datetime import date
import Statements


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
def addCar(cnx, car, supplier, user):
    SQLDeleteInsertUpdate(cnx, Statements.INSERT['Cars'], car.toTuple())
    SQLDeleteInsertUpdate(cnx, Statements.INSERT['UpdateCars'], (user.getEmployee().getId(), car.getVin(), date.today(), 'Added Vehicle'))
    SQLDeleteInsertUpdate(cnx, Statements.INSERT['CarSupply'], ( supplier.getId(),car.getVin(), date.today()))
    
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
def addSupplier(cnx, supplier,date, user):
    sup_id = SQLInsertGetId(cnx, Statements.INSERT['Suppliers'], supplier.toTuple()[1:])
    if sup_id != -1:
        supplier.setId(sup_id)
        SQLDeleteInsertUpdate(cnx, Statements.INSERT['WorksWith'], (user.getEmployee().getId(), supplier.getId(), date))
    return

# remove entites
def removeEmployee(cnx, empid):
    SQLDeleteInsertUpdate(cnx, Statements.DELETE['Employee'], (empid,))
    return
def removeExpense(cnx, xid):
    SQLDeleteInsertUpdate(cnx, Statements.DELETE['UpdateExpenses'], (xid,))
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
def getCar(cnx, vin):
    r = SQLSelect(cnx, Statements.SELECT['Cars'], (vin,))
    for i in range(len(r)):
        if len(r[i]) == 7:
            r[i] = Car(r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], r[i][5]==1, r[i][6])
    return r
def getCustomer(cnx, cid):
    r = SQLSelect(cnx, Statements.SELECT['Customer'], (cid,))
    for i in range(len(r)):
        if len(r[i]) == 4:
            r[i] = Customer(r[i][0], r[i][1], r[i][2], r[i][3])
    return r
# searches
def searchCars(cnx, query):
    # wild card search to increase number of records
    query = '%' + query + '%'
    params = 3
    q = tuple([query for i in range(params)])
    r = SQLSelect(cnx, Statements.SEARCH['Cars'], q)
    for i in range(len(r)):
        if len(r[i]) == 7:
            r[i] = Car(r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], r[i][5]==1, r[i][6])
    return r
def searchEmployees(cnx, query):
    # wild card search to increase number of records
    query = '%' + query + '%'
    r = SQLSelect(cnx, Statements.SEARCH['Employee'], (query,))
    for i in range(len(r)):
        if len(r[i]) == 7:
            r[i] = Employee(r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], r[i][5]==1, r[i][6])
    return r
def searchExpenses(cnx, query):
    # wild card search to increase number of records
    query = '%' + query + '%'
    params = 2
    q = tuple([query for i in range(params)])
    r = SQLSelect(cnx, Statements.SEARCH['Expenses'], q)
    for i in range(len(r)):
        if len(r[i]) == 4:
            r[i] = Expense(r[i][0], r[i][1], r[i][2], r[i][3])
    return r
def searchSales(cnx, query):
    # wild card search to increase number of records
    query = '%' + query + '%'
    r = SQLSelect(cnx, Statements.SEARCH['CustomerPurchases'], (query,))
    for i in range(len(r)):
        cust = getCustomer(cnx, r[i][0])
        car = getCar(cnx, r[i][1])
        if len(cust) == 1 and len(car) == 1:
            r[i] = Sale(cust[0], car[0])
    return r
def searchSuppliers(cnx, query):
    # wild card search to increase number of records
    query = '%' + query + '%'
    r = SQLSelect(cnx, Statements.SEARCH['Suppliers'], (query,))
    for i in range(len(r)):
        if len(r[i]) == 8:
            r[i] = Supplier(r[i][0], r[i][1], r[i][2], r[i][4], r[i][5], r[i][6], r[i][7], r[i][3])
    return r
def searchCustomers(cnx, query):
    # wild card search to increase number of records
    query = '%' + query + '%'
    r = SQLSelect(cnx, Statements.SEARCH['Customer'], (query,))
    for i in range(len(r)):
        if len(r[i]) == 7:
            r[i] = Customer(r[i][0], r[i][1], r[i][2], r[i][3], r[i][4], r[i][5]==1, r[i][6])
    return r
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
