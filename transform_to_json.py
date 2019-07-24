# Imports
import mysql.connector as mysql
import numpy as np
import json
import os

from datetime import datetime
from itertools import groupby
from decimal import Decimal
from pandas import cut

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
    data = pull_data(sql_query)
    salary_list = []
    
    for i in range(0, 200000, 10000):
        employees_in_range = list(filter(lambda x: i - 9999 < int(x[6]) < i, data))

        if not employees_in_range:
            continue

        item = {}
        item["SalaryRange"] = f"{i - 9999} - {i}"
        item["Employees"] = []

        for e in employees_in_range:
            employee = {}
            employee["EmployeeNum"] = e[0]
            employee["Name"] = f"{e[2]} {e[3]}"
            employee["HireDate"] = '{:%m/%d/%Y}'.format(e[5])
            employee["Title"] = e[8]
            employee["Salary"] = e[6]
            item["Employees"].append(employee)
        
        salary_list.append(item)

    with open("/Users/macbook/Desktop/salary_list.json", "w+") as json_file:
        json.dump(salary_list, json_file)


def main():
    #employees_list_json()
    salary_list_json()

if __name__ == "__main__":
    main()