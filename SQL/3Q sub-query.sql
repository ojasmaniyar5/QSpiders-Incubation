
# Question 1
SELECT * 
FROM emp 
WHERE dname 
LIKE '%S';

# Question 2
SELECT ename 
FROM emp 
WHERE sal = (SELECT MAX(sal) 
            FROM emp 
            WHERE dname = 'ACCOUNTING') 
AND dname = 'ACCOUNTING';

# Question 3
SELECT dname 
FROM emp 
WHERE comm = (SELECT MAX(comm) 
                    FROM emp);

# Question 4
SELECT employee_name 
FROM employees 
WHERE department_name 
LIKE 'O%';

# Question 5
SELECT * 
FROM employees 
WHERE department_number = (SELECT department_number 
                           FROM employees 
                           WHERE employee_name = 'Scott');

# Question 6
SELECT * 
FROM employees 
WHERE department_name = 'OPERATIONS AND ACCOUNTING';

# Question 7
SELECT * 
FROM employees 
WHERE salary > (SELECT salary 
                FROM employees 
                WHERE employee_name = 'Miller');

# Question 8
SELECT department_name 
FROM employees 
WHERE job = 'SALESMAN' 
GROUP BY department_name 
HAVING COUNT(*) >= 3;

# Question 9
SELECT department_name 
FROM employees 
WHERE manager_id IS NULL;

# Question 10
SELECT * 
FROM employees 
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Jones Manager');

# Question 11
SELECT employee_name 
FROM employees 
WHERE department_name IN ('Research', 'Accounting') 
AND manager_id IS NOT NULL 
GROUP BY employee_name 
HAVING COUNT(*) >= 2;

# Question 12
SELECT department_name 
FROM employees 
WHERE employee_name NOT LIKE 'S%' 
AND salary BETWEEN 1500 AND 3000;

# Question 13
SELECT loc 
FROM employees 
WHERE salary = (SELECT MIN(salary) 
                FROM employees 
                WHERE salary > 2000);

# Question 14
SELECT location 
FROM employees 
WHERE department_name = 'Accounting';

# Question 15
SELECT location 
FROM employees 
WHERE department_name = 'IT' 
GROUP BY location 
HAVING COUNT(*) > 4;

# Question 16
SELECT * 
FROM employees 
WHERE job <> (SELECT job 
              FROM employees 
              WHERE employee_name = 'Allen') 
