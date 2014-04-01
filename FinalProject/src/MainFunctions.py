'''
Created on 2014-03-26

@author: mo
'''
import getpass
import os
import DatabaseHelper
from datetime import date
from Entities import Car, Customer, Employee, Expense, Sale, Supplier, User

PROG_HEADER = """Used Car Dealer
Version 1.0 Created in 2014
Bryan Chau & Mohamed Mohamedtaki
CP363 Database I
"""

# screen clear
def clear():
    os.system('cls')
    print(PROG_HEADER)
    return
def cls():
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
        u = input("Username: ")
        p = getpass.getpass("Password: ")
        user = DatabaseHelper.getAccount(cnx, u, p)
        if user is None:
            go = input("Invalid username/password combination. Retry?(Y/N) ").upper() == 'Y'
    return user

# entity creators/deleters/updaters
def profitSummary(cnx,user):
    input("Your profit Summary")
    return

def newCar(cnx, user):
    clear()
    print("Please enter the following details for the car")
    vin = input("Vehicle Identification Number(VIN):\n").upper()
    make = input("Make: ").upper()
    model = input("Model: ").upper()
    year = 0
    while year <= 1900:
        try:
            year = int(input("Year: "))
        except:
            print("Invalid year, please enter a valid year > 1900")
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
    car = Car(vin, make, model, year, colour, sold, price)

    while True:
        try:
            suppliers = DatabaseHelper.searchSuppliers(cnx, input("Supplier: "))
            length = len(suppliers)
            if length == 0:
                print("Could not find supplier. Try again.")
            elif length == 1:
                supplier = suppliers[0]
                break
            else:
                print("\nFound suppliers: ")
                for i in range(length):
                    print("Result {}".format(i+1))
                    print(suppliers[i])
                index = -1
                while index < 0:
                    try:
                        index = int(input("Select supplier by result number: ")) - 1
                        if index > length -1 or index <0:
                            index = -1
                            print("Index out of bounds. Try again.")
                    except:
                        print("Incorrect input. Try again.")
                supplier = suppliers[index]
                break
        except:
            print("Could not find supplier. Try again.")
    
    try:
        DatabaseHelper.addCar(cnx, car,supplier, user)
        print("Car successfully added.")
        input("Please press enter to continue.")
    except:
        print("Could not add this car.")
        input("Please press enter to continue.")
    return

def newEmployee(cnx,user):
    clear()
    print("Please enter the following details for the Employee")
    
            
    name = input("Full Name: ")
    
    salary = 0
    while salary < 1:
        try:
            salary = int(input("Salary: "))
        except:
            print("Invalid salary")
            
    dateEmployed = date.today()
    
    while True:
        isManager = input("Is employee a manager?(Y/N): ").upper()
        if isManager == "Y":
            isManager = True
            break
        elif isManager == "N":
            isManager = False
            break
            
    mid = 0
    while mid < 1:
        try:
            mid = int(input("Manager id: "))
        except:
            print("Invalid manager id")
            mid = 0
            
    username = input("Username: ")
    password = input("Password: ")        
    e = Employee(0,name,salary,dateEmployed,None,isManager,mid)
    user = User(username, password, e)

    try:
        clear()
        DatabaseHelper.addEmployee(cnx, user)
        print("Employee successfully added.")
        input("Please press enter to continue.")
    except:
        print("Could not add employee.")
        input("Please press enter to continue.")
        
    return

def removeEmployee(cnx,user):
    clear()
    print("Please enter the id of the employee to remove")
    
    eid = 0
    while eid < 1:
        try:
            eid = int(input("Employee id: "))
        except:
            print("Invalid employee id")
            eid = 0
    try:
        clear()
        DatabaseHelper.removeEmployee(cnx, eid) #needs to just set date of departure field.
        print("Employee successfully removed")
        input("Please press enter to continue.")
    except:
        print("Could not remove employee.")
        input("Please press enter to continue.")
        
    return

def newExpense(cnx,user):
    clear()
    print("Please enter the following details for the Expense")
    
    date = date.today()
    
    cost = -1
    while cost < 0:
        try:
            cost = int(input("Cost of expense: "))
        except:
            print("Invalid cost")
            cost = -1
            
    details = input("Enter the details of the expense: \n")
    
    e = Expense(0,date,cost,details)

    try:
        clear()
        DatabaseHelper.addExpense(cnx, e,user)
        print("Expense successfully added.")
        input("Please press enter to continue.")
    except:
        print("Could not add expense.")
        input("Please press enter to continue.")
        
    return

