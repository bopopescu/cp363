'''
Created on 2014-03-25

@author: mo
'''
import getpass
import os
import DatabaseHelper

PROG_HEADER = """Used Car Dealer
Version 1.0 Created in 2014
Bryan Chau & Mohamed Mohamedtaki
CP363 Database I
"""

def clear():
    os.system('cls')
    return
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
def main():
    con = DatabaseHelper.connect()
    DatabaseHelper.createTables(con)
    user = login(con)
    if con is not None and user is not None:
        clear()
        print(PROG_HEADER)
        print("Welcome, {}!".format(user.getEmployee().getName()))
        run = True
        while run:
            #clear()
            i = input()
            if i == 'exit':
                run = False
            else:
                print(i)
    DatabaseHelper.close(con)
    clear()
main()