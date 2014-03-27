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
    DatabaseHelper.addCar(cnx, c, user)
    return

def newSale(cnx, user):
    return

def search(cnx, user):
    return