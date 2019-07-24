employee_list_query = '''
    SELECT
        DISTINCT(e.emp_no) AS EmployeeNum,
        birth_date AS DOB,
        first_name AS FirstName,
        last_name AS LastName,
        gender AS Gender,
        hire_date AS HireDate,
        (
            SELECT FORMAT(salary, 2) 
            FROM salaries s 
            WHERE s.emp_no = e.emp_no 
            ORDER BY s.to_date DESC LIMIT 1
        ) AS Salary,
        (
            SELECT dept_name 
            FROM departments d 
            WHERE d.dept_no = 
            (
                SELECT dept_no 
                FROM dept_emp de 
                WHERE de.emp_no = e.emp_no 
                ORDER BY de.to_date DESC LIMIT 1
            )
        ) AS Department,
        (
            SELECT title 
            FROM titles t 
            WHERE t.emp_no = e.emp_no 
            ORDER BY t.to_date DESC LIMIT 1
        ) AS Title
    FROM employees e
    ORDER BY EmployeeNum
    LIMIT 100; 
'''