def updateExpense(cnx,user):
    clear()
    print("Please enter the id of the expense to update")
    
    xid = 0
    while xid < 1:
        try:
            xid = int(input("Expense id: "))
        except:
            print("Invalid expense id")
            xid = 0
    
    DatabaseHelper.removeExpense(cnx, xid)
    
        
    return

def newSale(cnx,user):
    clear()
    print("Please enter the following details for the Sale")
    
    while True:
        exist = input("Create new customer?(Y/N): ").upper()
        if exist == "Y":
            c = newCustomer(cnx,user)
            if c != None:
                clear()
                print("Please enter the following details for the Sale")
                break
        elif exist == "N":
            break
    while True:
        vin = input("Vehicle Identification Number(VIN): ").upper()
        cars = DatabaseHelper.getCar(cnx, vin)
        if len(cars) == 0:
            print("Could not find car with VIN: {}".format(vin))
        elif len(cars) == 1:
            car = cars[0]
            break
        else:
            print("Found cars:")
            for i in range(len(cars)):
                print("Result {}".format(i+1))
                print(cars[i])
            index = -1
            while index < 0:
                try:
                    index = int(input("Select car by result number: ")) - 1
                    if index > len(cars) -1 or index <0:
                        index = -1
                        print("Index out of bounds. Try again.")
                except:
                    print("Incorrect input. Try again.")
            car = cars[index]
    try:
        customer = c
    except:
        while True:
            cname = input("Customer Name: ")
            customers = DatabaseHelper.searchCustomers(cnx, cname)
            if len(customers) == 0:
                print("Could not find customer with name: {}".format(cname))
            elif len(customers) == 1:
                customer = customers[0]
                break
            else:
                print("Found customers:")
                for i in range(len(customers)):
                    print("Result {}".format(i+1))
                    print(customers[i])
                index = -1
                while index < 0:
                    try:
                        index = int(input("Select customer by result number: ")) - 1
                        if index > len(customers) -1 or index <0:
                            index = -1
                            print("Index out of bounds. Try again.")
                    except:
                        print("Incorrect input. Try again.")
                customer = customers[index]
                break
        
    
    s = Sale(customer,car)
    DatabaseHelper.addSale(cnx, s, user)
    try:
        clear()
        
        print("Sale successfully added.")
        input("Please press enter to continue.")
    except:
        print("Could not add Sale")
        input("Please press enter to continue.")
    return

def newCustomer(cnx,user):
    clear()
    print("Please enter the following details for the new Customer")
               
    cname = input("Customer name: ")
    join_date = date.today()
    phone = input("Phone number: ")
    
    customer = Customer(0,cname,join_date,phone)
    try:
        clear()
        DatabaseHelper.addCustomer(cnx, customer, user)
        print("Customer successfully created")
        input("Please press enter to continue.")
        return customer
    except:
        print("Could not create customer")
        input("Please press enter to continue.")
        return None

def newSupplier(cnx,user):
    clear()
    print("Please enter the following details for the new Supplier")
               
    sname = input("Supplier name: ")
    phone = input("Phone number: ")
    postalCode = input("Postal code: ")
    street = input("Street: ")
    city = input("City: ")
    province = input("Province: ")
    country = input("Country: ")
    
    supplier = Supplier(0,sname,phone,street,city,province,country,postalCode)
    try:
        clear()
        DatabaseHelper.addSupplier(cnx, supplier,date.today(), user)
        print("Supplier successfully created")
        input("Please press enter to continue.")

    except:
        print("Could not create supplier")
        input("Please press enter to continue.")
    
    return
#Search Functions
def searchCars(cnx,user):
    cont = True
    while cont:
        clear()
        s = input("Enter a search query:")
        r = DatabaseHelper.searchCars(cnx, s)
        print("\nYour Search returned {} result(s).".format(len(r)))
        for i in range(len(r)):
            print(r[i])
        if input("Enter 'Y' to search again. Any other key to return to previous: ").upper() != 'Y':
            cont = False
    return

