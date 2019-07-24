# Imports
from xml.etree import ElementTree as ET
from itertools import groupby

# Variables
from sql_queries import sql_query
from pull_data import pull_data

def employees_list_xml():
    data = pull_data(sql_query)
    employee_xml = ET.Element("EmployeeList")
    emp_list = ET.SubElement(employee_xml, "Employees")

    for d in data:
        item = ET.SubElement(emp_list, "empl")

        emp_id = ET.SubElement(item, "Id")
        emp_id.text = str(d[0])

        dob = ET.SubElement(item, "DOB")
        dob.text = '{:%m/%d/%Y}'.format(d[1])

        first_name = ET.SubElement(item, "FirstName")
        first_name.text = d[2]

        last_name = ET.SubElement(item, "LastName")
        last_name.text = d[3]

        gender = ET.SubElement(item, "Gender")
        gender.text = d[4]

        hire_date = ET.SubElement(item, "HireDate")
        hire_date.text = '{:%m/%d/%Y}'.format(d[5])

        current_salary = ET.SubElement(item, "CurrentSalary")
        current_salary.text = str(d[6])

        current_department = ET.SubElement(item, "CurrentDepartment")
        current_department.text = d[7]

        current_title = ET.SubElement(item, "CurrentTitle")
        current_title.text = d[8]

    xml = ET.tostring(employee_xml)
    destination_file = open("/Users/macbook/Desktop/employee_list.xml", "wb")
    destination_file.write(xml)

    print("Generated XML")


def main():
    employees_list_xml()

if __name__ == "__main__":
    main()