AND salary > (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Martin');

# Question 17
SELECT * 
FROM employees 
WHERE location = (SELECT location 
                  FROM employees 
                  WHERE employee_name = 'Adam' 
                  AND manager_id IS NOT NULL);

# Question 18
SELECT job, manager_id 
FROM employees 
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Jones');

# Question 19
SELECT employee_name, hire_date, commission 
FROM employees 
WHERE employee_id = (SELECT manager_id 
                     FROM employees 
                     WHERE employee_name = 'Ford');

# Question 20
SELECT COUNT(*) 
FROM employees 
WHERE salary < (SELECT salary 
                FROM employees 
                WHERE employee_name = 'Blake' 
                AND manager_id IS NOT NULL);

# Question 21
SELECT * 
FROM employees 
WHERE location = 'Chicago' 
AND commission = 0;

# Question 22
SELECT * 
FROM employees 
WHERE department_name = 'Sales' 
AND salary > (SELECT AVG(salary) 
              FROM employees 
              WHERE department_name = 'Sales');

# Question 23
SELECT * 
FROM employees 
WHERE department_name = 'Research' 
AND job = 'MANAGER';

# Question 24
SELECT DISTINCT department_name 
FROM employees 
WHERE commission IS NOT NULL 
AND commission > 0;

# Question 25
SELECT department_name 
FROM employees 
WHERE salary = (SELECT MAX(salary) 
                FROM employees) 
AND manager_id IS NULL;

# Question 26
SELECT * 
FROM employees 
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Blake') 
AND commission > 0 
AND manager_id IS NOT NULL;

# Question 27
SELECT DISTINCT department_name, location 
FROM employees 
WHERE job = 'MANAGER' 
AND employee_id IN (SELECT manager_id 
                    FROM employees 
                    WHERE job = 'MANAGER');


# Question 28
SELECT department_name, location
FROM employees
WHERE job = 'CLERK'
AND manager_id = (SELECT employee_id 
                  FROM employees 
                  WHERE employee_name = 'Blake')
AND salary < (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Martin');

# Question 29
SELECT *
FROM employees
WHERE manager_id <> (SELECT employee_id 
                    FROM employees 
                    WHERE job = 'PRESIDENT')
AND commission > 0
AND salary > (SELECT MAX(salary) 
              FROM employees 
              WHERE job = 'CLERK');

# Question 30
SELECT *
FROM employees
WHERE hire_date > (SELECT MIN(hire_date) + INTERVAL 2 YEAR 
                   FROM employees)
AND salary > (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Blake');

# Question 31
SELECT location
FROM employees
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Blake');

# Question 32
SELECT *
FROM employees
WHERE job = (SELECT job 
             FROM employees 
             WHERE employee_name = 'Jones')
AND salary < (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Scott');

# Question 33
SELECT employee_name, department_name, salary_12 AS annual_salary
FROM employees
WHERE department_id IN (30, 20)
GROUP BY department_id
HAVING COUNT(_) >= 3;

# Question 34
SELECT *
FROM employees
WHERE salary < (SELECT MIN(salary) 
                FROM employees 
                WHERE job = 'SALESMAN');

# Question 35
SELECT *
FROM employees
WHERE hire_date < (SELECT MAX(hire_date) 
                   FROM employees);

# Question 36
SELECT DISTINCT salary
FROM employees
ORDER BY salary
LIMIT 1 OFFSET 2;

# Question 37
SELECT *
FROM employees
WHERE salary > (SELECT MAX(salary) 
                FROM employees 
                WHERE job = 'MANAGER');

# Question 38
SELECT *
FROM employees
WHERE hire_date > (SELECT MIN(hire_date) + INTERVAL 4 YEAR 
                   FROM employees)
AND salary < (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Blake');

# Question 39
SELECT department_name
FROM employees
WHERE location = 'New York';

# Question 40
SELECT location
FROM employees
WHERE employee_name NOT LIKE 'A%'
AND salary BETWEEN 1000 AND 3000;

# Question 41
SELECT department_name
FROM employees
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Blake');

# Question 42
SELECT department_name, location
FROM employees
WHERE employee_id = (SELECT manager_id 
                     FROM employees 
                     WHERE employee_id = (SELECT manager_id 
                                          FROM employees 
                                          WHERE employee_name = 'Martin'));

# Question 43
SELECT manager_id, job, department_id
FROM employees
WHERE commission = 0
AND location IN ('Chicago', 'Dallas');

# Question 44
SELECT _, salary_12 AS annual_salary
FROM employees
WHERE commission = (SELECT MAX(commission) 
                    FROM employees);

# Question 45
SELECT *
FROM employees
WHERE department_name = 'Sales'
AND commission > 0
AND hire_date < (SELECT MAX(hire_date) 
                 FROM employees);

# Question 46
SELECT department_name
FROM employees
WHERE employee_id = (SELECT manager_id 
                     FROM employees 
                     WHERE employee_id = (SELECT manager_id 
                                          FROM employees 
                                          WHERE employee_name = 'Ward'));

# Question 47
SELECT department_name
FROM employees
WHERE salary > (SELECT AVG(salary) 
                FROM employees 
                WHERE job = 'CLERK');

# Question 48
SELECT _, salary_1.25 AS new_salary
FROM employees
ORDER BY employee_id
LIMIT 1 OFFSET (SELECT COUNT(*) 
                FROM employees - 1);

# Question 49
SELECT department_id
FROM employees
WHERE department_name = 'Sales'
AND job = 'MANAGER';


# Question 49
SELECT department_name
FROM employees
WHERE salary = (SELECT MIN(salary) 
                FROM employees 
                WHERE manager_id IS NOT NULL)
AND manager_id IS NOT NULL;

# Question 50
SELECT hire_date, job
FROM employees
WHERE department_name = 'Sales';

# Question 51
SELECT location, department_name
FROM employees
WHERE job = 'PRESIDENT';

# Question 52
SELECT department_name
FROM employees
WHERE salary = (SELECT MAX(salary) 
                FROM employees 
                WHERE salary < 3000)
AND salary < 3000;

# Question 53
SELECT department_name
FROM employees
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Adams');

# Question 54
SELECT *
FROM employees
ORDER BY employee_id
LIMIT 1 OFFSET (SELECT COUNT(*) 
                FROM employees - 1);

# Question 55
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) 
                FROM employees 
                WHERE department_id = 30);

# Question 56
SELECT COUNT(*)
FROM employees
WHERE department_name = 'Research'
AND salary < (SELECT MIN(salary) 
              FROM employees 
              WHERE department_id = 10);

# Question 57
SELECT DISTINCT department_name
FROM employees
WHERE job = 'CLERK';

# Question 58
SELECT DISTINCT department_name
FROM employees
WHERE department_name LIKE '%L%';

# Question 59
SELECT *
FROM employees
WHERE hire_date > (SELECT hire_date 
                   FROM employees 
                   WHERE employee_name = 'Blake');

# Question 60
SELECT department_name
FROM employees
GROUP BY department_name
HAVING COUNT() >= 3 AND COUNT() <= 5;

# Question 61
SELECT location
FROM employees
WHERE manager_id IN (SELECT employee_id 
                     FROM employees 
                     WHERE salary > 2000);

# Question 62
SELECT *
FROM employees
WHERE department_name LIKE '%E%E%';

# Question 63
SELECT employee_name, salary
FROM employees
WHERE salary > (SELECT MAX(salary) 
                FROM employees 
                WHERE job = 'ANALYST');

# Question 64
SELECT *
FROM employees
WHERE location = 'Chicago';

# Question 65
SELECT employee_name
FROM employees
WHERE salary = (SELECT MIN(salary) 
                FROM employees 
                WHERE department_name = 'Research')
AND department_name = 'Research';

# Question 66
SELECT DISTINCT department_name
FROM employees
WHERE job = 'SALESMAN';

# Question 67
SELECT department_name
FROM employees
GROUP BY department_name
HAVING COUNT(*) >= 3;

# Question 68
SELECT employee_name
FROM employees
WHERE department_name IN ('Research', 'Accounting')
AND manager_id IN (SELECT employee_id 
                   FROM employees 
                   WHERE job = 'MANAGER')
GROUP BY employee_name
HAVING COUNT(DISTINCT manager_id) >= 2;

# Question 69
SELECT employee_name, job, location
FROM employees
WHERE job = 'MANAGER'
AND location = 'Chicago';

# Question 70
SELECT employee_name
FROM employees
WHERE salary = (SELECT MAX(salary) 
                FROM employees 
                WHERE location = 'Dallas' 
                AND salary < (SELECT MAX(salary) 
                              FROM employees 
                              WHERE location = 'Dallas'))
AND location = 'Dallas';

# Question 71
SELECT *
FROM employees
WHERE commission IS NULL OR commission = 0
AND hire_date > '1983-07-31';

# Question 72
SELECT employee_name
FROM employees
WHERE department_name IN ('Sales', 'Research')
AND employee_id IN (SELECT manager_id 
                    FROM employees 
                    WHERE department_name IN ('Sales', 'Research'))
GROUP BY employee_name
HAVING COUNT(DISTINCT employee_id) >= 2;

# Question 73
SELECT *
FROM employees
WHERE commission > (SELECT MAX(salary) 
                    FROM employees 
                    WHERE job = 'SALESMAN')
AND manager_id <> (SELECT employee_id 
                   FROM employees 
                   WHERE employee_name = 'King');


# Question 74
SELECT location
FROM departments
WHERE department_id IN (SELECT department_id 
                        FROM employees 
                        WHERE EXTRACT(YEAR FROM hire_date) = 1981);

# Question 75
SELECT department_name, MIN(salary)
FROM employees
GROUP BY department_name
HAVING MIN(salary) < (SELECT AVG(salary) 
                      FROM employees);

# Question 76
SELECT *
FROM employees
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Jones');

# Question 77
SELECT *
FROM employees
WHERE location LIKE '%O%O%';

# Question 78
SELECT employee_name
FROM employees
WHERE department_id = 10
AND salary > (SELECT MAX(salary) 
              FROM employees 
              WHERE department_id <> 10);

# Question 79
SELECT employee_name, job, MAX(salary)
FROM employees
GROUP BY job;

# Question 80
SELECT employee_id, employee_name
FROM employees
WHERE job = 'CLERK'
AND salary = (SELECT MAX(salary) 
              FROM employees 
              WHERE job = 'CLERK');

# Question 81
SELECT hire_date
FROM employees
WHERE employee_id = (SELECT manager_id 
                     FROM employees 
                     WHERE employee_id = (SELECT manager_id 
                                          FROM employees 
                                          WHERE employee_name = 'Smith'));

# Question 82
SELECT COUNT(*)
FROM employees
WHERE job = 'SALESMAN'
AND location IN ('New York', 'Chicago');

# Question 83
SELECT department_name
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) BETWEEN 1981 AND 1982
AND salary > 1800;

# Question 84
SELECT location
FROM employees
WHERE salary = (SELECT MAX(salary) 
                FROM employees)
AND manager_id IS NULL;

# Question 85
SELECT *
FROM employees
WHERE department_name = 'Accounting'
AND salary > (SELECT AVG(salary) 
              FROM employees 
              WHERE department_name = 'Accounting');

# Question 86
SELECT location
FROM employees
WHERE commission > 0;

# Question 87
SELECT *
FROM employees
WHERE manager_id <> (SELECT employee_id 
                     FROM employees 
                     WHERE job = 'PRESIDENT')
AND commission > 0
AND salary > (SELECT MAX(salary) 
              FROM employees 
              WHERE job = 'CLERK');

# Question 88
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) 
                FROM employees 
                WHERE department_id = 20);

