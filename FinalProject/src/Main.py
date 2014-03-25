'''
Created on 2014-03-25

@author: mo
'''
import DatabaseHelper
import os

def clear():
    os.system('cls')
def main():
    con = DatabaseHelper.connect()
    DatabaseHelper.createTables(con)
    if con is not None:
        run = True
        while run:
            #clear()
            i = input()
            if i == 'exit':
                run = False
            else:
                print(i)
    DatabaseHelper.close(con)
main()