def searchEmployees(cnx,user):
    cont = True
    while cont:
        clear()
        s = input("Enter a search query:")
        r = DatabaseHelper.searchEmployees(cnx, s)
        for i in range(len(r)):
            print(r[i])
        if input("Enter 'Y' to search again. Any other key to return to previous: ").upper() != 'Y':
            cont = False
    return

def searchSales(cnx,user):
    cont = True
    while cont:
        clear()
        s = input("Enter a search query:")
        r = DatabaseHelper.searchSales(cnx, s)
        for i in range(len(r)):
            print(r[i])
        if input("Enter 'Y' to search again. Any other key to return to previous: ").upper() != 'Y':
            cont = False
    return

def searchExpenses(cnx,user):
    cont = True
    while cont:
        clear()
        s = input("Enter a search query:")
        r = DatabaseHelper.searchExpenses(cnx, s)
        for i in range(len(r)):
            print(r[i])
        if input("Enter 'Y' to search again. Any other key to return to previous: ").upper() != 'Y':
            cont = False
    return 

def searchSuppliers(cnx,user):
    cont = True
    while cont:
        clear()
        s = input("Enter a search query:")
        r = DatabaseHelper.searchSuppliers(cnx, s)
        for i in range(len(r)):
            print(r[i])
        if input("Enter 'Y' to search again. Any other key to return to previous: ").upper() != 'Y':
            cont = False
    return 

MANAGE_CARS_MENU = (("Add a new car",newCar),("Make a sale",newSale),("Search cars",searchCars),("Return to previous",None))
def manageCarsSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print("Please choose from the following options:")
        for j in range(len(MANAGE_CARS_MENU)):
            print("{}) {}".format(j+1, MANAGE_CARS_MENU[j][0]))
        i = input("Selection(number from above): ")
        
        if i.isdigit():
            i = int(i)
            if i == len(MANAGE_CARS_MENU):
                run = False
            else:
                MANAGE_CARS_MENU[i-1][1](cnx,user)
    return

MANAGE_EMPLOYEES_MENU = (("Add employee",newEmployee), ("Remove employee",removeEmployee),("Search employees",searchEmployees),("Return to previous",None))
def manageEmployeesSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print("Please choose from the following options:")
        for j in range(len(MANAGE_EMPLOYEES_MENU)):
            print("{}) {}".format(j+1, MANAGE_EMPLOYEES_MENU[j][0]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == len(MANAGE_EMPLOYEES_MENU):
                run = False
            else:
                MANAGE_EMPLOYEES_MENU[i-1][1](cnx,user)    
    return


MANAGE_EXPENSES_MENU = (("Add expense",newExpense), ("Update expense",updateExpense),("Return to previous",None))
def manageExpensesSelection(cnx, user):
    run = True
    while run == True:
        clear()
        print("Please choose from the following options:")
        for j in range(len(MANAGE_EXPENSES_MENU)):
            print("{}) {}".format(j+1, MANAGE_EXPENSES_MENU[j][0]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == len(MANAGE_EXPENSES_MENU):
                run = False
            else:
                MANAGE_EXPENSES_MENU[i-1][1](cnx,user)   
    return

MANAGE_SALES_MENU = [("Make a sale",newSale),("Search sales",searchSales),("Profit Summary",profitSummary),("Return to previous",None)]
def manageSalesSelection(cnx, user):
    run = True
    while run == True:
        clear()    
        print("Please choose from the following options:")
        for j in range(len(MANAGE_SALES_MENU)):
            print("{}) {}".format(j+1, MANAGE_SALES_MENU[j][0]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == len(MANAGE_SALES_MENU):
                run = False
            else:
                MANAGE_SALES_MENU[i-1][1](cnx,user)  
    return

MANAGE_SUPPLIERS_MENU = [("Add supplier",newSupplier),("Search Suppliers",searchSuppliers),("Return to previous",None)]
def manageSuppliersSelection(cnx, user):
    run = True
    while run == True:
        clear()    
        print("Please choose from the following options:")
        for j in range(len(MANAGE_SUPPLIERS_MENU)):
            print("{}) {}".format(j+1, MANAGE_SUPPLIERS_MENU[j][0]))
        i = input("Selection(number from above): ")
        if i.isdigit():
            i = int(i)
            if i == len(MANAGE_SUPPLIERS_MENU):
                run = False
            else:
                MANAGE_SUPPLIERS_MENU[i-1][1](cnx,user) 
    return

