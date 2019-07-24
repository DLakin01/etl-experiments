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


def salary_list_xml():
    data = pull_data(sql_query)
    salary_xml = ET.Element("SalaryList")
    salaries = ET.SubElement(salary_xml, "SalaryRanges")

    for i in range(0, 200000, 10000):
        employees_in_range = list(filter(lambda x: i - 9999 < int(x[6]) < i, data))

        if not employees_in_range:
            continue
        
        salary_range = ET.SubElement(salaries, "SalaryRange")
        salary_range.set("name", f"{i - 9999} - {i}")

        for e in employees_in_range:
            employee = ET.SubElement(salary_range, "empl")

            emp_id = ET.SubElement(employee, "Id")
            emp_id.text = str(e[0])

            name = ET.SubElement(employee, "FullName")
            name.text = f"{e[2]} {e[3]}"

            hire_date = ET.SubElement(employee, "HireDate")
            hire_date.text = '{:%m/%d/%Y}'.format(e[5])

            title = ET.SubElement(employee, "CurrentTitle")
            title.text = e[8]

            salary = ET.SubElement(employee, "CurrentSalary")
            salary.text = str(e[6])

    xml = ET.tostring(salary_xml)
    destination_file = open("/Users/macbook/Desktop/salary_list.xml", "wb")
    destination_file.write(xml)

    print("Generated XML")

def main():
    #employees_list_xml()
    salary_list_xml()

if __name__ == "__main__":
    main()