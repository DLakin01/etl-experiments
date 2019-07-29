# Imports
from itertools import groupby
import json

# Variables
from sql_queries import sql_query
from pull_data import pull_data

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

    with open("/Users/macbook/Desktop/employees_list.json", 'w') as json_file:
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

    with open("/Users/macbook/Desktop/salary_list.json", "w") as json_file:
        json.dump(salary_list, json_file)


def department_list_json():
    data = pull_data(sql_query)
    department_list = []

    data = sorted(data, key=lambda x: x[7])
    for i, g in groupby(data, lambda x: x[7]):
        employees_in_department = list(g)
        item = {}
        item["Department"] = employees_in_department[0][7]
        item["Employees"] = []

        for e in employees_in_department:
            employee = {}
            employee["EmployeeNum"] = e[0]
            employee["Name"] = f"{e[2]} {e[3]}"
            employee["HireDate"] = '{:%m/%d/%Y}'.format(e[5])
            employee["Title"] = e[8]
            employee["Salary"] = e[6]
            employee["Department"] = e[7]
            item["Employees"].append(employee)

        department_list.append(item)

    with open("/Users/macbook/Desktop/department_list.json", "w") as json_file:
        json.dump(department_list, json_file)

    print("Generated JSON")
        
def main():
    employees_list_json()
    salary_list_json()
    department_list_json()

if __name__ == "__main__":
    main()