# Question 89
SELECT department_name, location
FROM employees
WHERE job = 'CLERK'
AND manager_id = (SELECT employee_id 
                  FROM employees 
                  WHERE employee_name = 'Blake')
AND salary < (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Martin');

# Question 90
SELECT location, department_name
FROM employees
WHERE job = 'MANAGER'
AND salary < (SELECT MIN(salary) 
              FROM employees 
              WHERE job = 'CLERK');

# Question 91
SELECT location
FROM employees
WHERE commission > 0;

# Question 92
SELECT employee_id, employee_name, job
FROM employees
WHERE job LIKE '%E%'
ORDER BY employee_id DESC;

# Question 93
SELECT department_name, location, department_id
FROM employees
WHERE manager_id IN (SELECT manager_id 
                     FROM employees 
                     GROUP BY manager_id 
                     HAVING COUNT(*) > 1);

# Question 94
SELECT AVG(salary)
FROM employees
WHERE department_name = 'Accounting';

# Question 95
SELECT *
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 1981;

# Question 96
SELECT _, salary_1.35 AS new_salary
FROM employees
WHERE employee_name = 'Smith' OR job = 'PRESIDENT';

# Question 97
SELECT COUNT(*)
FROM employees
WHERE commission > salary;

# Question 98
SELECT *
FROM employees
WHERE salary/30 > 1500
AND EXTRACT(YEAR FROM hire_date) < 1982;

# Question 99
SELECT COUNT(*)
FROM employees
WHERE commission > salary;

# Question 100
SELECT *
FROM employees
WHERE salary/30 > 1500
AND EXTRACT(YEAR FROM hire_date) < 1982;

# Question 101
SELECT *
FROM employees
WHERE job = (SELECT job 
             FROM employees 
             WHERE employee_name = 'Smith')
AND department_id = (SELECT department_id 
                     FROM employees 
                     WHERE employee_name = 'Jones')
AND salary > (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Turner');

# Question 102
SELECT *
FROM employees
WHERE employee_name LIKE 'S%'
AND salary > (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Allen')
AND salary < (SELECT salary 
              FROM employees 
              WHERE employee_name = 'Ford');

# Question 103
SELECT *
FROM employees
WHERE job IN ('CLERK', 'ANALYST')
AND location <> 'Dallas';

# Question 104
SELECT department_name
FROM employees
WHERE job = 'MANAGER';

# Question 105
SELECT MAX(salary)
FROM employees
WHERE department_name = 'Sales';

# Question 106
SELECT DISTINCT salary
FROM employees
ORDER BY salary
LIMIT 1 OFFSET 1;

# Question 107
SELECT department_name
FROM employees
WHERE salary = (SELECT DISTINCT salary
                FROM employees
                ORDER BY salary
                LIMIT 1 OFFSET 2);

# Question 108
SELECT *
FROM employees
WHERE salary > (SELECT MAX(salary) 
                FROM employees 
                WHERE job = 'MANAGER');

# Question 109
SELECT *
FROM employees
WHERE salary > (SELECT MAX(salary) 
                FROM employees 
                WHERE job = 'MANAGER');

# Question 110
SELECT employee_id, job, salary
FROM employees
WHERE job = 'ANALYST'
AND salary > (SELECT MAX(salary) 
              FROM employees 
              WHERE job = 'MANAGER');

# Question 111
SELECT department_name, location
FROM employees
WHERE manager_id = (SELECT employee_id 
                    FROM employees 
                    WHERE employee_name = 'Clark');

# Question 112
SELECT *
FROM employees
WHERE location = 'Dallas';

# Question 113
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) 
                FROM employees 
                WHERE department_id = 20);

# Question 114
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) 
                FROM employees);

# Question 115
SELECT *
FROM employees
ORDER BY hire_date
LIMIT 1;