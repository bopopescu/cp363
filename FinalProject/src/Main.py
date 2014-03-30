'''
Created on 2014-03-25

@author: mo
'''
from MainFunctions import *

# menus and main
MANAGER_MENU = (("Manage Cars",manageCarsSelection), ("Manage Employees",manageEmployeesSelection), ("Manage Expenses",manageExpensesSelection), ("Manage Sales",manageSalesSelection), ("Profit Summary",profitSummary), ("Exit",None))
SALES_MENU = (("Add Cars", newCar), ("Make a Sale", newSale), ("Car Detail Search", search), ("Exit", None))

def main():
    con = DatabaseHelper.connect()
    DatabaseHelper.createTables(con)
    user = login(con)
    if con is not None and user is not None:
        run = True
        while run:
            clear()
            print("Welcome, {}!".format(user.getEmployee().getName()))
            if user.getEmployee().isManager():
                i = managerSelection()
                if i == len(MANAGER_MENU):
                    run = False
                elif i == 0:
                    continue
                else:
                    clear()
                    MANAGER_MENU[i-1][1](con, user)
            else:
                i = salesPersonSelection()
                if i == len(SALES_MENU):
                    run = False
                elif i == 0:
                    continue
                else:
                    clear()
                    SALES_MENU[i-1][1](con, user)
    DatabaseHelper.close(con)
    cls()
    return

def managerSelection():
    print("Please choose from the following options:")
    for j in range(len(MANAGER_MENU)):
        print("{}) {}".format(j+1, MANAGER_MENU[j][0]))
    i = input("Selection(number from above): ")
    if i.isdigit():
        i = int(i)
        if i > len(MANAGER_MENU) or i < 1:
            i = 0
    else:
        i = 0
    return i
def salesPersonSelection():
    print("Please choose from the following options:")
    for j in range(len(SALES_MENU)):
        print("{}) {}".format(j+1, SALES_MENU[j][0]))
    i = input("Selection(number from above): ")
    if i.isdigit():
        i = int(i)
        if i > len(SALES_MENU) or i < 1:
            i = 0
    else:
        i = 0
    return i
# run program
main()