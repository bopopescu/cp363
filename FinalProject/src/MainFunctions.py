'''
Created on 2014-03-26

@author: mo
'''
import getpass
import os
import DatabaseHelper
from Entities import *

PROG_HEADER = """Used Car Dealer
Version 1.0 Created in 2014
Bryan Chau & Mohamed Mohamedtaki
CP363 Database I
"""
MANAGE_CARS_MENU = ["Add car","Remove car","Return to previous"]
DELETE_CARS_MENU = ["Find cars","Remove car by VIN","Return to previous"]
MANAGE_EMPLOYEES_MENU = ["Add employee", "Remove employee","Return to previous"]
MANAGE_EXPENSES_MENU = ["Add expense", "Remove expense","Return to previous"]
MANAGE_SALES_MENU = ["Add sale","Return to previous"]


# screen clear
def clear():
    os.system('cls')
    return

# account login
def login(cnx):
    user = None
    u = ""
    p = ""
    go = True
    while user is None and go:
        clear()
        print(PROG_HEADER)
        u = input("Username: ")
        p = getpass.getpass("Password: ")
        user = DatabaseHelper.getAccount(cnx, u, p)
        if user is None:
            go = input("Invalid username/password combination. Retry?(Y/N) ").upper() == 'Y'
    return user

# entity creators
def newCar(cnx, user):
    print(PROG_HEADER)
    print("Please enter the following details for the car")
    vin = input("Vehicle Identification Number(VIN):\n").upper()
    make = input("Make: ").upper()
    model = input("Model: ").upper()
    year = 0
    while year <= 1900:
        try:
            year = int(input("Year: "))
        except:
            print("Invalid year, please enter a valid price > 0")
            year = 0
    colour = input("Colour: ").upper()
    sold = False
    price = 0
    while price <= 0:
        try:
            price = float(input("Price: $"))
        except:
            print("Invalid price, please enter a valid price > 0")
            price = 0
    c = Car(vin, make, model, year, colour, sold, price)
    try:
        clear()
        DatabaseHelper.addCar(cnx, c, user)
        print("Car successfully added.")
        input("Please press enter to continue.")
    except:
        print("Could not add this car.")
        input("Please press enter to continue.")
    return

#Search Functions
def searchCars():
    return

def searchEmployees():
    return

def searchSales():
    return

def searchExpenses():
    return 

SEARCH_MENU = (("Search Cars",searchCars),("Search Employees",searchEmployees),("Search Expenses",searchExpenses),("Search Sales",searchSales),("Return to previous",None))

def search(cnx, user):
    run = True
    while run == True:
        clear()
        print(PROG_HEADER)     
        print("Please choose from the following options:")
        for j in range(len(SEARCH_MENU)):
            print("{}) {}".format(j+1, SEARCH_MENU[j][0]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == len(SEARCH_MENU):
                run = False
            else:
                SEARCH_MENU[i-1][1]()
    return

def manageCarsSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print(PROG_HEADER)     
        print("Please choose from the following options:")
        for j in range(len(MANAGE_CARS_MENU)):
            print("{}) {}".format(j+1, MANAGE_CARS_MENU[j]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == 1:
                clear()
                newCar(cnx,user)
            elif i == 2:
                clear()
                deleteCarSelection(cnx,user)
            elif i == 3:
                run = False
    return

def deleteCarSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print(PROG_HEADER)     
        print("Please choose from the following options:")
        for j in range(len(DELETE_CARS_MENU)):
            print("{}) {}".format(j+1, DELETE_CARS_MENU[j]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == 1:
                clear()
                search(cnx,user)
            if i == 2:
                clear()
            elif i == 3:
                run = False
    return

def manageEmployeesSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print(PROG_HEADER)     
        print("Please choose from the following options:")
        for j in range(len(MANAGE_EMPLOYEES_MENU)):
            print("{}) {}".format(j+1, MANAGE_EMPLOYEES_MENU[j]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == 1:
                clear()
                newEmployee(cnx,user)
            elif i == 2:
                clear()
                deleteEmployee(cnx,user)
            elif i == 3:
                run = False
    return

def newEmployee(cnx,user):
    return

def deleteEmployee(cnx,user):
    return

def manageExpensesSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print(PROG_HEADER)     
        print("Please choose from the following options:")
        for j in range(len(MANAGE_EXPENSES_MENU)):
            print("{}) {}".format(j+1, MANAGE_EXPENSES_MENU[j]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == 1:
                clear()
                newEmployee(cnx,user)
            elif i == 2:
                clear()
                deleteEmployee(cnx,user)
            elif i == 3:
                run = False
    return

def newExpense(cnx,user):
    return

def deleteExpense(cnx,user):
    return

def manageSalesSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print(PROG_HEADER)     
        print("Please choose from the following options:")
        for j in range(len(MANAGE_SALES_MENU)):
            print("{}) {}".format(j+1, MANAGE_SALES_MENU[j]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == 1:
                clear()
                newSale(cnx,user)
            elif i == 2:
                run = False
    return

def newSale(cnx,user):
    return

