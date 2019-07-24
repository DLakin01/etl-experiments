# Imports
import mysql.connector as mysql
import json
import numpy as np
import os
from datetime import datetime

# Variables
from config import mysql_config
from sql_queries import sql_query

def pull_data(sql_query):
    cnx = mysql.connect(**mysql_config)
    cursor = cnx.cursor()
    cursor.execute(sql_query)

    data = cursor.fetchall()
    cursor.close()

    if data:
        return data

def employees_list_json():
    data = pull_data(sql_query)
    employee_list = []

    for d in data:
        employee = {}
        employee["EmployeeId"] = d[0]
        employee["DOB"] = '{:%m/%d/%Y}'.format(d[1])
        employee["FirstName"] = d[2]
        employee["LastName"] = d[3]
        employee["Gender"] = d[4]
        employee["HireDate"] = '{:%m/%d/%Y}'.format(d[5])
        employee["CurrentSalary"] = d[6]
        employee["CurrentDepartment"] = d[7]
        employee["CurrentTitle"] = d[8]
        
        employee_list.append(employee)

    with open("/Users/macbook/Desktop/employees_list.json", 'w+') as json_file:
        json.dump(employee_list, json_file)


def salary_list_json():
        print("OK")

def main():
    employees_list_json()

if __name__ == "__main__":
    main()