'''
This class contains all entity classes related to the system
Includes Car, Customer, Employee, Expense, Supplier classes

@author: Mohamed Mohamedtaki
'''
class Car:
    def __init__(self, vin, make, model, year, colour, sold, price):
        """
        Creates a car object
        """
        self._vin = vin
        self._make = make
        self._model = model
        self._year = year
        self._colour = colour
        self._sold = sold
        self._price = price
    def getVin(self):
        return self._vin
    def getMake(self):
        return self._make
    def getModel(self):
        return self._model
    def getYear(self):
        return self._year
    def getColour(self):
        return self._colour
    def isSold(self):
        return self._sold
    def getPrice(self):
        return self._price
    def toTuple(self):
        return (self._vin, self._make, self._model,\
                self._year, self._colour, 1 if self._sold else 0, self._price)
    def __str__(self):
        result = """VIN: {}
        MAKE: {}
        MODEL: {}
        YEAR: {}
        COLOUR: {}
        SOLD: {}
        PRICE: ${}
        """.format(self._cId, self._cName, self._joinDate, self._phone)
        return result

class Customer:
    def __init__(self, cid, name, date, phone):
        """
        Creates a customer object
        """
        self._cId = cid
        self._cName = name
        self._joinDate = date
        self._phone = phone
    def getId(self):
        return self._cId
    def getName(self):
        return self._cName
    def getJoinDate(self):
        return self._joinDate
    def getPhone(self):
        return self._phone
    def setId(self, i):
        self._cId = i
        return
    def __str__(self):
        result = """ID: {}
        NAME: {}
        DATE JOINED: {}
        PHONE: {}
        """.format(self._cId, self._cName, self._joinDate, self._phone)
        return result
    def toTuple(self):
        return (self._cId, self._cName, self._joinDate, self._phone)

class Employee:
    def __init__(self, eid, name, salary, dateEmployed, dateLeft, isManager, manager):
        """
        Creates an Employee object
        """
        self._eId = eid
        self._name = name
        self._salary = salary
        self._dateEmployed = dateEmployed
        self._dateLeft = dateLeft
        self._isManager = isManager
        self._managerId = manager
    def getId(self):
        return self._eId
    def getName(self):
        return self._name
    def getSalary(self):
        return self._salary
    def getDateEmployed(self):
        return self._dateEmployed
    def getDateLeft(self):
        return self._dateLeft
    def setId(self, i):
        self._eId = i
        return
    def setDateLeft(self, date):
        self._dateLeft = date
        return
    def addToSalary(self, amount):
        self._salary = self._salary + amount
        return
    def removeFromSalary(self, amount):
        self._salary = self._salary - amount
        return
    def isManager(self):
        return self._isManager
    def getManager(self):
        return self._managerId
    def __str__(self):
        result = """ID: {}
        NAME: {}
        SALARY: ${}
        DATE OF EMPLOYMENT: {}
        DATE OF DEPARTURE: {}
        IS MANAGER: {}
        """.format(self._eId, self._name, self._salary,\
                   self._dateEmployed, self._dateLeft, self._isManager)
        return result
    def toTuple(self):
        return (self._eId, self._name, self._salary,self._dateEmployed, self._dateLeft,
                1 if self._isManager else 0, self._managerId)
class Expense:
    def __init__(self, xid, date, cost, details):
        """
        Creates an Expense object
        """
        self._xId = xid
        self._date = date
        self._cost = cost
        self._details = details
    def getId(self):
        return self._xId
    def getDate(self):
        return self._date
    def getCost(self):
        return self._cost
    def getDetails(self):
        return self._details
    def setId(self, i):
        self._xId = i
        return
    def __str__(self):
        result = """ID: {}
        DATE: {}
        COST: ${}
        DETAILS:
        {}
        """.format(self._xId, self._date, self._cost, self._details)
        return result
    def toTuple(self):
        return (self._xId, self._date, self._cost, self._details)

class Supplier:
    def __init__(self, sid, name, phone, street, city, province, country, postalcode):
        """
        Creates a Supplier object
        """
        self._sId = sid
        self._sName = name
        self._phone = phone
        self._street = street
        self._city = city
        self._province = province
        self._country = country
        self._postalCode = postalcode
    def getId(self):
        return self._sId
    def getName(self):
        return self._sName
    def getPhone(self):
        return self._phone
    def getStreet(self):
        return self._street
    def getCity(self):
        return self._city
    def getProvince(self):
        return self._province
    def getCountry(self):
        return self._country
    def getPostalCode(self):
        return self._postalCode
    def getAddress(self):
        return """{}
        {}, {}
        {} {}
        """.format(self._street, self._city, self._province, self._country, self._postalCode)
    def setId(self, i):
        self._sId = i
        return
    def __str__(self):
        result = """ID: {}
        NAME: {}
        PHONE: {}
        ADDRESS: {}
        """.format(self._sId, self._sName, self._phone, self.getAddress())
        return result
    def toTuple(self):
        return (self._sId, self._sName, self._phone,self._postalCode, self._street, self._city, self._country,self._province)

class User:
    def __init__(self, username, password, employee):
        self._username = username
        self._password = password
        self._employee = employee
    def getUserName(self):
        return self._username
    def getEmployee(self):
        return self._employee
    def __str__(self):
        result = """USERNAME: {}
    ID: {}
    NAME: {}
    """.format(self._username, self._employee.getId(), self._employee.getName())
        return result
    def toTuple(self):
        return (self._employee.getId(), self._username, self._password)
    
class Sale:
    def __init__(self, customer, car):
        self._customer = customer
        self._car = car
    def getCustomer(self):
        return self._customer
    def getcar(self):
        return self._car
    def __str__(self):
        result = """CUSTOMER NAME: {}
    CAR DETAILS:
    {}
    """.format(self._customer.getName(), self._car)
        return result
    def toTuple(self):
        return (self._cid, self._vin)